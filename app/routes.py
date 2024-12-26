# Import necessary modules from Flask
from flask import Blueprint, request, jsonify

# Import User model and custom exceptions
from app.models import User
from app.exceptions import UserNotFoundError, ValidationError

# Create a blueprint for user-related routes
user_bp = Blueprint('user_bp', __name__)

# Route to get a list of all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve all users from the database.

    :return: A JSON response with a list of users and a 200 status code
             or an error message with a 500 status code
    """
    try:
        users = User.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to get a specific user by their ID
@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve a user by their ID.

    :param user_id: The ID of the user to retrieve
    :return: A JSON response with user details and a 200 status code
             or an error message with a 404/500 status code
    """
    try:
        user = User.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        else:
            # Raise an error if the user is not found
            raise UserNotFoundError("User not found")
    except UserNotFoundError as e:
        # Handle user not found errors
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to create a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.

    :return: A JSON response with the created user's ID and a 201 status code
             or an error message with a 400/500 status code
    """
    try:
        data = request.get_json()
        # Validate that required fields are provided
        if not data.get("name") or not data.get("email") or not data.get("password"):
            raise ValidationError("Missing required fields")

        # Create a User instance and save it to the database
        user = User(data["name"], data["email"], data["password"])
        user_id = user.save()
        return jsonify({"id": str(user_id)}), 201
    except ValidationError as e:
        # Handle validation errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to update an existing user's details
@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update the details of an existing user.

    :param user_id: The ID of the user to update
    :return: A JSON response with a success message and a 200 status code
             or an error message with a 404/400/500 status code
    """
    try:
        data = request.get_json()
        # Validate that the request body is not empty
        if not data:
            raise ValidationError("No data provided")

        # Update the user in the database
        result = User.update_user(user_id, data)
        if result.modified_count > 0:
            return jsonify({"message": "User updated successfully"}), 200
        else:
            # Raise an error if the user is not found
            raise UserNotFoundError("User not found")
    except UserNotFoundError as e:
        # Handle user not found errors
        return jsonify({"error": str(e)}), 404
    except ValidationError as e:
        # Handle validation errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to delete a user
@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by their ID.

    :param user_id: The ID of the user to delete
    :return: A JSON response with a success message and a 200 status code
             or an error message with a 404/500 status code
    """
    try:
        # Delete the user from the database
        result = User.delete_user(user_id)
        if result.deleted_count > 0:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            # Raise an error if the user is not found
            raise UserNotFoundError("User not found")
    except UserNotFoundError as e:
        # Handle user not found errors
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

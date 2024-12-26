# Import the mongo object from the app module
from app import mongo
from bson import ObjectId  # Import ObjectId for handling MongoDB document IDs

# User class for managing user-related operations
class User:
    def __init__(self, name, email, password):
        """
        Initialize a User object with name, email, and password.

        :param name: Name of the user
        :param email: Email address of the user
        :param password: Password of the user
        """
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        """
        Save the user data to the MongoDB database.

        :return: The ID of the newly inserted user document
        """
        user_data = {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
        return mongo.db.users.insert_one(user_data).inserted_id

    @staticmethod
    def get_all_users():
        """
        Retrieve all user documents from the database.

        :return: A list of all user documents
        """
        return list(mongo.db.users.find())

    @staticmethod
    def get_user_by_id(user_id):
        """
        Retrieve a single user document by its ID.

        :param user_id: The ID of the user to retrieve
        :return: The user document or None if not found
        """
        try:
            # Convert user_id to ObjectId
            user_id = ObjectId(user_id)
        except Exception:
            return None  # Return None if the ID is invalid

        return mongo.db.users.find_one({"_id": user_id})

    @staticmethod
    def update_user(user_id, data):
        """
        Update a user's details in the database.

        :param user_id: The ID of the user to update
        :param data: A dictionary containing the fields to update
        :return: The result of the update operation
        """
        try:
            # Convert user_id to ObjectId
            user_id = ObjectId(user_id)
        except Exception:
            return None  # Return None if the ID is invalid

        return mongo.db.users.update_one({"_id": user_id}, {"$set": data})

    @staticmethod
    def delete_user(user_id):
        """
        Delete a user document from the database.

        :param user_id: The ID of the user to delete
        :return: The result of the delete operation
        """
        try:
            # Convert user_id to ObjectId
            user_id = ObjectId(user_id)
        except Exception:
            return None  # Return None if the ID is invalid

        return mongo.db.users.delete_one({"_id": user_id})

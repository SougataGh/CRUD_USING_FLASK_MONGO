# CRUD_USING_FLASK_MONGO
This project is a Flask-based web application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource. The application exposes REST API endpoints and is containerized using Docker for ease of setup and deployment.
## Features
- CRUD Operations: Provides endpoints to manage users in the database.
- MongoDB Integration: Uses Flask-PyMongo to interact with MongoDB.
- RESTful API: Well-structured API endpoints for each operation.
- Modular Design: Organized using blueprints and follows best practices for scalability.
- Exception Handling: Robust error handling for various scenarios.
- Docker Support: Easily deployable using Docker.
## Prerequisites
Before setting up the application, ensure you have the following installed on your system:
- Python 3.8 or higher
- Docker and Docker Compose
- MongoDB (local or cloud-based, e.g., MongoDB Atlas)
- Git
## Setup and Installation
### 1. Clone the Repository :
```bash
git clone https://github.com/your-username/flask-mongo-crud.git
cd flask-mongo-crud
```
### 2. Setup MongoDB :
- Ensure MongoDB is running locally or configure a connection string for a cloud MongoDB instance.
- Update the MONGO_URI in app/config.py if necessary.

### 3. Run Using Docker :
- Build the Docker image:
```bash
docker build -t flask-mongo-crud .
```
- Start the container:
```bash
docker run -p 5000:5000 flask-mongo-crud
```
- The app will be available at http://localhost:5000.
## REST API Endpoints
### 1. Get All Users :
- Endpoint: GET /users
- Description: Retrieves all users from the database.
- Response: JSON array of users.
```json
[
  {
    "id": "64b7e63e5d3a2b1ec1f57f01",
    "name": "Sougata Ghosh",
    "email": "ghoshsougataa@example.com",
    "password": "hashed_password"
  }
]
```

### 2. Get a User by ID :
- Endpoint: GET /users/<id>
- Description: Retrieves a single user by ID.
- Response: JSON object of the user.

### 3. Create a New User :
Endpoint: POST /users
Description: Adds a new user to the database.
Request Body:
```json
{
  "name": "Sougata Ghosh",
  "email": "ghoshsougataa@gmail.com",
  "password": "hashed_password"
}
```
### 4. Update a User :
- Endpoint: PUT /users/<id>
- Description: Updates an existing user's details.
- Request Body: Provide any fields to update.

### 5.Delete a User :
- Endpoint: DELETE /users/<id>
- Description: Deletes a user from the database.

## File Structure
```bash
flask-mongo-crud/
│
├── app_factory.py          # Entry point for the application
├── app/
│   ├── __init__.py         # Package initialization
│   ├── config.py           # Configuration file
│   ├── user_routes.py      # User-related routes
│
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container instructions
├── README.md               # Project documentation
```

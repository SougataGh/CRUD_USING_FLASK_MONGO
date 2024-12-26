class UserNotFoundError(Exception):
    """Exception raised when a user is not found in the database."""
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    """Exception raised when there is a validation error in user input."""
    def __init__(self, message="Validation error occurred"):
        self.message = message
        super().__init__(self.message)

class DatabaseError(Exception):
    """Exception raised for errors related to the database."""
    def __init__(self, message="Database operation failed"):
        self.message = message
        super().__init__(self.message)

class BadRequestError(Exception):
    """Exception raised for bad requests, such as missing fields."""
    def __init__(self, message="Bad request, missing required fields"):
        self.message = message
        super().__init__(self.message)

class InternalServerError(Exception):
    """Exception raised for internal server errors."""
    def __init__(self, message="Internal server error occurred"):
        self.message = message
        super().__init__(self.message)

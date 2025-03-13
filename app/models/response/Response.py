    
from typing import Generic, TypeVar, Optional
from app.models.response import ErrorResponse

T = TypeVar("T")  # Define generic type

class ResponseModel(Generic[T]):
    """
    Represents a generic response model for API responses.
    """
    content: Optional[T]
    error: Optional[ErrorResponse]
    is_success: bool
    message: Optional[str]
    resource: Optional[str]

    def __init__(self, content: Optional[T] = None, error: Optional[ErrorResponse] = None,
                 is_success: bool = False, message: Optional[str] = None, resource: Optional[str] = None):
        """
        Initializes an instance of the ResponseModel class.
        :param content: The content of the response (generic type)
        :param error: An instance of ErrorResponse representing an error
        :param is_success: A boolean indicating if the response was successful
        :param message: A message associated with the response
        :param resource: The resource path or identifier related to the response
        """
        self.content = content
        self.error = error
        self.is_success = is_success
        self.message = message
        self.resource = resource

    def __repr__(self):
        """
        Returns a string representation of the ResponseModel instance.
        """
        return (f"ResponseModel(content={self.content}, error={self.error}, "
                f"is_success={self.is_success}, message={self.message}, resource={self.resource})")

class ErrorResponse:
    """
    Represents an error response for a REST API.
    """
    def __init__(self, error_type, message, instance, status, details=None):
        """
        Initializes an instance of the ErrorResponse class.
        :param error_type: Type of HTTP error
        :param message: Error message
        :param instance: The path called
        :param status: HTTP error code
        :param details: List of additional ErrorResponse objects (default: None)
        """
        self.error_type = error_type
        self.message = message
        self.instance = instance
        self.status = status
        self.details = details if details is not None else []

    def __repr__(self):
        """
        Returns a string representation of the ErrorResponse instance.
        """
        return (f"ErrorResponse(error_type={self.error_type}, message={self.message}, "
                f"instance={self.instance}, status={self.status}, details={self.details})")

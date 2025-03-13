class TokenResponse:
    """
    Represents a token response from an API.
    """
    def __init__(self, access_token, expires_in, token_type="Bearer"):
        """
        Initializes an instance of the TokenResponse class.
        :param access_token: The access token
        :param expires_in: Token expiration time in seconds
        :param token_type: The type of the token (default is 'Bearer')
        """
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type

    def __repr__(self):
        """
        Returns a string representation of the TokenResponse instance.
        """
        return (f"TokenResponse(access_token={self.access_token}, expires_in={self.expires_in}, "
                f"token_type={self.token_type})")

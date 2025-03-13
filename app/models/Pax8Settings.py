class Pax8Settings:
    """
    Represents settings for connecting to the Pax8 API.
    """

    def __init__(self, client_id: str, client_secret: str, audience: str, grant_type: str, base_url: str):
        """
        Initializes an instance of the Pax8Settings class.
        :param client_id: The client ID for OAuth authentication
        :param client_secret: The client secret for OAuth authentication
        :param audience: The audience for the token request
        :param grant_type: The grant type for the token request
        :param base_url: The base URL for the Pax8 API
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.audience = audience
        self.grant_type = grant_type
        self.base_url = base_url

    def __repr__(self):
        """
        Returns a string representation of the Pax8Settings instance.
        """
        return (f"Pax8Settings(client_id={self.client_id}, client_secret=<hidden>, "
                f"audience={self.audience}, grant_type={self.grant_type}, base_url={self.base_url})")

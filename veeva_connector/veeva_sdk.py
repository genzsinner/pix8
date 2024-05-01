from base_connector.error_handler import AuthenticationError
from veeva_connector.auth import VeevaAuth
from veeva_connector.veeva_api import VeevaAPI


class VeevaSDK:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.authenticate()

    def authenticate(self):
        try:
            self.token = VeevaAuth.authenticate(self.username, self.password)
        except Exception as e:
            raise AuthenticationError(f"Authentication failed: {e}")

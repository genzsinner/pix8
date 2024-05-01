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
        self.token = VeevaAuth.authenticate(self.username, self.password)

    def fetch_user_data(self):
        return VeevaAPI.fetch_user_data_from_veeva(self.token)

    def fetch_document_data(self):
        return VeevaAPI.fetch_document_data_from_veeva(self.token)

    def fetch_group_data(self):
        return VeevaAPI.fetch_group_data_from_veeva(self.token)


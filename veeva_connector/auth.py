import requests

from base_connector.error_handler import AuthenticationError, HTTPException


class VeevaAuth:
    @staticmethod
    def authenticate(username, password):
        url = "https://xxx/api/v23.2/auth/"

        data = {"username": username, "password": password}
        try:
            response = requests.post(url, data=data)

            if response.status_code == 200:
                return response.json()['sessionId']
            else:
                return AuthenticationError("Authentication fail.")     # Add Proper error handling
        except Exception as e:
            raise HTTPException(500, f"Error while authentication to veeva : {e}")

    @staticmethod
    def refresh_token(old_token):
        # Logic to refresh token if expired
        new_token = "<new_authentication_token>"
        return new_token

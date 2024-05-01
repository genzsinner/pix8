import requests
from base_connector.error_handler import HTTPException
from base_connector.response import SDKResponse


class VeevaAPI:

    @staticmethod
    def fetch_user_data_from_veeva(session_token):
        url = "VEEVA_FETCH_USERS_URL"
        headers = {
            "Authorization": f"Bearer {session_token}"
        }
        response = []
        try:
            resp_size = -1
            start = 0
            while resp_size != 0:
                response = requests.get(url=f"{url}{start}", headers=headers).json()
                resp_size = len(response.get("users"))
                start = start + resp_size + 1
                response += response.get('users')

            response = SDKResponse(status_code=200, json_data=response)
            return response.send_response()

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching documents: {str(e)}")

        # Except Authention error and send response acroding to thatand then regenerate the authention token and rerun.

    def fetch_document_data_from_veeva(session_token):
        url = "VEEVA_FETCH_DOCUMENTS_URL"
        headers = {
            "Authorization": f"Bearer {session_token}"
        }
        response = []
        try:
            resp_size = -1
            start = 0
            while resp_size != 0:
                response = requests.get(
                    url=f"{url}{start}", headers=headers).json()
                resp_size = len(response.get("documents"))
                start = start + resp_size + 1
                response += response.get('documents')
            response = SDKResponse(status_code=200, json_data=response)
            return response.send_response()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching documents: {str(e)}")

    def fetch_group_data_from_veeva(session_token):
        url = "VEEVA_FETCH_GROUPS_URL"
        headers = {
            "Authorization": f"Bearer {session_token}"
        }
        try:
            response = requests.get(url=f"{url}", headers=headers).json()
            response = SDKResponse(status_code=200, json_data=response.get('groups'))
            return response.send_response()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching documents: {str(e)}")



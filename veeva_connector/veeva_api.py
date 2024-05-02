import os
from io import BytesIO

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
            return response

        except Exception as e:
            raise HTTPException(status_code=500, message=f"Error fetching documents: {str(e)}")

        # Except Authention error and send response acroding to thatand then regenerate the authention token and rerun.

    @staticmethod
    def fetch_group_data_from_veeva(session_token):
        url = "VEEVA_FETCH_GROUPS_URL"
        headers = {
            "Authorization": f"Bearer {session_token}"
        }
        try:
            response = requests.get(url=f"{url}", headers=headers).json()
            return response
        except Exception as e:
            raise HTTPException(status_code=500, message=f"Error fetching documents: {str(e)}")

    @staticmethod
    def fetch_document_meta_data_from_veeva(session_token):
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
            return response
        except Exception as e:
            raise HTTPException(status_code=500, message=f"Error fetching documents: {str(e)}")

    @staticmethod
    def download_version_rendition_file_upload_to_s3(session_token, document_id, major_version, minor_version,
                                                     rendition_type, s3, bucket_name, s3_base_path):
        url = "download_version_rendition_file".format(document_id=document_id, major_version=major_version,
                                                       minor_virsion=minor_version,
                                                       rendition_type=rendition_type)
        headers = {
            "Authorization": f"Bearer {session_token}"
        }

        try:
            response = requests.get(url, headers=headers)
            # Extract the filename and extension from the Content-Disposition header
            _, params = response.headers.get('Content-Disposition', '').split(';', 1)
            original_filename = params.split('=')[-1].split("''")[-1]
            base_filename, file_extension = os.path.splitext(original_filename)

            # Create a BytesIO object from the response content
            file_content = BytesIO(response.content)

            s3.upload_fileobj(file_content, bucket_name,
                              s3_base_path + document_id + "/" + f"{major_version}_{minor_version}" + "/" +
                              "rendition" + "/" + f'{base_filename}{file_extension}')
            return {"message": f"Version source file uploaded to s3."}
        except Exception as e:
            raise HTTPException(status_code=500, message=f"Error fetching documents: {str(e)}")

    @staticmethod
    def fetch_version_wise_renditions(session_token, document_id, major_version, minor_version):
        url = "FETCH_VERSION_WISE_RENDITIONS".format(document_id=document_id)
        headers = {
            "Authorization": f"Bearer {session_token}"
        }

        try:
            response = requests.get(url, headers=headers)
            return response

        except Exception as e:
            print(f"Error : {e}")

    @staticmethod
    def download_version_source_file_upload_to_s3(session_token, document_id, major_version, minor_version, s3,
                                                  bucket_name, s3_base_path):
        url = "download_version_source_file".format(document_id=document_id, major_version=major_version,
                                                    minor_virsion=minor_version)
        headers = {
            "Authorization": f"Bearer {session_token}"
        }

        try:
            response = requests.get(url, headers=headers)

            # Extract the filename and extension from the Content-Disposition header
            _, params = response.headers.get('Content-Disposition', '').split(';', 1)
            original_filename = params.split('=')[-1].split("''")[-1]
            base_filename, file_extension = os.path.splitext(original_filename)

            # Create a BytesIO object from the response content
            file_content = BytesIO(response.content)

            s3.upload_fileobj(file_content, bucket_name,
                              s3_base_path + document_id + "/" + f"{major_version}_{minor_version}" + "/" + f'{base_filename}{file_extension}')
            return {"message": f"Version source file uploaded to s3."}
        except Exception as e:
            print(f"Error : {e}")

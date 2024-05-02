import boto3
from base_connector.error_handler import AuthenticationError, S3Error
from base_connector.response import SDKResponse
from veeva_connector.auth import VeevaAuth
from veeva_connector.schema import DocumentMetaDataInputSchema
from veeva_connector.veeva_api import VeevaAPI
from typing import Union, Dict, Any


class VeevaSDK:
    def __init__(self, username: str, password: str, s3_base_path: str = None,
                 bucket_name: str = None, region_name: str = None,
                 aws_access_key_id: str = None, aws_secret_access_key: str = None) -> None:
        self.username = username
        self.password = password
        self.token: Union[str, None] = None
        self.s3 = None
        self.setup_s3(s3_base_path, bucket_name, region_name, aws_access_key_id, aws_secret_access_key)
        self.authenticate()

    def setup_s3(self, s3_base_path: str, bucket_name: str, region_name: str,
                 aws_access_key_id: str, aws_secret_access_key: str) -> None:
        if s3_base_path and bucket_name and region_name and aws_access_key_id and aws_secret_access_key:
            self.s3 = boto3.client('s3',
                                   aws_access_key_id=aws_access_key_id,
                                   aws_secret_access_key=aws_secret_access_key,
                                   region_name=region_name)

    def authenticate(self) -> None:
        self.token = VeevaAuth.authenticate(self.username, self.password)

    def fetch_user_data(self) -> Dict[str, Any]:
        """Fetches user data from Veeva."""
        response = VeevaAPI.fetch_user_data_from_veeva(self.token)
        response = SDKResponse(status_code=200, json_data=response)
        return response.send_response()

    def fetch_group_data(self) -> Dict[str, Any]:
        """Fetches group data from Veeva."""
        response = VeevaAPI.fetch_group_data_from_veeva(self.token)
        response = SDKResponse(status_code=200, json_data=response.get('groups'))
        return response.send_response()

    def fetch_document_data(self, meta_data: Union[DocumentMetaDataInputSchema, None] = None , version_source_file: bool = False,
                            version_wise_rendition_file: bool = False) -> Dict[str, Any]:
        """Fetches document data from Veeva."""
        if (version_source_file or version_wise_rendition_file) and self.s3 is None:
            error_msg = ("S3 parameters are required for fetching document data with version_source_file, "
                         "version_wise_rendition_file. Required parameters: s3_base_path, bucket_name, "
                         "region_name, aws_access_key_id, aws_secret_access_key")
            raise S3Error(status_code=400, message=error_msg)

        print(meta_data)

        document_meta_data = VeevaAPI.fetch_document_meta_data_from_veeva(self.token)


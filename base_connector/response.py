class SDKResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self.json_data = json_data if json_data is not None else {}

    def send_response(self):
        return {'status_code': self.status_code, "response":self.json_data}
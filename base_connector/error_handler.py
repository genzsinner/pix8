class Errorhandler(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(f"{status_code}:{message}")
        self.error_code = status_code

class AuthenticationError(Errorhandler):
    def __init__(self, message: str) -> None:
        super().__init__(401, message)


class HTTPException(Errorhandler):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(status_code, message)


class S3Error(Errorhandler):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(status_code, message)

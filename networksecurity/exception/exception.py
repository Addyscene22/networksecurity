import sys
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        return (
            f"Error occurred in python script name [{self.file_name}] "
            f"line number [{self.lineno}] error message [{self.error_message}]"
        )

if __name__ == '__main__':
    try:
        logger.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

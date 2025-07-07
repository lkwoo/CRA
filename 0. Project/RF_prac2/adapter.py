class Azure:
    def ms_connect(self):
        pass

    def ms_login(self, ID, password):
        pass

    def ms_sendData(self):
        pass

    def ms_receiveData(self):
        pass

    def ms_disconnect(self):
        pass


class AWS:
    def aws_conn(self, id, password):
        pass

    def aws_setData(self):
        pass

    def aws_getData(self):
        pass

    def aws_bye(self):
        pass

class Adapter(Azure):
    def __init__(self, aws):
        self._aws = aws

def run(az):
    az.ms_connect()
    az.ms_login("KFC", "1234")
    az.ms_sendData()
    az.ms_receiveData()
    az.ms_disconnect()


if __name__ == "__main__":
    run(Azure())
    run(AWS())

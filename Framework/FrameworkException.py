class FrameworkException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__("FrameworkException: {:S}".format(msg))


class MultipleInstancesException(FrameworkException):
    def __init__(self, msg: str) -> None:
        super().__init__("MultipleInstancesException: {:S}".format(msg))

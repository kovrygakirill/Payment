class MyException(Exception):
    def __init__(self, message: str):
        self.message = message


class ProblemWithDataBase(MyException):
    pass


class NotValidUserProfile(MyException):
    pass


class LackOfBalance(MyException):
    pass


class NotValidTINsForSend(MyException):
    pass


class NotValidMoneyForSend(MyException):
    pass

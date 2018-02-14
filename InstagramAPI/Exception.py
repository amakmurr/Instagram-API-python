class LoginFailedException(Exception):

    def __init__(self, message):
        super(LoginFailedException, self).__init__(message)


class UserNotFoundException(Exception):

    def __init__(self, message):
        super(UserNotFoundException, self).__init__(message)


class MediaNotFoundException(Exception):

    def __init__(self, message):
        super(MediaNotFoundException, self).__init__(message)

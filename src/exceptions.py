class OnLibraryException(Exception):
    detail = 'Unknown error'

    def __init__(self, *args):
        super().__init__(self.detail, *args)


class ObjectNotFound(OnLibraryException):
    detail = 'Object was not found'

class ValidationError(Exception):
    def __init__(self, message=None):
        super().__init__(f'Post code is not valid')

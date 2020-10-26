class InvalidOperationError(Exception):
    """
    Should be used when a given operation is done on an invalid state.
    """
    def __init__(self, message):
        self.message = message
        pass

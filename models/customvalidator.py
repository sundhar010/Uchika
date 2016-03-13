class IS_IIITS():
    def __init__(self, Email, error_message="Is not IIITS mail"):
        self.Email = Email
        self.error_message = error_message

    def __call__(self, value):
        error = None
        print value
        if not "@iiits.in" in value:
            error = self.error_message
        return (value, error)

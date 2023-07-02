class IllegalArgumentException(RuntimeError):
    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(*args)

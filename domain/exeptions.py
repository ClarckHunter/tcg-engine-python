class InvalidMove(Exception):
    def __init__(self, reason: str, phase:str | None = None):
        self.reason = reason
        self.phase = phase
        super().__init__(reason)
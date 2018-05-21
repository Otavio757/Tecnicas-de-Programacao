class ConcepaSummary:
    def __init__(self, to6am, to12h, to18h, to24h):
        self.to6am = to6am
        self.to12h = to12h
        self.to18h = to18h
        self.to24h = to24h

    def __str__(self):
        return f"INFO:\r\nUnitl 6AM crossed {self.to6am} cars\r\nUntil 12H {self.to12h}\r\nUntil 18H {self.to18h}\r\nIn the whole day {self.to24h}"

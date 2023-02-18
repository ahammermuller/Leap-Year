class  Countdown:
    def __init__(self, start, step=1):
        self.current = int(start)
        self.step = int(step)

    def down(self):
        self.current -= self.step

    @property
    def complete(self):
        return self.current <= 0


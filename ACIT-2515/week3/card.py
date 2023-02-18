class Card:
    def __init__(self, value, color):
        try:
            value = int(value)
        except ValueError:
            raise AttributeError("Not a good number")

        if not 0 < value <=10:
            raise AttributeError("Invalid value for card")
        if color != "red" and color !="black":
            raise AttributeError("Invalid color")
        self.value = value
        self.color = color

    def is_stronger_than(self, other_card):
        return self.value > other_card.value
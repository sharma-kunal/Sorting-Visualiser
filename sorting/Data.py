class Data:
    # Total of data to sort
    length = 32

    def __init__(self, value, color=None):
        self.value = value
        self.set_color(color)

    def set_color(self, color=None):
        if not color:
            color = 'cyan'
        self.color = color
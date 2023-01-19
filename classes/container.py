class container:
    def __init__(self, value, position):
        if isinstance(value, str):
            raise TypeError
        if isinstance(position, tuple):
            raise TypeError
        self.value = value
        self.position = position
class container:
    def __init__(self, value, position):
        if not isinstance(value, str):
            raise TypeError('value should be a string only')
        if not isinstance(position, tuple):
            raise TypeError('value should be a tuple only')
        self.value = value
        self.position = position
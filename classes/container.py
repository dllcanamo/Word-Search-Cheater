class container:
    def __init__(self, value, position):
        if not isinstance(value, str):
            raise TypeError('value should be a string only')
        if not isinstance(position, tuple):
            raise TypeError('value should be a tuple only')
        self.value = value
        self.position = position

    def get_lower_left_coordinates(self):
        new_x = self.position[0] + 1
        new_y = self.position[1] - 1
        return (new_x, new_y)

    def get_lower_right_coordinates(self):
        new_x = self.position[0] + 1
        new_y = self.position[1] + 1
        return (new_x, new_y)
    
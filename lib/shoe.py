#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size

    def get_brand(self):
        return self._brand
    def set_brand(self, value):
        self._brand = value
    def get_size(self):
        return self._size
    def set_size(self, value):
        if type(value) in (int,):
            self._size = value
        else:
            print("size must be an integer")
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)
    
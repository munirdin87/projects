class Car:
    """this is a simple class to learn how a class works"""

    def __init__(self, brand, color, tpye_, size, h_power):
        self.brand = brand
        self.color = color
        self.type_ = color
        self.size = size
        self.h_power = h_power


    def drive(self):
        print('You can drive me ')


    def start(self):
        print("vroom vroom vroom")


    def stop(self):
        print('I stopped, help me driver')
bmw = Car('bmw', 'black', 'sedan', 'full', 250)

bmw.drive()
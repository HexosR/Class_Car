class car:
    def __init__(car, make, model, year):
        car.make = make
        car.model = model
        car.year = year

    def get_make(car):
        return car.make

    def get_model(car):
        return car.model
    
    def get_year(car):
        return car.year

    def set_make(car, make):
        car.make = make

    def set_model(car, model):
        car.model = model

    def set_year(car, year):
        car.year = year

    def __str__(car):
        return 'Make: ' + car.make + '\n' + 'Model: '  + car.model + '\n' + 'Year: ' + car.year

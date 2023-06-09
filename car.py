class Car:
    def __init__(self, make, model, year):
        self._make = make # protected attribute
        self.model = model # protected attribute
        self.__year = year # private attribute  

    def start_engine(self):
        self.__ignite_spark()
        print("Engine start . .")
class House:
    A: float
    p: float

    def __init__(self, house_number: int, a: float, p: float):
        """
        Initializes the House object.
        :param house_number: the house number
        :param a: the area of the house
        :param p: the performance of the PV system
        """
        self.house_number = house_number
        self.A = a
        self.p = p

    def __str__(self):
        """
        Returns a string representation of the House object.
        :return: a string representation of the House object
        """
        return "House " + str(self.house_number) + ": " + str(self.A) + " m^2, "

class Address:

    # constructors
    def __init__(self, street, number, zipcode, city):
        self.street = street
        self.number = number
        if (zipcode >= 10000) and (zipcode <= 99999):
            self.zipcode = zipcode
        else:
            print("Wrong zipcode")
        self.city = city

    def get_address(self):
        return self.street + " " + str(self.number) + ", " + \
            str(self.zipcode) + " " + self.city

    # getters and setters
    def get_street(self):
        return self.street

    def get_zipcode(self):
        return self.zipcode

    def set_street(self, street):
        self.street = street

    def set_zipcode(self, zp):
        self.zipcode = zp

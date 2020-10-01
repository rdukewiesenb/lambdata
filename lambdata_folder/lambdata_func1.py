# import pandas as import pd


"""
DOCUMENTATION:
'location' = city property is located in
'property_type' = single-family house, duplex, apartment, or condo
'square_footage' = size of the property in square feet
'num_bath' = number of bathrooms on the property
'num_bed' = number of bedrooms on the property
'type_of_sale' = buy, sell or rent
'price' = price of property or monthly rent
"""
class RealEstate:
    def __init__(self, location, property_type, square_footage, num_bath, num_bed):
        self.location = str(location)
        self.property_type = property_type
        self.square_footage = int(square_footage)
        self.num_bath = int(num_bath)
        self.num_bed = int(num_bed)

    def for_sale(self, type_of_sale, price):
        return f"A {self.num_bed} bed-{self.num_bath} bath, {self.square_footage} sq. foot {self.property_type}" + \
             f" in {self.location} is for {type_of_sale} at {price}."
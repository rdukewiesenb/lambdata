""" Basic unit tests for Lambdata Package """

from random import randint
import unittest
from lambdata_func1 import RealEstate

# (self, location, property_type, square_footage, num_bath, num_bed):

class RealEstateTest(unittest.TestCase):
    def setUp(self):
        self.house = RealEstate("DC", "house", 500, 1, 1)
    def test_real_estate(self):
        self.assertIn("house", self.house.property_type)
        self.assertNotIn("off the market", self.house.property_type)

# class ExampleTests(unittest.TestCase):
#     def test_increment(self):
#         x0 = 0
#         y0 = increment(x0)
#         self.assertEqual(y0, 1)

#         x1 =-1
#         y1 = increment(x1)
#         self.assertEqual(y1, 0)

#         x2 = 10.5
#         y2 = increment(x2)
#         self.assertEqual(y2, 11.5)



# class SocialMediaUser(unittest.TestCase):
#     def setUp(self):
#         """ Common default setup code that runs before our tests. """
#         """ We can create attributes in any method. """
#         self.user1 = SocialMediaUser("Jimmy", "France")
#         self.user2 = SocialMediaUser("Craig", "Kenya")
#         self.user3 = SocialMediaUser("Nick", "Nova Scotia", upvotes=50)

#     def test_name(self):
#         self.assertEqual(self.user1.name, "Jimmy")
#         self.assertEqual(self.user2.name, "Craig")
        
#     def test_unpopular_popular(self):
#         """ Testing to see if the is_popular methods works as intended. """
#         self.assertFalse(self.user3.is_popular())
#         self.user3.receive_upvotes(randint(101, 1000))
#         self.assertTrue(self.user3.is_popular())

""" This argument is used to test that all classes work as intended. """
if __name__ == "__main__":
    unittest.main()

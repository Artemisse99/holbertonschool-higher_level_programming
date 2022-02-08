""" unittest module about rectangle """

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(1, 2)

    def tearDown(self):
        Base.reset()

    def creation(self):
        self.assertTrue(isinstance(self.rectangle, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))
    
    def test_id_rec(self):
        """Test Rectangle class: check for id."""

        self.assertEqual(self.rectangle.id, 1)

        self.rectangle = Rectangle(3, 3)
        self.assertEqual(self.rectangle.id, 2)

        self.rectangle = Rectangle(4, 4)
        self.assertEqual(self.rectangle.id, 3)

        self.rectangle = Rectangle(6, 2, 8, 8, 12)
        self.assertEqual(self.rectangle.id, 12)
    
        self.rectangle = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(self.rectangle.id, 34)

        self.rectangle = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(self.rectangle.id, -5)

        self.rectangle = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(self.rectangle.id, 9)

        self.rectangle = Rectangle(10, 10)
        self.assertEqual(self.rectangle.id, 4)

    def test_creation_wrong(self):
        with self.assertRaises(TypeError) as err:
            Rectangle("Godines", 2)
            
        with self.assertRaises(TypeError) as err:
            Rectangle(1, "Gomez")

        with self.assertRaises(TypeError) as err:
            Rectangle("Godines", "Gomez")

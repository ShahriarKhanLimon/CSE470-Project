from django.test import TestCase, Client
from django.urls import reverse
from App_Shop.models import Category, Product

# Create your tests here.

#Testing models classes
class CategoryrTest(TestCase):
    def test__str__(self):
        category=Category(title="T shirt")
        self.assertEqual(category.__str__(),"T shirt")

class ProductTest(TestCase):
    def test__str__(self):
        category=Category(title="shirt")
        category.save()
        item = Product(name="Black T shirt", price=500, category = category)
        item.save()
        self.assertEqual(item.__str__(),"Black T shirt")
from django.test import TestCase
from .models import Image,Location,Category

import pyperclip

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.web =Image(name='Web',description='Nice Image',image='web.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.web,Image))
    def test_save_method(self):
        self.web.save_image()  
        images =Image.objects.all()
        self.assertTrue(len(images) > 0)  
    # def test_delete_image(self):
    #      self.web.save_image() 
    #      self.assertTrue(Image.delete_image(1),True)

    class CategoryTestClass(TestCase):
       def setUp(self):
        self.category = Category(category='Fashion')

       def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
    
    #Test to save the method
       def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    



class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location="Nairobi")

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)     

   
     
         
    
             

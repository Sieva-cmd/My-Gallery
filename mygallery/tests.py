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
    def test_delete_image(self):
         self.web.save_image() 
         self.assertTrue(Image.delete_image(1),True)

   
     
         
    
             

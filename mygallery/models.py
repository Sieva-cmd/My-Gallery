
from django.db import models
import pyperclip


# Create your models here.

class Location(models.Model):
    location =models.CharField(max_length=60)
      
    def __str__(self):
        return self.location

    def save_location(self):
        self.save()    
    
class Category(models.Model):
    category =models.CharField(max_length=60) 

    def __str__(self):
        return self.category
        
    def save_category(self):
        self.save()            



class Image(models.Model):
    name =models.CharField(max_length=60)
    description=models.CharField(max_length=200)
    image =models.ImageField(upload_to ='photos/',blank=True)
    location =models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):

        return self.name

    class Meta:
        ordering = ['name'] 


         
    def save_image(self):
        self.save()  
    @classmethod    
    def delete_image(cls,id):
        image =cls.objects.filter(image_id=id).delete()
        return image
        # Image.objects.filter(id=id).delete() 


    def get_all_images(self):
        self.objects.all()  

    @classmethod
    def filter_by_location(cls,location) :
        images =cls.objects.filter(location__in=location) 
        return images 
    @classmethod     
    def  search_image_by_category(cls,search_term):
        images =cls.objects.filter(category__category__icontains=search_term)   
        return images  

    @classmethod
    def get_image_by_id(cls,image_id):
   
        image =cls.objects.filter(id = image_id)
        return image

           



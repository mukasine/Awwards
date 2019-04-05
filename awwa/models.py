from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 60,null = True)
    image = models.ImageField(upload_to = "images/",null = True)
    user = models.ForeignKey(User,null=True)
    
    link = models.CharField(max_length = 70,null = True)
    # likes = models.IntegerField(default=0)
    description = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    # profile = models.ForeignKey(Profile, null=True) 
    # comments = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    def update_description(self,new_description):
        self.image_description = new_description
        self.save()


    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains = search_term)
        return project

    class Meta:
        ordering = ['-pub_date']
class Profile(models.Model):
    username = models.CharField(default='User',max_length=60)
    profile_image = models.ImageField(upload_to = "profile/",null=True)
    bio = models.TextField(default='',blank = True)
    project = models.ForeignKey(Project,null=True)
    contact = models.TextField(null = True)
    project = models.IntegerField(default=0)



    def __str__(self):
        return self.username

    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save()

    # @classmethod
    # def search_by_n(cls,search_term):
    #   photos = cls.objects.filter(name__icontains = search_term)
    #   return photos

    
class Rating(models.Model):
    user = models.ForeignKey(User, null= True)
    project = models.ForeignKey(Project, null= True)
    user = models.ForeignKey(User, null= True)
    project = models.ForeignKey(Project, null= True,related_name='rating')
    design= models.IntegerField(default=0)
    usability= models.IntegerField(default=0)
    content= models.IntegerField(default=0)
    def __str__(self):
        return self.content


    def delete_content(self):
        self.delete()

    def save_content(self):
        self.save()
class Votes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True,)
    project =  models.ForeignKey(Project,on_delete=models.CASCADE)
    design = models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))))
    usability = models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))))
    content = models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))))

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

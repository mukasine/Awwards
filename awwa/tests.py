from django.test import TestCase
from .models import Project,Profile,Rating

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Project()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Project))

     
class RatingTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.wecode= Rating()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Rating))

   
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.wecode= Profile( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_profile()
        image = Profile.objects.all()
        self.assertTrue(len(image) > 0) 
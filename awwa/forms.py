from django import forms
from .models import Project,Profile,Rating

class awwaLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }   
class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']
class RatingForm(forms.ModelForm):
	model = Rating
	design = forms.IntegerField(label='design')
	
	usability= forms.IntegerField(label='Project Caption')
	content= forms.IntegerField(label = 'Project Field')
class VotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user','project','posted_on']
   
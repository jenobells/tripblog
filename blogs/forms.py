from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'description', 'date',
            'headerImage', 'image1', 'image2', 'image3', 'location')


# JobForm is the name of our form
# forms.ModelForm - tells Django that this form is a ModelForm
# (so Django will do some magic for us)

# class Meta - tells Django which model
# should be used to create this form (model = Job)

# fields - we specify which fields should be in our form

# https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/

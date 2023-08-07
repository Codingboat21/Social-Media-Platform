from django import forms
from .models import PImages ,Post

class POSTForm(forms.ModelForm):
     class Meta:
        model= Post
        fields = ('image','caption')
      #   lables= {"image":" "}
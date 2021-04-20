from django import forms
from ads.models import Ad


class CreateForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'price', 'text', 'picture']  # Picture is manual


#from django.core.exceptions import ValidationError
#from django.core import validators

# strip means to remove whitespace from the beginning and the end before storing the column
class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)

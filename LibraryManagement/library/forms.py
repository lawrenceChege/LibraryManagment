from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Author

        # specify fields to be used
        fields = [
            "title",
            "full_name",
        ]

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_title = forms.CharField(label="Your title", max_length=25)
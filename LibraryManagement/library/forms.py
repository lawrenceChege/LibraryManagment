from datetime import timezone
from django import forms

from .models import AgeGroup, Book, Category, Member, Publisher, Author
from django.contrib.auth.models import User


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

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'age_group', 'isbn', 'quantity', 'available', 
                  'publisher', 'publishing_date',]

   
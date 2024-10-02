from datetime import timezone
from django import forms

from .models import AgeGroup, Book, Category, Member, Publisher, Author, Transaction
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

        
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'library_id', 'user', 'outstanding_debt', ]


class IssueForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'book', 'member', 'return_date', 'rent_fee', ]


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'book', 'member', 'rent_fee', ]
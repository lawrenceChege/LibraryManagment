from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    full_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.full_name}'
    
class Publisher(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Category(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'
    
class AgeGroup(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    min_age = models.IntegerField()
    max_age = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.min_age} to {self.max_age}'

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)    
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True)
    quantity= models.PositiveIntegerField(default=0)
    available= models.PositiveIntegerField(default=0)
    publisher= models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publishing_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    created_on = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="modifier")
    modified_on = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.title} by {self.author.full_name}'

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    library_id = models.CharField(max_length=12, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outstanding_debt = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE) 
    return_date = models.DateTimeField(blank=True, null=True)
    rent_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issuer")    
    issue_date = models.DateTimeField(default=timezone.now)   
    received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", blank=True, null=True)    
    date_returned = models.DateTimeField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.book.title} issued to {self.member.first_name}{self.member.last_name} on {self.issue_date} '
    
from django.contrib import admin

from .models import AgeGroup, Author, Book, Category, Member, Publisher, Transaction

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ('-full_name',)
    list_display=('title', 'full_name')
    search_fields =('full_name',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    ordering = ('-name',)
    list_display=('name', 'website', 'address')
    search_fields =('name', 'website')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('-name',)
    list_display=('name',)
    search_fields =('name',)

@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    ordering = ('-name',)
    list_display=('name', 'min_age', 'max_age')
    search_fields =('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ('-title',)
    list_display=('isbn', 'title', 'author', 'category', 'age_group', 'publisher','quantity', 'available')
    search_fields =('isbn', 'title',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    ordering = ('-first_name',)
    list_display=('library_id','first_name', 'last_name', 'user', 'outstanding_debt')
    search_fields =('library_id','first_name', 'last_name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    ordering = ('-issue_date',)
    list_display=('transaction_id','member', 'book', 'rent_fee','issue_date','return_date', 'is_returned')
    search_fields =('transaction_id',)
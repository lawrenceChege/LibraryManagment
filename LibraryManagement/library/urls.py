
from django.urls import path

from library.views import author_detail, book_detail, create_author, create_book, create_member, delete_author, delete_book, delete_member, issue_book, list_authors, list_books, list_members, member_detail, return_book, search_books, transactions, update_author, update_book, update_member


urlpatterns = [
    path(r"authors/", list_authors, name='list_authors'),
    path(r"authors/<int:id>/", author_detail, name='author_detail'),
    path(r"authors/create/", create_author, name='create_author'),
    path(r"authors/update/<int:id>", update_author, name='update_author'),    
    path(r"authors/delete/<int:id>", delete_author, name='delete_author'),
    path(r"books/", list_books, name='list_books'),
    path(r"books/<int:id>/", book_detail, name='book_detail'),
    path(r"books/create/", create_book, name='create_book'),
    path(r"books/update/<int:id>", update_book, name='update_book'),    
    path(r"books/delete/<int:id>", delete_book, name='delete_book'),
    path(r"members/", list_members, name='list_members'),
    path(r"members/<int:id>/", member_detail, name='member_detail'),
    path(r"members/create/", create_member, name='create_member'),
    path(r"members/update/<int:id>", update_member, name='update_member'),    
    path(r"members/delete/<int:id>", delete_member, name='delete_member'),
    path(r"transactions/", transactions, name='transactions'),
    path(r'issue/<int:book_id>/', issue_book, name='issue_book'),
    path(r'return/<int:transaction_id>/', return_book, name='return_book'),
    path(r'search/', search_books, name='search_books'),
]
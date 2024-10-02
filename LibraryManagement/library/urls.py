

# urlpatterns = [
#     path(),
#     # path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
#     # path('members/', views.member_list, name='member_list'),
#     # path('members/<int:member_id>/', views.member_detail, name='member_detail'),
#     # path('issue/<int:book_id>/<int:member_id>/', views.issue_book, name='issue_book'),
#     # path('return/<int:transaction_id>/', views.return_book, name='return_book'),
#     # path('search/', views.search_books, name='search_books'),
# ]

from django.urls import path

from library.views import author_detail, book_detail, create_author, create_book, create_member, delete_author, delete_book, delete_member, list_authors, list_books, list_members, member_detail, update_author, update_book, update_member


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
]
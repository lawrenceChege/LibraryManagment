from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import AuthorForm, BookForm, IssueForm, MemberForm, ReturnForm
from .models import Author, Book, Member, Transaction
from django.db.models import Q
from django.utils import timezone

# Author CRUD

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors/list.html', {'authors': authors})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'authors/detail.html', {'author': author})

def create_author(request):
    if request.method == 'GET':
        return render( request, "authors/add_form.html", {"form": AuthorForm})
    elif request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('list_authors')

def update_author(request, id):
    
    author = get_object_or_404(Author, id=id)
    if request.method == 'GET':
        return render( 
            request, "authors/edit_form.html", {"form": AuthorForm({'id': id, 'title': author.title, 'full_name':author.full_name})})
    elif request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            # Author.objects.filter(pk=id).update(title=author.title, full_name=author.full_name)
            return redirect('author_detail', author.id )

def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('list_authors')
    return render(request, 'authors/confirm_delete.html', {'author': author})
        
# book CRUD

def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail.html', {'book': book})

def create_book(request):
    if request.method == 'GET':
        return render( request, "books/add_form.html", {"form": BookForm})
    elif request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('list_books')

def update_book(request, id):
    
    book = get_object_or_404(Book, id=id)
    if request.method == 'GET':
            
        form = BookForm(instance=book)
        return render( 
            request, "books/edit_form.html", {"form": form})
    elif request.method == "POST":
        
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.modified_by = request.user
            instance.save()
            return redirect('book_detail', book.id )

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'books/confirm_delete.html', {'book': book})


# member CRUD

def list_members(request):
    members = Member.objects.all()
    return render(request, 'members/list.html', {'members': members})

def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'members/detail.html', {'member': member})

def create_member(request):
    if request.method == 'GET':
        return render( request, "members/add_form.html", {"form": MemberForm})
    elif request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('list_members')

def update_member(request, id):
    
    member = get_object_or_404(Member, id=id)
    if request.method == 'GET':
            
        form = MemberForm(instance=member)
        return render( 
            request, "members/edit_form.html", {"form": form})
    elif request.method == "POST":
        
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.modified_by = request.user
            instance.save()
            return redirect('member_detail', member.id )

def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('list_members')
    return render(request, 'members/confirm_delete.html', {'member': member})

def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/list.html', {'transactions': transactions})
# Issue Book
def issue_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available == 0:
        return render(request, "transactions/book_unavailable.html", {'book': book})
    
    if request.method == 'GET':
        return render( request, "transactions/add_form.html", {"form": IssueForm})
    elif request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():        
            instance = form.save(commit=False)
            
            if instance.member.outstanding_debt + instance.rent_fee <= 500:
                instance.issued_by = request.user
                instance.save()
                return redirect('list_transactions')
            return render(request, "transactions/member_unqualified.html", {"member": instance.member})


# Return Book and Charge Rent Fee
def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
    if request.method == 'GET':
            
        form = ReturnForm(instance=transaction)
        return render( 
            request, "members/edit_form.html", {"form": form})
    elif request.method == "POST":
        
        form = ReturnForm(request.POST, instance=transaction)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.received_by = request.user
            instance.member.outstanding_debt += instance.rent_fee
            instance.save()
            return redirect('transactions', )

        return render(request, "transactions/detail.html", {"transaction": transaction})

# Search Book
def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'books/book_list.html', {'books': books})

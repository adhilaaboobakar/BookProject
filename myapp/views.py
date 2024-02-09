from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.models import Book

from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    language = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    pages = forms.IntegerField()

class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        return render(request,"book_list.html",{"data":qs})
    
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        # pk=1
        # id=1
        # print(kwargs)
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id).delete()
        return redirect("book-list")
    
class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookForm()
        return render(request,"book_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Book.objects.create(**data)
            return redirect("book-list")
        else:
            return render(request,"book_add.html",{"form":form})
        
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Book.objects.get(id=id)
        data={
            "name":movie_object.name,
            "author":movie_object.author,
            "language":movie_object.language,
            "genre":movie_object.genre,
            "pages":movie_object.pages

        }
        form=BookForm(initial=data)
        return render(request,"book_update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Book.objects.filter(id=id).update(**data)
            return redirect("book-list")
        else:
            return render(request,"book_update.html",{"form":form})
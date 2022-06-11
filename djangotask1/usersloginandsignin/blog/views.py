from turtle import update
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your views here.
# def home(request):
#     return render(request,'blog.html',{})

class HomeView(LoginRequiredMixin,generic.ListView):
    model=models.Post
    template_name='blog.html'
    ordering=['-created_at','category']
    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

class DraftView(LoginRequiredMixin,generic.ListView):
    model=models.Post
    template_name='post_draft.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        context=super(DraftView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

class UpdatePost(LoginRequiredMixin,generic.UpdateView):
    model=models.Post
    template_name='update_post.html'
    fields='__all__'
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        id=obj.id
        return redirect(reverse('home'))
    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        context=super(UpdatePost,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context
class PostDetailView(LoginRequiredMixin,generic.DetailView):
    model=models.Post
    template_name='post_details.html'
    def get_context_data(self,*args,**kwargs):
        userid=self.request.user
        posts=models.Post.objects.all().filter(user=userid)
        cat_menu=models.Category.objects.all()
        context=super(PostDetailView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        context['object_list']=posts
        return context


class AddPostView(LoginRequiredMixin,generic.CreateView):
    form_class=forms.PostForm
    model=models.Post
    template_name='add_post.html'
    def get_form_kwargs(self):
        form = super().get_form_kwargs()
        form['user'] = self.request.user
        return form
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        id=obj.id
        return redirect(reverse('home'))
    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        context=super(AddPostView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context
class DeletePostView(LoginRequiredMixin,generic.DeleteView):
    model=models.Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        context=super(DeletePostView,self).get_context_data(*args,**kwargs)
        context['cat_menu']=cat_menu
        return context

def CategoryView(request,cats):
    cat_menu=models.Category.objects.all()
    cat=models.Category.objects.filter(slug=cats).first()
    category_posts=models.Post.objects.filter(category=cat)
    return render(request,"categories.html",{'cats':cat.name.title(),'category_posts':category_posts,'cat_menu':cat_menu})

def User_posts(request):
    cat_menu=models.Category.objects.all()
    userid=request.user
    posts=models.Post.objects.all().filter(user=userid)
    return render(request,"myposts.html",{'cat_menu':cat_menu,'object_list':posts})

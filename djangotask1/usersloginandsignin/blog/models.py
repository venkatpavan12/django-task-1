from django.db import models
import misaka
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
User=get_user_model()
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=25,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,editable=False)
    title=models.CharField(max_length=50,unique=True)
    image=models.ImageField(upload_to='posts',null=True)
    summary=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now=True)
    draft=models.BooleanField(default=False)
    content=models.TextField()
    content_html=models.TextField(editable=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.content_html=misaka.html(self.content)
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('post-detail',args=(str(self.id)))
    class Meta:
        ordering=['-created_at']
        unique_together=['user','title']


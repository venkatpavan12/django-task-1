from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PostForm, self).__init__(*args, **kwargs)
    class Meta:
        model=Post
        fields='__all__'
        image=forms.ImageField()
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'summary':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control py-2'}),
            'draft':forms.CheckboxInput(),
        }
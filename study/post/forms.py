from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #작성하려고 했을 때 새 폼을 주는 것
    class Meta:
        model=Post
        fields=['title','content']
        
        # widgets = {'title': forms.TextInput(attrs={'class':'form',
        #                                            'placeholder':'제목을 입력하세요'}),
        #            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요'})
        #            }

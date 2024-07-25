from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
        #외래키로 연결했으니 필드에 추가해도 되는 거고,
        #자동으로 저장되는 애들은 절대로 추가하면 안 됨.
        
        # widgets = {'title': forms.TextInput(attrs={'class':'form',
        #                                            'placeholder':'제목을 입력하세요'}),
        #            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요'})
        #            }

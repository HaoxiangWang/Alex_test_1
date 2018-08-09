from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # 指定数据库模型
        model = Comment
        fields = ['name', 'email', 'url', 'text']

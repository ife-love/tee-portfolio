from django import forms
from django.contrib.auth.models import User
from .models import Category, Post, Comment, UserProfileInfo


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        widgets = {
            'username':forms.TextInput({'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'email':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control editable medium-editor-textarea'}),
            
        }


class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

        widgets = {
            'portfolio_site':forms.TextInput({'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
        }


class CategoryForm(forms.ModelForm):
     class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass form-control'}),
        }


class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'category', 'tags', 'image')

        widgets = {
            'author':forms.TextInput(attrs={'value':'', 'id':'elder', 'type':'hidden'}),
            # 'tags':forms.ModelMultipleChoiceField(attrs={'class':'form-control' }),
            # 'category':forms.Select(attrs={'class', 'textinputclass form-control'}),
            'title':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'title-tag':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea'}),
        }


class UpdatePostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'category', 'image')

        widgets = {
            'author':forms.TextInput(attrs={'value':'', 'id':'elder', 'type':'hidden'}),
            'title':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'title-tag':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('user', 'text')

        # widgets = {
        #     'user':forms.TextInput(attrs={'class':'textinputclass form-control'}),
        #     'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control'}),
        # }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Signup_App.models import Registration, CategoryModel, BlogModel, User_details_Model


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-group col-md-6', 'placeholder': 'Name'}), required=True,
        max_length=50)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Father's name"}),
        required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'id': 'inputPassword6', 'placeholder': "Mother's name"}),
        required=True, max_length=50)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email'}), required=True,
        max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class User_detail_modelForm(forms.ModelForm):
    class Meta:
        model = User_details_Model
        fields = '__all__'


class BlogForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Father's name"}),
        required=True, max_length=50)



    class Meta:
        model = BlogModel
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'

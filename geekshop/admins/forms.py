from django import forms

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import ProductCategory, Product

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'





class AdminsCategoryElementForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

class CategoryUpdateFormAdmin(forms.ModelForm):
    class Meta:
        model = ProductCategory
        # exclude =()
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryUpdateFormAdmin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'




class AdminsProductElementForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Product
        fields = ('name','description','image','price','quantity','category')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

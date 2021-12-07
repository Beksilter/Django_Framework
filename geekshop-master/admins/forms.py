from django import forms;
from users.forms import UserRegistrationForm, UserProfileForm
from users.models import Users
from products.models import ProductsCategory, Products

class AdminsUserCreationForm(UserRegistrationForm):
    # все стили уже определены в предке, кроме 
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    
    class Meta:
        model = Users
        fields = (
            'username', 
            'email', 
            'image',
            'first_name', 
            'last_name', 
            'password1', 
            'password2', 
            )
        
class AdminsUserUpdateForm(UserProfileForm):
    # класс Meta переопределять не нужно - определен в профиле, который родитель
    # но нужно переопределить доступные только для чтения поля:
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email    = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))

# для категорий достаточно одной формы...
class AdminsCategoryElementForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')

# для товаров тоже достаточно одной формы.
class AdminsProductElementForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    # description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    # price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'})
    # quantity = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'})
    # # category = 
    class Meta:
        model = Products
        fields = ('name','description','image','price','quantity','category')

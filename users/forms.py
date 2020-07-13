from django import forms
# from django.contrib.auth.forms import UserCreationForm
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    # clean_ function receives what user sent, checks if it is in the database, and chooses what to return from that
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     try:
    #         models.User.objects.get(username=email)
    #         return email
    #     except models.User.DoesNotExist:
    #         raise forms.ValidationError("User does not exist")

    # def clean_password(self):
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #     try:
    #         user = models.User.objects.get(username=email)
    #         if user.check_password(password):
    #             return password
    #         else:
    #             raise forms.ValidationError("Password is wrong")
    #         return email
    #     except models.User.DoesNotExist:
    #         raise forms.ValidationError("User does not exist")

# class SignUpForm(UserCreationForm):

#     username = forms.EmailField(label="Email")
 

# when you just make form, ModelForm recognizes which model you want to make, so you don't need to define fields in model.
class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "first_name", 
            "last_name", 
            "email",
            # "birthdate"
            )
        widgets={
                'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
                'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            }

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if models.User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with the same email already exists")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    # intercepting between saving process of form 
    def save(self, *args, **kwargs):
        # when commit=False, it is going to create a django object, but not put that into the database
        user = super().save(commit=False)

        # the code below saves email as username
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email

        user.set_password(password)
        user.save()

# class SignUpForm(forms.Form):
#     first_name = forms.CharField(max_length=80)
#     last_name = forms.CharField(max_length=80)

#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         try:
#             models.User.objects.get(email=email)
#             raise forms.ValidationError("User already exists with that email")
#         except models.User.DoesNotExist:
#             return email
    
#     def clean_password1(self):
#         password = self.cleaned_data.get("password")
#         password1 = self.cleaned_data.get("password1")
#         if password != password1:
#             raise forms.ValidationError("Password confirmation does not match")
#         else:
#             return password

#     def save(self):
#         first_name = self.cleaned_data.get("first_name")
#         last_name = self.cleaned_data.get("last_name")
#         email = self.cleaned_data.get("email")
#         password = self.cleaned_data.get("password")
#         password1 = self.cleaned_data.get("password1")

#         models.User.objects.create_user(email, email=email, password=password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
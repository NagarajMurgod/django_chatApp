from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()



class RegisterForm(UserCreationForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["email"].required = True
        
    class Meta:
        model = User
        fields= [
            "email",
            "username"
        ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)  # might raise multiple errors
        except ValidationError as e:
            # Only raise the first error
            raise ValidationError(e.messages[0])
        return password

        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # 👈 Grab request safely
        super().__init__(*args, **kwargs)
    
    def get_user(self): 
        username = self.cleaned_data.get('username')
        # password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        return user 
        
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     user = User.objects.filter(email = email)
    #     if not user.exists:
    #         raise ValidationError("Eamil address does not exist")
        
    #     return email
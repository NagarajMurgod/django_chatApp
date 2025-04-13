from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()



class RegisterForm(UserCreationForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["email"].required = True
        
    class Meta:
        model = User
        fields= [
            "email"
        ]
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('email').split('@')[0]

        if commit:
            user.save()
        
        return user
        

class LoginForm(forms.Form):
    
    email = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # 👈 Grab request safely
        super().__init__(*args, **kwargs)
    
    def get_user(self): 
        email = self.cleaned_data.get('email')
        # password = self.cleaned_data.get('password')
        user = User.objects.filter(email = email).first()
        return user 
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        user = User.objects.filter(email = email)
        if not user.exists:
            raise ValidationError("Eamil address does not exist")
        
        return email
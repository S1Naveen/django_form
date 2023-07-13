from django import forms
g=[('male','MALE'),('female','FEMALE')]
class SignUp(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    gender=forms.ChoiceField(choices=g)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
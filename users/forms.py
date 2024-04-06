from .models import User
from django import forms


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password_confirm'] = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password_confirm != password:
            raise forms.ValidationError("Passwordlar bir biriga mos emas")

        return password

    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 5 or len(username) > 30:
            raise forms.ValidationError("username 5 va 30 orasida bo'lishi lozim")

        return username


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 5 or len(username) > 30:
            raise forms.ValidationError("username 5 va 30 orasida bo'lishi lozim")

        return username


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'photo', 'phone_number')



class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        new_password = self.cleaned_data['new_password']
        confirm_password = self.cleaned_data['confirm_password']

        if new_password != confirm_password:
            raise forms.ValidationError("Passwordlar bir biriga mos emas")

        return self.cleaned_data
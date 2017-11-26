from django import forms

class NameForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': "subjectfield"}), max_length=100)
    message = forms.CharField(widget=forms.TextInput(attrs={'class': "messagefield"}), max_length=100)
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': "emailfield"}), max_length=100)
    cc_myself = forms.BooleanField(required=False)



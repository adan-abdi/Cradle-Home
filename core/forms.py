from django import forms


from .models import Comment, Suggest, Contact

# ModelForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


# ModelForm
class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest
        exclude = ('created', 'post')

        widgets = {
            'suggestion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'message', 'service')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Whats your name?"}),
            'phone': forms.TextInput(attrs={'placeholder': 'Whats your phone number?',}),
            'email': forms.TextInput(attrs={'placeholder': 'Whats your email address?',}),
            'message': forms.Textarea(attrs={"rows":5, "cols":77, 'placeholder': 'Whats your message?',}),
            'service': forms.TextInput(attrs={'placeholder': 'Whats your service do you want?',}),
        }

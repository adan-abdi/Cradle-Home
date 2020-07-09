from django import forms


from .models import Comment, Suggest, Contactme

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

class ContactmeForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = ('name', 'email','message')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email',
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                }),
        }

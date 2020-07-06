from django import forms


from .models import Comment, Newsletter, SharedPost

# Model Form
class SharedPostForm(forms.ModelForm):
        class Meta:
            model = SharedPost
            fields = ('name', 'email', 'recipientemail', 'message')

# name = forms.CharField(max_length=25)
# email = forms.EmailField()
# to = forms.EmailField()
# comments = forms.CharField(required=False, widget=forms.Textarea)


# ModelForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# ModelForm
class NewsletterList(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('name', 'email')


# # ModelForm
# class SuggestTopic(forms.Form):
#     comment = forms.CharField()




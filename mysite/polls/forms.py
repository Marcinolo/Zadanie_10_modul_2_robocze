from django import forms
from .models import Author, Quote, Tag

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags']

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.filter(user=self.user)
        self.fields['tags'].queryset = Tag.objects.all()

    def set_user(self, user):
        self.user = user

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

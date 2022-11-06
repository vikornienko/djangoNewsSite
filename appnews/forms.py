import re

from django import forms
from django.core.exceptions import ValidationError

from .models import News

class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=128,
    #                         label='News title:',
    #                         widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='News content:',
    #                           required=False,
    #                           widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    # is_published = forms.BooleanField(label='Publish:', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),
    #                                   label='News category',
    #                                   empty_label='Choice category',
    #                                   widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def custom_clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Title don't start from number")
        return title
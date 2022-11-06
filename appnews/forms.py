from django import forms

from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=128,
                            label='News title:',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='News content:',
                              required=False,
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    is_published = forms.BooleanField(label='Publish:', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='News category',
                                      empty_label='Choice category',
                                      widget=forms.Select(attrs={"class": "form-control"}))
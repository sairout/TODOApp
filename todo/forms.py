from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    #title = forms.Textarea(widget=forms.TextInput(attrs={}))

    class Meta:
        model = Todo
        fields = ["item", "complete"]

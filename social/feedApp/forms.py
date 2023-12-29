from django import forms
from .models import Message 

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title','author','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}), #form-control is the individual field class for bootstrap which will be wrapped in form-group class
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'user', 'type':'hidden'}),
            'body' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Type your message content here ... '}),
            }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}), #form-control is the individual field class for bootstrap which will be wrapped in form-group class
            'body' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Type your message content here ... '}),
            }
        


from django import forms 

class userinput(forms.Form): 
  q = forms.CharField(widget=forms.TextInput(attrs={'class': 'input #hastag'}))
  
from django import forms

class FormBibliography(forms.Form):
    main = forms.CharField(label='Bibliografia', max_length=50)
    author = forms.CharField(label='Autor', max_length=20)
    webLink = forms.URLField(label='Link')
    
class SearchBibliography(forms.Form):
    search = forms.CharField(label='Buscador')
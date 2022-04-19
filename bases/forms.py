from django import forms

class FormBibliography(forms.Form):
    main = forms.CharField(label='Bibliografia', max_length=50)
    author = forms.CharField(label='Autor', max_length=20)
    webLink = forms.URLField(label='Link')
    

class FormBlog(forms.Form):
    title = forms.CharField(label = 'Titulo', max_length=20)
    subTitle = forms.CharField(label = 'Subtitulo', max_length=20)
    body = forms.CharField(label = 'Texto')
    author = forms.CharField(label = 'Autor', max_length=20)
    date = forms.DateField(label = 'Fecha')


class FormUserInfo(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=15)
    webLink = forms.URLField()


class SearchBibliography(forms.Form):
    search = forms.CharField(label='Buscador')
from django.shortcuts import render
from .models import Bibliography
from .forms import FormBibliography, SearchBibliography

def biblography(request):
    print(request.method)
    if request.method == 'POST':
        formBiblio = FormBibliography(request.POST)
        if formBiblio.is_valid():
            data = formBiblio.cleaned_data
            addBibliography = Bibliography(main=data['main'],author=data['author'],webLink=data['webLink'])
            addBibliography.save()
            
    formBiblio = FormBibliography()
    return render(request, 'bases/bibliography.html', {'formBiblio': formBiblio})

def searchBibliography(request):
    biblio_searching = []
    data = request.GET.get('search', None)
    if data is not None:
        biblio_searching = Bibliography.objects.filter(author__icontains = data)
    
    searching = SearchBibliography()
    return render(request, 'bases/searchBibliography.html', 
                  {'searching': searching,
                    'biblio_searching': biblio_searching,
                    'data': data
                  })
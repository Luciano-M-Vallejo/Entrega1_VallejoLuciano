from django.shortcuts import render
from .models import Bibliography, Blogs, UserInfo
from .forms import FormBibliography, SearchBibliography, FormBlog, FormUserInfo

def biblography(request):
    if request.method == 'POST':
        formBiblio = FormBibliography(request.POST)
        if formBiblio.is_valid():
            data = formBiblio.cleaned_data
            addBibliography = Bibliography(main=data['main'],author=data['author'],webLink=data['webLink'])
            addBibliography.save()
            
    formBiblio = FormBibliography()
    return render(request, 'bases/bibliography.html', {'formBiblio': formBiblio})

def blogs(request):
    print(request.method)
    if request.method == 'POST':
        formBlog = FormBlog(request.POST)
        if formBlog.is_valid():
            data = formBlog.cleaned_data
            addBlog = Blogs(title=data['title'], subTitle=data['subTitle'], body=data['body'], author=data['author'], date=data['date'])
            addBlog.save()
            
    formBlog = FormBlog()
    return render(request, 'bases/blogs.html', {'formBlog': formBlog})

def userInfo(request):
    if request.method == 'POST':
        formUserInfo = FormUserInfo(request.POST)
        if formUserInfo.is_valid():
            data = formUserInfo.cleaned_data
            addUserInfo = UserInfo(name=data['name'], description=data['description'], email=data['email'], password=data['password'], webLink=data['webLink'])
            addUserInfo.save()
            
    formUserInfo = FormUserInfo()
    return render(request, 'bases/userInfo.html', {'formUserInfo': formUserInfo})

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
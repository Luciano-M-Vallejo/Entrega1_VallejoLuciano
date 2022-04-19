from django.shortcuts import render, redirect

from index.models import Avatar
from .models import Bibliography, Blogs, UserInfo
from .forms import FormBibliography, SearchBibliography, FormBlog, FormUserInfo
from django.contrib.auth.decorators import login_required


def listBiblography(request):
    biblographyAll = Bibliography.objects.all()
    return render(
        request, "bases/bibliography.html",
        {'biblographyAll': biblographyAll}
    )

@login_required
def creatBiblography(request):
    if request.method == 'POST':
        formBiblio = FormBibliography(request.POST)
        if formBiblio.is_valid():
            data = formBiblio.cleaned_data
            addBibliography = Bibliography(
                main=data['main'],
                author=data['author'],
                webLink=data['webLink']
            )
            addBibliography.save()
            return redirect('bibliography')
            
    formBiblio = FormBibliography()
    return render(
        request, 'bases/creatBibliography.html',
        {'formBiblio': formBiblio})

@login_required
def upLoadBibliography(request, id):
    
    bibliography = Bibliography.objects.get(id=id)
    
    if request.method == 'POST':
        formBiblio = FormBibliography(request.POST)
    
        if formBiblio.is_valid():
            data = formBiblio.cleaned_data
            bibliography.main = data['main']
            bibliography.author = data['author']
            bibliography.webLink = data['webLink']
            bibliography.save()
            return redirect('listBibliography')
    
    formBiblio = FormBibliography(
        initial={
            'main': bibliography.main,
            'author': bibliography.author,
            'webLink': bibliography.webLink
        }
    )
    return render(
        request, 'bases/upLoadBibliography.html', 
        {'formBiblio': formBiblio, 'bibliography': bibliography}
    )

@login_required
def deleteBibliography(request, id):
    bibliography = Bibliography.objects.get(id=id)
    bibliography.delete()
    return redirect('listBibliography')
        
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

def blogs(request):
    blogsAll = Blogs.objects.all()
    return render(
        request, "bases/blogs.html",
        {'blogsAll': blogsAll}
    )

@login_required
def creatBlog(request):
    print(request.method)
    if request.method == 'POST':
        formBlog = FormBlog(request.POST)
        if formBlog.is_valid():
            data = formBlog.cleaned_data
            addBlog = Blogs(
                title=data['title'], 
                subTitle=data['subTitle'], 
                body=data['body'],
                author=data['author'],
                date=data['date']
            )
            addBlog.save()
            return redirect('blogs')
        
    formBlog = FormBlog()
    return render(request, 'bases/creatBlog.html', {'formBlog': formBlog})

def userInfo(request):
    if request.method == 'POST':
        formUserInfo = FormUserInfo(request.POST)
        if formUserInfo.is_valid():
            data = formUserInfo.cleaned_data
            addUserInfo = UserInfo(name=data['name'], description=data['description'], email=data['email'], password=data['password'], webLink=data['webLink'])
            addUserInfo.save()
            
    formUserInfo = FormUserInfo()
    return render(request, 'bases/userInfo.html', {'formUserInfo': formUserInfo})

@login_required
def searchAvatarUrl(user):
    return Avatar.objects.filter(user = user)[0].img.url
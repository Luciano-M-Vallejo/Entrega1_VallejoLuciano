from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html', {})

def about_me(request):
    name = 'Luciano'
    lastName = 'Vallejo'
    course = 'Django + Python'
    
    dicc_data = {
        'name': name,
        'lastName': lastName,
        'course': course
    }
    return render(request, 'index/about_me.html', dicc_data)
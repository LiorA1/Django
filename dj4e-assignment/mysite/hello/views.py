from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.




def hello(request):
    #print(request.COOKIES)

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    if num_visits > 4 :
        del(request.session['num_visits'])

    response = HttpResponse('view count=' + str(num_visits))

    response.set_cookie('dj4e_cookie', '13403518', max_age=1000)

    response.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire

    return response


def sessfun(request):
    print("Before:")
    print(request.session.__dict__)
    #print(dir(request.session))
    #print(help(request.session))

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    print("After:")
    print(request.session.__dict__)

    if num_visits > 4 :
        del(request.session['num_visits'])



    return HttpResponse('view count= ' + str(num_visits))
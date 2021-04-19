from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', 
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):
    print("request.COOKIES: ", request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    response = HttpResponse('In a view - the zap cookie value is '+ str(oldval))

    # set 'zap' cookie
    if oldval : 
        response.set_cookie('zap', int(oldval) + 1) # No expired date = until browser close
    else : 
        response.set_cookie('zap', 42) # No expired date = until browser close

    # set 'sakaicar' cookie
    response.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire

    return response

# https://www.youtube.com/watch?v=Ye8mB6VsUHw


def sessfun(request):
    print("Before:")
    print(request.session.__dict__)
    #print(dir(request.session))
    #print(help(request.session))

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 

    print("After:")
    print(request.session.__dict__)

    if num_visits > 4:
        del(request.session['num_visits'])

    return HttpResponse('view count = ' + str(num_visits))


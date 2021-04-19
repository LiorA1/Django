from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import html
from django.views.decorators.csrf import csrf_exempt
from django.views import View

# Call as dumpdata('GET', request.GET)

def dumpdata(httpMethod, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+httpMethod+' data:<br/>\n'

        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        
        retval += '</p>\n'
    return retval

def getform(request):
    response = """<p>Impossible GET guessing game...</p>
        <form>
        <p>
            <label for="guess">Input Guess</label>
            <input type="text" name="guess" size="40" id="guess"/>
        </p>
        <input type="submit"/>
        </form>"""

    response += dumpdata('GET', request.GET)
    return HttpResponse(response)


@csrf_exempt
def postform(request):
    response = """<p>Impossible POST guessing game...</p>
        <form method="POST">
        <p>
            <label for="guess">Input Guess</label>
            <input type="text" name="guess" size="40" id="guessy"/>
        </p>
        <input type="submit"/>
        </form>"""

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)


@csrf_exempt
def html4(request):
    dump = dumpdata('POST', request.POST)
    return render(request, 'getpost/html4.html', {'data' : dump })

@csrf_exempt
def html5(request):
    dump = dumpdata('POST', request.POST)
    return render(request, 'getpost/html5.html', {'data' : dump })


from django.middleware.csrf import get_token

def failform(request):
    response = """<p>CSRF Fail guessing game...</p>
        <form method="post">
        <p>
            <label for="guess">Input Guess</label>
            <input type="text" name="guess" size="40" id="guess"/>
        </p>
        <input type="hidden" name="csrfmiddlewaretoken" value="__token__"/>
        <input type="submit"/>
        </form>"""
    token = get_token(request)
    print("the csrf token is: ", token)

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)


from django.middleware.csrf import get_token

# low level use example of csrf
def csrfform(request):
    response = """<p>CSRF Success guessing game...</p>
        <form method="POST">
        <p>
            <label for="guess">Input Guess</label>
            <input type="text" name="guess" size="40" id="guess"/>
        </p>
        <input type="hidden" name="csrfmiddlewaretoken" value="__token__"/>
        <input type="submit"/>
        </form>"""

    token = get_token(request)
    response = response.replace('__token__', html.escape(token))

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)


# Call as checkguess('42')
def checkguess(guess) :
    msg = False
    if guess :
        try:
            if int(guess) < 42 :
                msg = 'Guess too low'
            elif int(guess) > 42 :
                msg = 'Guess too high'
            else:
                msg = 'Congratulations!'
        except:
            msg = 'Bad format for guess:' + html.escape(guess) 
            # we get the 'guess' fron the user hence - we escape it.

    return msg


def guess(request):
    print('guess function based view')
    guess = request.POST.get('guess')
    msg = checkguess(guess)
    return render(request, 'getpost/guess.html', {'message' : msg })


# For each HTTP METHOD - one can implement the corresponding method name.
class ClassyView(View) :
    def get(self, request):
        print('ClassView/GET')
        return render(request, 'getpost/guess.html')

    def post(self, request):
        print('ClassView/POST')
        guess = request.POST.get('guess')
        msg = checkguess(guess)

        return render(request, 'getpost/guess.html', {'message' : msg })


# FIX to POST-Refresh
# By: "POST-Redirect-GET-Refresh"
# Send a 302 and Location: header to the browser
def bounce(request):
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm')


class AwesomeView(View):

    def get(self, request):
        msg = request.session.get('msg', False)
        print("BeforeIf: ", request)
        if ( msg ) : 
            print("BeforeDel: ", request.session.items())
            del(request.session['msg']) # delete from the session (in the server-side)
            print("AfterDel: ", request.session.items())

        return render(request, 'getpost/guess.html', {'message' : msg })

    def post(self, request):
        guess = request.POST.get('guess')
        print(request)
        print(request.POST)
        msg = checkguess(guess)
        request.session['msg'] = msg # For the GET method !. store in server-side
        print(request.path) ## 'request.path' - A string representing the full path to the requested page, not including the scheme or domain.

        return redirect(request.path)  # 302


# References

# https://stackoverflow.com/questions/3289860/how-can-i-embed-django-csrf-token-straight-into-html

# https://stackoverflow.com/questions/36347512/how-can-i-get-csrftoken-in-view

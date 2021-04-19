from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BasicForm, CatForm
from form.models import Cat
import html

def example(request) :
    form = BasicForm()
    return HttpResponse(form.as_table())


# Call as dumpdata('GET', request.GET)
def dumpdata(http_method, data) :
    ''' Dump a Dictionary - prints the code '''
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+http_method+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

class DumpPostView(View):  # Reusable bit...
    def post(self, request):
        dump = dumpdata('POST', request.POST)

        ctx = {'title': 'request.POST', 'dump': dump}
        return render(request, 'form/dump.html', ctx)


class SimpleCreate(DumpPostView): 
    def get(self, request):
        form = BasicForm()

        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)


class SimpleUpdate(DumpPostView):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        # old_data can be replaced with 'request.POST'/'request.GET'
        form = BasicForm(old_data)

        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)


class Validate(DumpPostView):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(initial=old_data) # 'initial' -  # old_data is instead a DB query.

        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)


    def post(self, request):
        print("Validate:POST")
        form = BasicForm(request.POST)

        if not form.is_valid():
            # form is not valid hence - shows the in-Valid data in the re-rendered page
            ctx = {'form' : form}
            #return render(request, 'form/form.html', ctx)
            return render(request, 'form/form.html', ctx, status='412') # WORK !
            # TODO: try not to return Http200
            #! He Return 200 also if the form is not valid

        # If there are no errors, we would save the data. BUT it just an example.
        x = reverse('form:success')
        #print(x) # x = "/form/success"
        return redirect(x)

# https://stackoverflow.com/questions/54695697/django-giving-validation-error-feedback-on-a-form-after-a-post-redirect-get


def success(request) :
    return HttpResponse('Thank you!')


class CatCreate(View): 
    def get(self, request) :
        form = CatForm()
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

    def post(self, request) :
        form = CatForm(request.POST)
        if not form.is_valid() :
            # form is not valid hence - we call a GET method again
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)

        # Save the form and get a model object
        newcat = form.save()
        x = reverse('form:main') + '#' + str(newcat.id)
        return redirect(x)


class CatUpdate(View):
    def get(self, request, pk) :
        oldcat = get_object_or_404(Cat, pk=pk) # Get the old 'cat' instance with the wanted 'pk'
        form = CatForm(instance=oldcat)
        ctx = { 'form': form }
        return render(request, 'form/form.html', ctx)

    def post(self, request, pk) :
        oldcat = get_object_or_404(Cat, pk=pk)
        form = CatForm(request.POST, instance=oldcat)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)

        editcat = form.save()
        x = reverse('form:main')
        return redirect(x)

# References

# https://stackoverflow.com/questions/383944/what-is-a-python-equivalent-of-phps-var-dump

from favs.models import Thing, Fav

from django.views import View
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin

from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ThingListView(OwnerListView):
    model = Thing
    template_name = "favs/list.html"

    def get(self, request) :
        thing_list = Thing.objects.all()
        favorites = list()

        if request.user.is_authenticated:
            # get the list of their favorite things but only the id's.
            
            #rows = request.user.favorite_things.values('id') # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.fav_set.all()
            #print(rows)
            rows = request.user.fav_set.values('thing_id')
            #print(rows)
            

            # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#values-list
            print("test: ", list(rows.values_list('thing_id', flat=True)))

            # favorites = [2, 4, ...] using list comprehension:
            #favorites = [ row['id'] for row in rows ]
            favorites = [ row['thing_id'] for row in rows ]
            print("favorites: ", favorites)
            print("thing_list: ", thing_list)

        #? Why not to override get_context ?
        ctx = {'thing_list' : thing_list, 'favorites': favorites}
        return render(request, self.template_name, ctx)


class ThingDetailView(OwnerDetailView):
    model = Thing
    template_name = "favs/detail.html"


class ThingCreateView(OwnerCreateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favs/form.html"


class ThingUpdateView(OwnerUpdateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favs/form.html"


class ThingDeleteView(OwnerDeleteView):
    model = Thing
    template_name = "favs/delete.html"


# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

from django.middleware.csrf import get_token

from django.views.decorators.csrf import ensure_csrf_cookie

#@method_decorator(csrf_exempt, name='dispatch') #TODO: How to send with CSRF token
#@method_decorator(ensure_csrf_cookie, name='dispatch') #TODO: How to send with CSRF token
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Thing, id=pk)
        #fav = Fav(user=request.user, thing=t)
        fav, created = Fav.objects.get_or_create(user=request.user, thing=t) 
        #TODO: I don't think that we need here try(save)-except !
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            print("Error: ", e)
            
        return HttpResponse()





#@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK start",pk)
        t = get_object_or_404(Thing, id=pk)
        #print(t)#print(dir(t))#print(t.__dict__)
        #token = get_token(request)
        #print(token)

        try:
            fav = Fav.objects.get(user=request.user, thing=t)
            #print(fav)
            fav.delete()
            #print(fav)

        except Fav.DoesNotExist as e:
            print("Error: ", e)
        
        print("Delete PK end",pk)
        return HttpResponse()


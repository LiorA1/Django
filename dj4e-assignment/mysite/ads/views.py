from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from ads.models import Ad, Comment, Fav
from ads.advance_views import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from ads.forms import CreateForm, CommentForm
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse

from django.db.models import Q


class AdListView(OwnerListView):
    model = Ad
    #paginate_by = 3
    # By convention:
    # template_name = "ads/ad_list.html"

    def get_context_data(self, **kwargs):
        # return the origianl context with 'ad_list' and 'favorites':
        context = super().get_context_data(**kwargs)

        ### Display the Favorites -
        favs = list()
        if self.request.user.is_authenticated:
            # get the list of their favorite ads but only the id's.
            # now, we have the ad_list, add the favorites:
            favsQuerySet = self.request.user.fav_set.values('ad_id') # we will get all the current user favorites ads id's.
            favs = list(favsQuerySet.values_list('ad_id', flat=True))

        context['favorites'] = favs

        ### Search Box -
        searchTerm = self.request.GET.get("search", False)
        if searchTerm:
            # Title only Search-
            # Multi-field Search -
            searchQuery = Ad.objects.filter(Q(title__contains=searchTerm) | Q(text__contains=searchTerm)).order_by('-updated_at')

            context['ad_list'] = searchQuery #if no searchTerm - 'ad_list' will be all the ads.


        context['search'] = searchTerm


        return context


class AdDetailView(OwnerDetailView):
    model = Ad

    # https://stackoverflow.com/questions/21758731/how-can-i-get-pk-or-id-in-get-context-data-from-cbv
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        adQuery = get_object_or_404(Ad, id=pk)
        comments = Comment.objects.filter(ad=adQuery).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad': adQuery, 'comments': comments, 'comment_form': comment_form }
        return context


    '''
    def get(self, request, pk):
        # It's like Charles's "forums/views.py", but because its just a context modification I
        # Used 'get_cintext_data' instead. (see above)

        # get the current Ad Object.
        adQuery = get_object_or_404(Ad, id=pk)
        # get all the comments of it
        comments = Comment.objects.filter(ad=adQuery).order_by('-updated_at')
        # build a new comment form
        comment_form = CommentForm()
        # build context
        context = { 'ad': adQuery, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)
        '''



class AdCreateView(OwnerCreateView):
    model = Ad
    #fields = ['title','price', 'text']
    fields = ['title', 'price', 'text', 'picture']  # Picture is manual


class AdUpdateView(OwnerUpdateView):
    model = Ad
    #fields = ['title','price', 'text']
    fields = ['title', 'price', 'text', 'picture']  # Picture is manual


class AdDeleteView(OwnerDeleteView):
    model = Ad


def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        # get the current ad
        currentAd = get_object_or_404(Ad, id=pk)
        # create a new Comment Object. (request.POST['comment'] - Came from the comment_form)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=currentAd)
        # save
        comment.save()
        # return
        return redirect(reverse('ads:ad_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = 'ads/comment_delete.html'

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    # get a post HTTP request - create a new fav entry - and response 200.
    def post(self, request, pk):
        adQuery = get_object_or_404(Ad, id=pk)
        fav, created = Fav.objects.get_or_create(user=request.user, ad=adQuery)
        try:
            fav.save()
        except IntegrityError as e:
            print("Error: ", e)

        return HttpResponse()



@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    # Get a post HTTP request - delete the fav entry - and response 200 ok.
    def post(self, request, pk):
        # search for the ad with the 'pk' id, search for the entry of (request.user,ad) and remove it.
        adQuery = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad=adQuery)
            fav.delete()
        except Fav.DoesNotExist as e:
            print("Error: ", e)

        return HttpResponse()



















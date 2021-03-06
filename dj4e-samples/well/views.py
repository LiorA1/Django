from django.shortcuts import render
from well.models import Post
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime

from well.utils import dump_queries

from django.db.models import Q


# Lior - Try to do the same in the 'get_context_data' method inside 'ListView'. Charles prefered to write from 'View'.
class PostListView(View):
    template_name = "well/list.html"

    def get(self, request) :
        search_val =  request.GET.get("search", False) # get A GET(HTTP) parameter.
        if search_val :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=search_val).select_related().order_by('-updated_at')[:10]

            # Multi-field search (the search_val apper in the 'title' or in the 'text' fields)
            query = Q(title__contains=search_val)
            query.add(Q(text__contains=search_val), Q.OR)
            objects = Post.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            # try both versions with > 4 posts and watch the queries that happen
            objects = Post.objects.all().order_by('-updated_at')[:10]
            # objects = Post.objects.select_related().all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'post_list' : objects, 'search': search_val}
        retval = render(request, self.template_name, ctx)

        dump_queries()
        return retval


# References

# https://docs.djangoproject.com/en/3.0/topics/db/queries/#one-to-many-relationships

# Note that the select_related() QuerySet method recursively prepopulates the
# cache of all one-to-many relationships ahead of time.

# sql “LIKE” equivalent in django query
# https://stackoverflow.com/questions/18140838/sql-like-equivalent-in-django-query

# How do I do an OR filter in a Django query?
# https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query

# https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running

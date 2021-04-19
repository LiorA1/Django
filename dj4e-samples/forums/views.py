from forums.models import Forum, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from forums.forms import CommentForm
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ForumListView(OwnerListView):
    model = Forum
    template_name = "forums/list.html"



class ForumDetailView(OwnerDetailView):
    """OwnerDetailView is a regular View"""
    model = Forum
    template_name = "forums/detail.html"

    def get(self, request, pk) :
        #get the forum (title, text, owner)
        forumQuery = Forum.objects.get(id=pk) #todo: get_object_or_404
        #get all the comments that belongs to the current forum.
        comments = Comment.objects.filter(forum=forumQuery).order_by('-updated_at')
        #build a new comment
        comment_form = CommentForm()
        context = { 'forum' : forumQuery, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)



class ForumCreateView(OwnerCreateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forums/form.html"


class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ['title', 'text']
    template_name = "forums/form.html"


class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = "forums/delete.html"


class CommentCreateView(LoginRequiredMixin, View):
    # pk is the key of the Forum !
    def post(self, request, pk) :
        #get the current forum
        f = get_object_or_404(Forum, id=pk)
        #create a new comment
        comment = Comment(text=request.POST['comment'], owner=request.user, forum=f)
        # request.POST['comment'] - Came from the comment_form
        comment.save()
        # return to the forum
        return redirect(reverse('forums:forum_detail', args=[pk]))



class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "forums/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.forum # 'self.object' is the comment !
        return reverse('forums:forum_detail', args=[forum.id])



from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import JsonResponse, HttpResponse
from chat.models import Message
from datetime import datetime, timedelta
import time


class HomeView(View):
    def get(self, request):
        return render(request, 'chat/main.html')


def jsonfun(request):
    time.sleep(3)
    stuff = {
        'first': 'first thing',
        'second': 'second thing'
    }
    return JsonResponse(stuff)


class TalkMain(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'chat/talk.html')

    def post(self, request):
        message = Message(text = request.POST['message'], owner = request.user)
        message.save()
        return redirect(reverse('chat:talk'))


class TalkMessages(LoginRequiredMixin, View):
    def get(self, request):
        messages = Message.objects.all().order_by('-created_at')[:10]

        results = []
        for message in messages:
            print(message.owner.username)
            #result = [message.text, naturaltime(message.created_at), str(message.owner.username)]  # Array of Arrays

            result = {'text': message.text, 'time': naturaltime(message.created_at), 'auth': str(message.owner.username)}  # Dictionary of Arrays
            #result = [message.text, message.owner.username, naturaltime(message.created_at)]

            results.append(result)
        
        #! Charles returns here array of arrays, but comment that it is considered "tacky"
        #!  So, I've changed it to a dictionary with one element - a list of dictionaries
        #! Changed from [[], [], ...., []]  To { 'comments': [{}, {}, ..... {}, {}]}
        # results is a list of dictionaries. 
        # And now we convert it to a dictionary with one element - a list of dictionaries
        results = { 'comments': results }
        #print(dict(results))
        return JsonResponse(results, safe = True)


# References

# https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html

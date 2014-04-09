from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Poll,Choice

def index(request):
    poll_list = Poll.objects.all()
    return render_to_response('index.html', dict(poll_list=poll_list))

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render_to_response('vote.html', dict(choice=choice))

def results(request, poll_id):
    return render_to_response('results.html')

def details(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render_to_response('details.html', dict(poll=poll))

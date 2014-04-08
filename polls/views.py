from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Poll,Choice

def index(request):
    poll_list = Poll.objects.all()
    return render_to_response('index.html', dict(poll_list=poll_list))

def vote(request, poll_id):
    return render_to_response('vote.html')

def results(request, poll_id):
    return render_to_response('results.html')

def details(request, poll_id):
    polls = Poll.objects.filter(pk=poll_id)
    choices = Choice.objects.filter(poll_id=poll_id)
    return render_to_response('details.html', dict(choices=choices))

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from models import Poll,Choice


def index(request):
    poll_list = Poll.objects.all()
    return render_to_response('index.html', dict(poll_list=poll_list))

def vote(request, poll_id, choice_id):
    choice = Choice.objects.get(pk=choice_id)
    choice.votes += 1
    choice.save()
    return redirect(results,poll_id=poll_id)

def delete(request, poll_id, choice_id):
    choice = Choice.objects.get(pk=choice_id)
    choice.delete()
    return redirect(results,poll_id=poll_id)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render_to_response('results.html', dict(poll=poll))

def details(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render_to_response('details.html', dict(poll=poll))

def add(request):
    if request.POST:
        poll = Poll(question=request.POST.get('question'))
        poll.save()
        for ch in request.POST.getlist('choice'):
            choice = Choice(poll=poll, choice=ch)
            choice.save()
        poll_list = Poll.objects.all()
        return render_to_response('index.html',dict(poll_list=poll_list, msg_success='Successfully submitted poll and choices'))
    else:
        return render(request,'add.html',{})


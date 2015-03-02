from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from sweep.models import Sweep, Player, Backer

# Create your views here.

def SweepAll(request):
	sweeps = Sweep.objects.all()
	context = {'sweeps': sweeps}
	return render_to_response('sweepall.html', context, context_instance=RequestContext(request))

def SweepDetail(request, sweepslug):
	sweep = Sweep.objects.get(slug=sweepslug)
	sweepplayers = Player.objects.filter(playersweep = sweep.id)
	context = {'sweep': sweep, 'sweepplayers': sweepplayers}
	return render_to_response('singlesweep.html', context, context_instance=RequestContext(request))

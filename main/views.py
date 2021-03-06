from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
# from django.http import HttpResponse
from main.models import State, City
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

#this is a comment

#forms
from main.forms import CitySearchForm, CreateCityForm, CityEditForm

@login_required
def city_delete(request, pk):
	
	City.objects.get(pk=pk).delete()

	return redirect('/city_search/')

@login_required
def city_edit(request, pk):

	print 'REQUEST TYPE -- %s' % request.method

	request_context = RequestContext(request)
	context = {}

	city = City.objects.get(pk=pk)

	context['city'] = city

	form = CityEditForm(request.POST or None, instance=city)

	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/city_search/')

	return render_to_response('city_edit.html', context, context_instance=request_context)



# Create your views here.
@login_required
def city_create(request):
	request_context = RequestContext(request)
	context = {}

	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			return render_to_response('city_create.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors 
			return render_to_response('city_create.html', context, context_instance=request_context)

	else:
		form = CreateCityForm()
		context['form'] = form

		return render_to_response('city_create.html', context, context_instance=request_context)


def city_search(request):
	request_context = RequestContext(request)

	context = {}

	if request.method == 'POST':
		form = CitySearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state = form.cleaned_data['state']

			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

			return render_to_response('city_search.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors

			return render_to_response('city_search.html', context, context_instance=request_context)


	else:
		form = CitySearchForm()
		context['form'] = form

		return render_to_response('city_search.html', context, context_instance=request_context)


def state_list(request):
	context = {}
	states = State.objects.all()
	context['states'] = states
	return render(request, 'state_list.html', context)

class StateListView(ListView):
	model = State
	template_name = 'state_list.html'
	context_object_name = 'states'

def state_detail(request, pk):
	context = {}
	state = State.objects.get(pk=pk)
	context['state'] = state
	return render(request, 'state_detail.html', context)

class StateDetailView(DetailView):
	model = State
	template_name = "state_detail.html"
	context_object_name = "state"


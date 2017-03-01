from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


def index(request):
    return render_to_response("index.html", context_instance = RequestContext(request))

def register(request):
    return render_to_response("register.html", context_instance = RequestContext(request))

def contact(request):
    return render_to_response("contact-us.html", context_instance = RequestContext(request))

def about(request):
    return render_to_response("about-us.html", context_instance=RequestContext(request))

# Create your views here.

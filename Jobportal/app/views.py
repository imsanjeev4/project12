from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from app.models import Register, Document
import hashlib
def index(request):
    return render_to_response("index.html", context_instance = RequestContext(request))

def register(request):
	if request.method == "POST":
		fname = request.POST['fullname']
		uname = request.POST['username']
		pword = request.POST['password']
		#password = hashlib.md5(pword).hexdigest()
		#print(password)
		eid = request.POST['emailid']
		checkuser = Register.objects.filter(emailid = eid).exists()
		print(checkuser)
		if checkuser == False:
			registersers = Register(
				fullname= fname,
				username = uname,
				#password = md5_crypt.encrypt(pword),
				#password = hashlib.md5(pword),
				#password = hashlib.new(pword).hexdigest(),
				password = pword,
				emailid = eid
			)
			registersers.save()
			return render_to_response("register.html", {'mess': 'Registration successfully','status':'True'}, context_instance = RequestContext(request))
		else:
			return render_to_response("register.html", {'mess': 'Email id already in use.Please check another emailid','status':'False'}, context_instance = RequestContext(request))
		
	else:
		return render_to_response("register.html", context_instance = RequestContext(request))

def login(request):
	if request.method == 'POST':
		check_count = Register.objects.count()
		print('COunt', check_count)
		if check_count > 0:
			username = request.POST['username']
			print('USERNAMERA',username)
			password = request.POST['password']
			print('PASSWORD',password)
			checkuser = Register.objects.filter(emailid = username).exists()
			if checkuser == True:
				checkuser = Register.objects.get(emailid = username)
				if  username == checkuser.emailid.strip() and password == checkuser.password:
					request.session['usersname'] = username
					return render_to_response("edit-profile.html", {'mess': 'login successfully'}, context_instance=RequestContext(request))
				else:
					return render_to_response("login.html", {'mess': 'Invalid Userid or Password'},context_instance=RequestContext(request))
			else:
				return render_to_response("login.html", {'mess': 'Invalid Username'},context_instance=RequestContext(request))
		else:
			return render_to_response("register.html", {'mess': 'First Registeruser'},context_instance=RequestContext(request))
			
	return render_to_response("login.html", context_instance = RequestContext(request))

def contact(request):
    return render_to_response("contact-us.html", context_instance = RequestContext(request))

def about(request):
    return render_to_response("about-us.html", context_instance=RequestContext(request))

def listview(request):

    return render_to_response("candidate-listing.html", context_instance=RequestContext(request))

def profile(request):
    return render_to_response("edit-profile.html", context_instance = RequestContext(request))
	
# Create your views here.

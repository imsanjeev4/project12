from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from app.models import Register, CandidateInfo
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
	if request.method == 'POST':
		username = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		website = request.POST['website']
		address = request.POST['address']
		designation = request.POST['designation']
		experience = request.POST['experience']
		age = request.POST['age']
		current = request.POST['current']
		demand = request.POST['demand']
		edulevel = request.POST['edulevel']
		uploadcv = request.FILES['uploadcv']
		fs = FileSystemStorage()
		filename_cv = fs.save(uploadcv.name, uploadcv)
		#uploaded_file_url = fs.url(filename)
		aboutme = request.POST['aboutme']
		skill = request.POST['skill']
		skilllevel = request.POST['skilllevel']
		degreename = request.POST['degreename']
		degreedate = request.POST['degreedate']
		aboutdeg = request.POST['aboutdeg']
		company = request.POST['company']
		webcom = request.POST['webcom']
		join_frm = request.POST['join_frm']
		endon = request.POST['endon']
		location = request.POST['location']
		about_company = request.POST['about_company']
		projname = request.POST['projname']
		startfrm = request.POST['startfrm']
		projendon = request.POST['endon2']
		projdesc = request.POST['projdesc']
		project_file = request.FILES['project_file']
		projectfs = FileSystemStorage()
		filename = projectfs.save(project_file.name, project_file)
		#uploaded_file_url = fs.url(filename)
		fb = request.POST['fb']
		twitter = request.POST['twitter']
		gplus = request.POST['gplus']
		linkedin = request.POST['linkedin']
		pinterest = request.POST['pinterest']
		behance = request.POST['behance']
		print(username,email,phone,website,address,designation,experience,age,current,demand,edulevel,uploadcv,project_file)
		profileInfo = CandidateInfo(
			username=username,
			email=email,
			phone=phone,
			website=website,
			address=address,
			designation=designation,
			experience=experience,
			age=age,
			current_salary=current,
			expected_salary=demand,
			edulevel=edulevel,
			uploadcv=uploadcv,
			aboutme=aboutme,
			skill_name=skill,
			skill_level=skilllevel,
			degree_name=degreename,
			degree_date=degreedate,
			about_degree=aboutdeg,
			company=company,
			company_website=webcom,
			join_from=join_frm,
			endon=endon,
			location=location,
			about_company=about_company,
			project_name=projname,
			project_start=startfrm,
			project_end=projendon,
			project_desc=projdesc,
			project_file=project_file,
			facebook=fb,
			twitter=twitter,
			google_plus=gplus,
			linkedin=linkedin,
			pinterest=pinterest,
			behance=behance		
		)
		profileInfo.save()
		return render_to_response("edit-profile.html", context_instance = RequestContext(request))
	else:
		return render_to_response("edit-profile.html", context_instance = RequestContext(request))
	
# Create your views here.

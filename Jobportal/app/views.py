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
		if checkuser == True:
			return render_to_response("register.html", {'mess': 'Email id already in use.Please check another emailid',
														'status': 'True'}, context_instance=RequestContext(request))
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
			return render_to_response("login.html", {'mess': 'Registration successfully','status':'False'}, context_instance = RequestContext(request))

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
					request.session['sessionuser'] = username
					return render_to_response("edit-profile.html", {'mess': 'login successfully','status':'True'}, context_instance=RequestContext(request))
				else:
					return render_to_response("login.html", {'mess': 'Invalid Userid or Password', 'status':'False'},context_instance=RequestContext(request))
			else:
				return render_to_response("login.html", {'mess': 'Invalid Username', 'status':'False'},context_instance=RequestContext(request))
		else:
			return render_to_response("register.html", {'mess': 'First Registeruser', 'status':'False'},context_instance=RequestContext(request))
			
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
		uploaded_file_url = fs.url(filename_cv)
		print('URL', uploaded_file_url )
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
		project_file_url = fs.url(filename)
		fb = request.POST['fb']
		twitter = request.POST['twitter']
		gplus = request.POST['gplus']
		linkedin = request.POST['linkedin']
		pinterest = request.POST['pinterest']
		behance = request.POST['behance']
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
		print('Session',request.session['sessionuser'])
		request.session['username'] = username
		request.session['email'] = email
		request.session['phone'] = phone
		request.session['website'] = website
		request.session['address'] = address
		request.session['designation'] = designation
		request.session['experience'] = experience
		request.session['age'] = age
		request.session['current'] = current
		request.session['demand'] = demand
		request.session['edulevel'] = edulevel
		request.session['uploaded_file_url'] = uploaded_file_url 
		request.session['aboutme'] = aboutme
		request.session['skill'] = skill
		request.session['skilllevel'] = skilllevel
		request.session['degreename'] = degreename
		request.session['degreedate'] = degreedate
		request.session['aboutdeg'] = aboutdeg
		request.session['company'] = company
		request.session['webcom'] = webcom
		request.session['join_frm'] = join_frm
		request.session['endon'] = endon
		request.session['location'] = location 
		request.session['about_company'] = about_company
		request.session['projname'] = projname
		request.session['startfrm'] = startfrm
		request.session['projendon'] = projendon
		request.session['project_file_url'] = project_file_url
		request.session['fb'] = fb
		request.session['twitter'] = twitter
		request.session['gplus'] = gplus
		request.session['linkedin'] = linkedin
		request.session['pinterest'] = pinterest
		request.session['behance'] = behance
		
		#get_data = CandidateInfo.objects.get(email=request.session['sessionuser'])
		#get_data = CandidateInfo.objects.get(email=request.session['sessionuser'])
		#print('DATA', get_data.project_desc)
		return render_to_response("edit-profile.html", {'status': 'True', 'mess':'Personal Information successfully saved !','user':username},context_instance = RequestContext(request))
	else:
		return render_to_response("edit-profile.html", context_instance = RequestContext(request))

def candidatedetail(request):
	return render_to_response("candidate-detail.html", context_instance = RequestContext(request))

def logout(request):
	if request.method == 'POST' and request.session['sessionuser'] != None:
		request.session['username'] = ''
		request.session['email'] = ''
		request.session['phone'] = ''
		request.session['website'] = ''
		request.session['address'] = ''
		request.session['designation'] = ''
		request.session['experience'] = ''
		request.session['age'] = ''
		request.session['current'] = ''
		request.session['demand'] = ''
		request.session['edulevel'] = ''
		request.session['uploaded_file_url'] = '' 
		request.session['aboutme'] = ''
		request.session['skill'] = ''
		request.session['skilllevel'] = ''
		request.session['degreename'] = ''
		request.session['degreedate'] = ''
		request.session['aboutdeg'] = ''
		request.session['company'] = ''
		request.session['webcom'] = ''
		request.session['join_frm'] = ''
		request.session['endon'] = ''
		request.session['location'] = '' 
		request.session['about_company'] = ''
		request.session['projname'] = ''
		request.session['startfrm'] = ''
		request.session['projendon'] = ''
		request.session['project_file_url'] = ''
		request.session['fb'] = ''
		request.session['twitter'] = ''
		request.session['gplus'] = ''
		request.session['linkedin'] = ''
		request.session['pinterest'] = ''
		request.session['behance'] = ''
		return render_to_response("index.html", context_instance = RequestContext(request))
	return render_to_response("index.html", context_instance = RequestContext(request))

def resetpassword(request):
	if request.method == 'POST':
		oldpassword = request.POST['oldpassword']
		getoldpasswordfromdb = Register.objects.filter(password=oldpassword)

		if oldpassword != getoldpasswordfromdb:
			return render_to_response("resetpassword.html", {'status': 'False', 'mess': 'Old password not match'}, content_type = RequestContext(request))
		newpassword = request.POST['password']
		confirmpassword = request.POST['confirmpassword']
		if confirmpassword != newpassword:
			return render_to_response("resetpassword.html", {'status':'False', 'mess':'ConfirmPassword not match with NewPassword'}, content_type = RequestContext(request))

	return render_to_response("resetpassword.html", context_instance = RequestContext(request))
#
# Create your views here.

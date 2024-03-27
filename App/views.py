from django.shortcuts import render
from App.models import adminlog,accessories,appointmentdet,dblfeed1
from django.http import HttpResponse,HttpResponseRedirect
#from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
	return render(request,'index.html',{})

def about(request):
	return render(request,'about.html',{})

def admin(request):
	return render(request,'adminlog.html',{})
def adminhome(request):
	return render(request,'adminhome.html',{})

def logincheck(request):
	if request.method == 'POST':
		uname = request.POST['uname']
		pwd = request.POST['pword']

		
		if adminlog.objects.filter(username=uname,password=pwd).exists():
			#return render(request,'newuser.html')
			request.session['users']=uname

			#return HttpResponseRedirect('Loginsuccess')
			return render(request,'admin.html')

		else:
			#return HttpResponse("Invalid Login")
			#return render(request, 'index.html', {res:"Invalid Login"})
			return render(request, 'adminlog.html')

	else:
		return render(request, 'adminlog.html')

def services(request):
	return render(request,'services.html',{})

def appointment(request):
	return render(request,'appointment.html',{})
def accessoriess(request):
	return render(request,'accessoriess.html',{})
	
def dbappointment(request):
	if request.method== "POST":
		name=request.POST['name']
		place=request.POST['place']
		email=request.POST['email']
		phone=request.POST['phone']
		
		d=appointmentdet()	
		d.name=name
		d.place=place
		d.email=email
		d.phone=phone
		d.save()
		msg="Your Appointment Recived SuccessFully"
		return render(request,'appointment.html',{"message":msg})

def viewbooking(request):
	resulteddisplay=appointmentdet.objects.all()
	return render(request,'viewbooking.html',{'result':resulteddisplay})

def appointmentend(request):
	return render(request,'appointmentend.html',{})


def ouroffers(request):
	return render(request,'ouroffers.html',{})

def barbers(request):
	return render(request,'barbers.html',{})

def contact(request):
	return render(request,'contact.html',{})

def services(request):
	return render(request,'services.html',{})

def postoffer(request):
	return render(request,'postoffer.html',{})

def postservices(request):
	return render(request,'postservices.html',{})

def postaccessories(request):
	return render(request,'postaccessories.html')

def customerfeed(request):
	return render(request,'customerfeed.html')

def storepostaccessories(request):

	if request.method=="POST":
		name=request.POST['name']
		brand=request.POST['brand']
		style=request.POST['style']
		liquid=request.POST['liquid']
		photo=request.FILES['pic']

		d=accessories()	
		d.name=name
		d.brand=brand
		d.style=style
		d.liquid=liquid
		d.photo=photo
		d.save()
		msg="record store SuccessFully"
		return render(request,'postaccessories.html',{"message":msg})

def vieworder(request):
	resulteddisplay=accessories.objects.all()
	return render(request,'vieworder.html',{'result':resulteddisplay})

def dblfeedget(request):

	if request.method=="POST":
		cname=request.POST['name']
		feed=request.POST['feed']
		rating=request.POST['rating']
		
		d=dblfeed1()	
		d.name=cname
		d.feed=feed
		d.rating=rating
		
		d.save()
		msg="your feedback submited"
		return render(request,'customerfeed.html',{"msg":msg})

def adcustomerfeed(request):
	getdata=dblfeed1.objects.all()
	return render(request,'adcustomerfeed.html',{"result":getdata})

def adminfeedbackans(request,id):
	getdata=dblfeed1.objects.get(id=id)
	return render(request,'adminfeedbackans.html',{'res':getdata})

def storefeedback(request,id):
	if request.method=="POST":
		rply=request.POST['replay']

		d=dblfeed1.objects.get(id=id)
		d.replay=rply
		d.save()
		msg="Feedback Sended To Customers"
		return render(request,'adminfeedbackans.html',{"msg":msg})
















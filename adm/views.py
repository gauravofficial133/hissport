
from django.shortcuts import render
import datetime
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection
from .models import Student , Eventlst , Pointstable
context={}
def adm(request):
	cursor = connection.cursor()
	cursor.execute("SELECT adm_student.sname ,adm_student.sclass,adm_student.ssec,adm_student.category,adm_student.house,max(adm_pointstable.points)as tpoints FROM adm_student INNER JOIN adm_pointstable ON adm_student.admno = adm_pointstable.admno GROUP BY adm_student.sname")
	context['top'] = cursor.fetchall()
	admlst  = Student.objects.values('admno')
	adm_lst = []
	for v in admlst:
		adm_lst.append(v['admno'])
	context['adm_lst'] = adm_lst
	if request.POST:
		up_gadm = request.POST['upadmno']
		context['up_adm']=up_gadm
		return redirect('/up_details/')
	user = request.user
	if user.is_authenticated:
		if user.is_superuser:
			return render(request,"admin.html",context)
		else:
			fltr = user.username
			reg_stu = Student.objects.filter(house=fltr)
			context['reg_det']=reg_stu
			return render(request,"st_house.html",context)
	else:
		return redirect('/login/')

def add_stu(request):
	selectclass=[2,3,4,5,6,7,8,9,10,11,12]
	context['selectclass']=selectclass
	eventlst = Eventlst.objects.values('eventname')
	w = []
	for x in eventlst:
		w.append(x['eventname'])
	context['eventlst'] = w

	if request.POST:
		#return HttpResponse("<script>console.log('in backend')</script>")
		sadmno  = request.POST.get('admno')
		sname   = request.POST.get('sname')
		scate   = request.POST.get('ageGroup')
		shouse  = request.POST.get('shouse')
		event1  = request.POST.get('event1')
		event2  = request.POST.get('event2')
		sclass  = request.POST.get('sclass')
		sgen    = request.POST.get('gender')
		ssec    = request.POST.get('ssec')
		if sclass in ["11","12"]:
			adddetails = Student(admno=sadmno,sname=sname,category=scate,gender=sgen,sclass=sclass,ssec=ssec,event1=event1,event2=event2).save()
		else:
			add_details = Student(admno=sadmno,sname=sname,category=scate,gender=sgen,house=shouse,sclass=sclass,ssec=ssec,event1=event1,event2=event2).save()
	user = request.user
	if user.is_authenticated:
		return render(request,"add_stu.html",context)
	else:
		return redirect('/login/')

def up_details(request):
	up_status = 0
	up_adm = context['up_adm']
	up_studetails = Student.objects.filter(admno = up_adm)
	context['predet'] = up_studetails
	if len(up_studetails) > 0:
		if request.POST:
			usadmno  = request.POST.get('admno')
			usname   = request.POST.get('sname')
			ushouse  = request.POST.get('shouse')
			uevent1  = request.POST.get('event1')
			uevent2  = request.POST.get('event2')
			usclass  = request.POST.get('sclass')
			up_studetails.update(admno=usadmno,sname=usname,house=ushouse,sclass=usclass,event1=uevent1,event2=uevent2)
			up_status = 1
		if up_status == 1:
			return redirect('/dashboard/')
	user = request.user
	if user.is_authenticated:
		return render(request,"up_details.html",context)
	else:
		return redirect('/login/')

def up_points(request):
	peventlst = Eventlst.objects.values('eventname')
	wx = []
	for x in peventlst:
		wx.append(x['eventname'])
	context['peventlst'] = wx
	if request.POST:
		padmno = request.POST['padmno']
		pgame =  request.POST['pgame']
		evgpoint = 0

		if pgame == "relay(4x100)":
			evgpoint = request.POST['relayp']
		else:
			evgpoint = request.POST['nrmlp']
		evpoint = Pointstable(admno=padmno,event=pgame,points=evgpoint).save()
	user = request.user
	if user.is_authenticated:
		if user.is_superuser:
			return render(request,"up_points.html",context)
		else:
			return redirect("dashboard")
	else:
		return redirect('/login/')

def up_event(request):
	pre_stat = Eventlst.objects.values('eventname').filter(status=False)
	pre_lst  = []
	for er in pre_stat:
		pre_lst.append(er['eventname'])
	context['prestat'] = pre_lst
	if request.POST:
		up_stat = request.POST['upevent']
		Pre_stat=Eventlst.objects.filter(eventname=up_stat).update(status=True)
	user = request.user
	if user.is_authenticated:
		if user.is_superuser:
			return render(request,"up_event.html",context)
		else:
			return redirect("dashboard")
	else:
		return redirect('/login/')
	
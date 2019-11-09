from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate, logout
from adm.models import Student , Eventlst , Pointstable
from django.db import connection
incontext = {}
def index(request):
	user = request.user
	if user.is_authenticated:
		return redirect("dashboard")
	cursor = connection.cursor()
	upc_event = Eventlst.objects.values('eventname').filter(status=False)
	upc_lst = []
	for f in upc_event:
		upc_lst.append(f['eventname'])
	incontext['upcoming'] = upc_lst[0:5]
	
	comp_event = Eventlst.objects.values('eventname').filter(status=True)
	comp_lst = []
	for e in comp_event:
		comp_lst.append(e['eventname'])
	incontext['completed'] = comp_lst[0:5]

	fgraph = cursor.execute("SELECT adm_student.house as house, SUM( CASE WHEN points IN (3,20) THEN 1 ELSE 0 END ) AS goldcount,SUM( CASE WHEN points IN (2,15) THEN 1 ELSE 0 END ) AS silvercount, SUM( CASE WHEN points IN (1,10) THEN 1 ELSE 0 END ) AS bronzecount,sum(adm_pointstable.points)as tpoints FROM adm_student INNER JOIN adm_pointstable ON adm_student.admno = adm_pointstable.admno GROUP BY adm_student.house")
	frow = cursor.fetchall()
	incontext['pt'] = frow
	return render(request,"index.html",incontext)

def login_view(request):
	user = request.user
	if user.is_authenticated:
		return redirect("dashboard")
	if request.POST:
		usr = request.POST['usr']
		psw = request.POST['pswd']
		user = authenticate(username=usr,password=psw)
		if user:
			login(request, user)
			return redirect("dashboard")
	return render(request,"login.html")

def logout_view(request):
	logout(request)
	return redirect("index")




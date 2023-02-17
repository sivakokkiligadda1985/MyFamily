from django.shortcuts import render

def fun1(request):
	return render(request,'website1/familyheads.html')

def fun2(request):
	a="Muktheswarao(Nancharaiah)"
	b="Muthamma"
	mydict={'x':a,'y':b}
	return render(request,'website1/Muktheswarao.html',mydict)


def fun3(request):
	a="Janakamaharaju"
	b="Venkateswaramma"
	c="Yogabala"
	d="Manoj kumar"

	mydict={'x':a,'y':b,'z':c,'p':d}
	return render(request,'website1/Janakamaharaju.html',mydict)


def fun4(request):
	a="Nancharaiah"
	b="Ramakumari"
	c="Aparna"
	d="Pavani"
	mydict={'x':a,'y':b,'z':c,'p':d}
	return render(request,'website1/Nancharaiah.html',mydict)


def fun5(request):
	a="Srinivasarao"
	b="Sree lalitha"
	c="Rohit"
	d="Gnaneswar"
	mydict={'x':a,'y':b,'z':c,'p':d}
	return render(request,'website1/Srinivasarao.html',mydict)


def fun6(request):
	a="Venkateswarao"
	b="Madhavi"
	c="Akash"
	d="Ganesh"
	mydict={'x':a,'y':b,'z':c,'p':d}

	return render(request,'website1/Venkateswarao.html',mydict)

def fun7(request):
	a="Venkateswarao"
	b="Padhamavathi"
	c="Siva subrhamanyam"
	d="Sravani"
	e="Chetan karthik"
	f="Krishna"
	g="Siva nageswarao"
	h="Aparna"
	i="Leksha sree"
	j="Rishi"
	mydict={'x':a,'y':b,'z':c,'p':d,'q':e,'r':f,'s':g,'t':h,'u':i,'v':j}

	return render(request,'website1/Siva brothers.html',mydict)
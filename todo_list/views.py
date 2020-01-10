from django.shortcuts import render,redirect
from .models import list
from bs4 import BeautifulSoup
import requests
import random
# Create your views here.
#from .forms import ListForm
from django.contrib import messages

def home(request):
	so=requests.get("https://www.brainyquote.com/topics/life")
	soup=BeautifulSoup(so.text,"html.parser")
	li=[]
	for i in range(20):
		li.append(i)
	r=random.choice(li)
	print(soup.find_all(class_="clearfix")[r].a.get_text())
	question=soup.find_all(class_="clearfix")[r].a.get_text()
	print()
	if request.method == "POST":
		item=request.POST['item']
		time=request.POST['time']
		forms=list(item=item,time=time)
		forms.save()
		messages.success(request,'Item is added to the list')
		all_items=list.objects.all
		return render(request,'home.html',{'all_items' : all_items,'thought':question})
	else:
		all_items=list.objects.all
		return render(request,'home.html',{'all_items' : all_items,'thought':question})
def delete(request,id):
	item = list.objects.get(pk=id)
	item.delete()
	messages.success(request,('Item has been deleted!'))
	return redirect(home)

def cross_off(request,id):
	item = list.objects.get(pk=id)
	item.completed = True
	item.save()
	return redirect(home)

def uncross(request,id):
	item = list.objects.get(pk=id)
	item.completed = False
	item.save()
	return redirect(home)

def edit(request,id):
	a=list.objects.get(pk=id)
	if request.method == "POST":
		a.item=request.POST['item']
		a.save()
		return redirect(home)
	else:
		return render(request,'edit.html', {'item' : a})

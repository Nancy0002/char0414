
from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from . import models
from .models import Char
import datetime
# Create your views here.



# Create your views here.
def index(request):
    chars = Char.objects.all()
    return render(request, 'chars/index.html', locals())


# def create(request):
#     return render(request, 'chars/create.html')

# def index(request):  #新增資料，資料不作驗證
# 	# form = PostForm()
# 	if request.method == "POST"	: #如果是以POST方式才處理
# 		Name = request.POST['Name'] #取得表單輸入資料
# 		Sex =  request.POST['Sex']
# 		Birthday =  request.POST['Birthday']
# 		Email = request.POST['Email']
# 		Phone =  request.POST['Phone']
# 		Addr =  request.POST['Addr']
#         #新增一筆記錄
# 		unit = member.objects.create(Name=Name, Sex=Sex, Birthday=Birthday, Email=Email,Phone=Phone, Addr=Addr) 
# 		unit.save()  #寫入資料庫
# 		return redirect('/index/')	
# 	# context = { 
#     #     'form':form 
#     # }    
# 	members = member.objects.all().order_by('id')
# 	return render(request, "members/index.html", locals())
# 	# return render(request, "members/index1.html", context)	

def create(request):
    if request.method == "POST" :
        username = request.POST["username"]
        title = request.POST["title"]
        content = request.POST["content"]
        publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        unit= Char.objects.create(title=title, content=content, username=username, publish=publish)
        unit.save()
        return redirect('/index/')
    chars = Char.objects.all().order_by('id')
    return render(request, "chars/create.html", locals())   

def delete(request,pk):
    chars = Char.objects.get(id=pk)
    if request.method == "POST":
        chars.delete()
        return redirect('/index/')
    context = {
        'char': Char
    }
    return render(request, 'chars/delete.html', context)



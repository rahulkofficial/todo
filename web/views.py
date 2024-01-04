import json

from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User

from web.models import Tasks,Students


def login(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        if username and password:
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)

                return HttpResponseRedirect("index")
        context={
            "error":True,
            "message":"Invalid email or password"
        }
        return HttpResponse(render(request,'login.html',context=context))
    context={
        
    }
    return HttpResponse(render(request,'login.html',context=context))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        stclass=request.POST.get('class')
        division=request.POST.get('division')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        st=Students.objects.filter(email=email).exists()
        fm=User.objects.filter(email=email)
        if st and fm:
            context={
                'error':True,
                'message':f"Student already exists with email {email}"
            }
            return HttpResponse(render(request,'signup.html',context=context))
        else:
            student=Students.objects.create(first_name=first_name,last_name=last_name,st_class=stclass,
                                        division=division,phone=phone,email=email,password=password)
            form=User.objects.create_user(username=email,password=password,email=email,first_name=first_name,last_name=last_name)
            student.save()
            form.save()
            return HttpResponseRedirect("/")      
    else:
        context={
            
        }
        return HttpResponse(render(request,'signup.html',context=context))


def index(request):
    current_user=request.user
    email=current_user.email
    studentQery=Students.objects.filter(email=email)
    student=studentQery[0]
    print(student)
    unfinished_tasks=Tasks.objects.filter(is_completed=False,is_deleted=False,student=student)
    finished_tasks=Tasks.objects.filter(is_completed=True,is_deleted=False,student=student)
    context={
        "unfinished_tasks":unfinished_tasks,
        "finished_tasks":finished_tasks,
    }
    return HttpResponse(render(request,'index.html',context=context))

def add_task(request):
    current_user=request.user
    email=current_user.email
    studentQery=Students.objects.filter(email=email)
    student=studentQery[0]
    title=request.POST.get('task')
    if title=="":
        response_data={
            'status':'error',
            'title':'You entered nothing',
            'message':'Please enter a task'
        }
    else:
        Tasks.objects.create(title=title,student=student)
        response_data={
            'status':'success',
            'title':'Success',
            'message':'You success fully add a new task'
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def delete(request,id):
    task=Tasks.objects.filter(id=id)
    if task.exists():
        task.delete()
        response_data={
            'status':'success',
            'title':'Sussess',
            'message':"You sussesfully deleted this task",
        }
    else:
        response_data={
            'status':'error',
            'title':'Error',
            'message':'The item is not any more'
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def revert(request,id):
    task=Tasks.objects.filter(id=id)
    if task.exists():
        task.update(is_completed=False)
        response_data={
            'status':'success',
            'title':'Success',
            'message':'Sussessfully reverted',
        }
    else:
        response_data={
            'status':'error',
            'title':'Error',
            'message':'The item is not any more'
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def complete(request,id):
    task=Tasks.objects.filter(id=id)
    if task.exists():
        task.update(is_completed=True)
        response_data={
            'status':'success',
            'title':'Success',
            'message':'Sussessfully marked as completed'
        }
    else:
        response_data={
            'status':'error',
            'title':'Error',
            'message':'The item is not any more'
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def edit(request,id):
    task=Tasks.objects.filter(id=id)
    title=task.values('title')[0]['title']
    print(title)
    context={
        "id":id,
        "title":title,
    }
    return HttpResponse(render(request,'update.html',context=context))


def update(request,id):
    task=Tasks.objects.filter(id=id)
    new_title=request.POST.get("task")
    if task.exists():
        task.update(title=new_title)
        response_data={
            'status':'success',
            'title':'Success',
            'message':'Sussessfully updated'
        }
    else:
        response_data={
            'status':'error',
            'title':'Error',
            'message':'The item is not any more'
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
    


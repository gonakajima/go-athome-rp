from django.shortcuts import render,redirect
from .models import Friend,Distance,Patient,PatientNeed,Service,ServiceAttr,ServicePost
from .forms import FriendForm,DistanceForm,PatientForm,PatientNeedForm,StatusForm,ServiceForm,ServiceAttrForm,ServicePostForm
from django.db.models import QuerySet
from django.core.mail import send_mail
from django.conf import settings

def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result
QuerySet.__str__ = __new_str__

def index(request):
    data = ServicePost.objects.all().values('title','date','text','name')
    params = {
        'title': 'Go At Home Header.',
        'side_txt': 'This is Side.',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

def friend(request):
    data = Friend.objects.all().values()
    params = {
        'title': 'Friend.',
        'data': data,
        'form': FriendForm(),
        }
    return render(request, 'hello/friend.html', params)

def createfriend(request):
    if(request.method=='POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Create.',
        'form': FriendForm(),
    }
    return render(request, 'hello/createfriend.html', params)

def deletefriend(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method=='POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Delete.',
        'id':num,
        'obj': friend,
    }
    return render(request, 'hello/deletefriend.html', params)

def putfriend(request):
    if(request.method=='POST'):
        obj = Distance()
        form = DistanceForm(request.POST, instance=obj)
        form.save()
    data = Distance.objects.all()
    params = {
        'title': 'Put your friend on.',
        'form': DistanceForm(),
        'data': data,
    }
    return render(request, 'hello/putfriend.html', params)

def patient(request):
    data = Patient.objects.all().values()
    params = {
        'title': 'Patient.',
        'data': data,
        'form': PatientForm(),
    }
    return render(request, 'hello/patient.html', params)

def contact(request):
    if(request.method=='POST'):
        obj = Patient()
        patient = PatientForm(request.POST, request.FILES, instance=obj)
        if patient.is_valid():
            patient.save()
        return redirect(to='confirm')
    else:
        patient = PatientForm()
    params = {
        'title': 'Contact.',
        'form': PatientForm(),
    }
    return render(request, 'hello/contact.html', params)
    
def confirm(request):
    '''confirm.htmlに達した時点でメール通知'''
    subject = '申し込み通知'
    message = 'confirm.htmlにGETしました。'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['5naka@au.com']
    send_mail(subject, message, from_email, recipient_list)
    '''メール通知部分終了'''
    params = {
        'title': '完了',
    }
    return render(request, 'hello/confirm.html', params)

def contact3(request):
    if(request.method=='POST'):
        obj = Patient()
        need = PatientNeedForm(request.POST, instance=obj)
        need.save()
        return redirect(to='confirm')
    params = {
        'title': 'Needs.',
        'form': PatientNeedForm(),
    }
    return render(request, 'hello/contact3.html', params)

def status(request):
    data = PatientNeed.objects.all().values()
    params = {
        'title': 'Status.',
        'data': data,
        'form': StatusForm(),
    }
    return render(request, 'hello/status.html', params)

def createstatus(request):
    if(request.method=='POST'):
        obj = PatientNeed()
        need = StatusForm(request.POST, instance=obj)
        need.save()
        return redirect(to='status')
    params = {
        'title': 'CreateStatus.',
        'form': StatusForm(),
    }
    return render(request, 'hello/createstatus.html', params)
    
def deletepatient(request, num):
    patient = Patient.objects.get(id=num)
    if(request.method=='POST'):
        patient.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Delete.',
        'id':num,
        'obj': patient,
    }
    return render(request, 'hello/deletepatient.html', params)

def service(request):
    data = Service.objects.all().values()
    params = {
        'title': 'Service.',
        'data': data,
        'form': ServiceForm(),
    }
    return render(request, 'hello/service.html', params)

def createservice(request):
    if(request.method=='POST'):
        obj = Service()
        service = ServiceForm(request.POST, instance=obj)
        service.save()
        return redirect(to='createservice2')
    params = {
        'title': 'Inform.',
        'form': ServiceForm(),
    }
    return render(request, 'hello/createservice.html', params)

def createservice2(request):
    if(request.method=='POST'):
        obj = ServiceAttr()
        attr = ServiceAttrForm(request.POST, instance=obj)
        attr.save()
        return redirect(to='/hello')
    params = {
        'title': 'Inform.',
        'form': ServiceAttrForm(),
    }
    return render(request, 'hello/createservice2.html', params)

def servicepost(request):
    if(request.method=='POST'):
        obj = ServicePost()
        msg = ServicePostForm(request.POST, instance=obj)
        if msg.is_valid():
            msg.save()
        else:
            print(msg.errors)
        return redirect(to='/hello')
    params = {
        'title': 'Post',
        'form': ServicePostForm(),
    }
    return render(request, 'hello/servicepost.html', params)
    


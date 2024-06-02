from msilib.schema import File
from django.shortcuts import render, HttpResponse, get_object_or_404
from home.models import Contact,Skill,Education,Project,Experince,About


# Create your views here.

def download_file(request, file_id):
    file=get_object_or_404(About,id=file_id)
    response=HttpResponse(file.cv,content_type='application/octet-stream')
    response['Content-Disposition']=f'attachement;filename=Raushan_Cv.pdf'
    return response

def home(request):
    skill=Skill.objects.all()
    r_skill=Skill.objects.count() / 2
    edu=Education.objects.all()
    proj=Project.objects.all()
    exp=Experince.objects.all()
    files=About.objects.all()
    context={ "skill":skill, "r_skill":r_skill, "edu":edu, "proj":proj,"exp":exp,"files": files}    
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')
def contact(request):
    # fetch from form
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        suggestion=request.POST['suggestion']

        print(name,email,phone,suggestion)

        ins=Contact(name=name, email=email,phone=phone, desc=suggestion)
        ins.save()

    return render(request,'contact.html') 
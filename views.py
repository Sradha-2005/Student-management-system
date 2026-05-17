from django.shortcuts import render,redirect
from anonymous.models import user_master
from faculty.models import Question,Examresult,Videos
from django.utils import timezone
from .models import profile_master
# Create your views here.
# Student Dashboard

def studentprofile(request):
    semail=request.session.get('email')
    ob=user_master.objects.get(email=semail)

    if request.method=="POST":
        address=request.POST["adds"]
        image_file=request.FILES['image']
        doc_file=request.FILES['doc']
        profile_update_obj,created=profile_master.objects.get_or_create(email=ob)
        if address:
            profile_update_obj.address=address
        if image_file:
            profile_update_obj.image=image_file
        if doc_file:
            profile_update_obj.document=doc_file
        profile_update_obj.save()

        ob.name=request.POST.get('name',ob.name)
        ob.email=request.POST.get('email',ob.email)
        ob.mobile=request.POST.get('mobile',ob.mobile)
        ob.password=request.POST.get('pwd',ob.password)
        ob.save()

    return render(request,"student_profile.html",{'sdata':ob})

def studentdashboard(request):
    username = request.session.get('username', 'Student')
    return render(request, 'studentdashboard.html', {'username': username})

def videos_display(request):
    all_videos = Videos.objects.all()
    return render(request,'teacherUpload.html',{'all_videos': all_videos}) 


# Example login view (you can adjust it to your logic)
def studentlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = user_master.objects.get(email=email, password=password, role_name='student')

            request.session['user_id'] = user.id
            request.session['username'] = user.name
            request.session['role'] = user.role_name
            request.session['email'] = user.email     # ⭐ IMPORTANT FIX

            return redirect('studentdashboard')

        except user_master.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})

    return render(request, 'login.html')

def studentexam(request):
         email=request.session.get("email")
         if request.method == "POST":
            questions = Question.objects.all()
            all_answers = {}# store selected answers as JSON
            total_score= 0 # store marks
            for q in questions:
                 key = f"q{q.slno}"# form input name
                 selected = request.POST.get(key)# user selected option
                 if selected:# convert string → int
                    selected= int(selected)
                    all_answers[str(q.slno)] = selected
                     # check correct answer
                    if (selected) == int(q.answer):
                           total_score += 1
                    else:
                        all_answers [str(q.slno)] = None # not attempted
                # Save result in DB
                 Examresult.objects.create(
                    email=email,
                     exam_date=timezone.now(),
                    answer=all_answers,
                    selected_answer=total_score
                )
               # return result to user
            return render(request, "studentresult.html", {
                 "score": total_score,
                 "total": questions.count()
          })
         else:
             ob = Question.objects.all()
             return render(request,'studentexam.html',{"studentexam":ob})

def studentvideo(request):
    return render(request,'studentvideo.html')

def studentprofile(request):
    return render(request,'studentprofile.html')

def studentresult(request):
    return render(request,'studentresult.html')

def studentlogout(request):
    return render(request,'studentlogout.html')

def studentchangepwd(request):
    return render(request,'studentchangepwd.html')

def facultylist(request):
    return render(request,'facultylist.html')


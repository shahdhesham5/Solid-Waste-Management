from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy,reverse

from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.views.generic import ListView ,DetailView #,CreateView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.contrib.auth.models import Group
from .models import *
from . import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CourseList(ListView):
    model = Course
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['students'] = Student.objects.all()
        return context


class CourseDetail(DetailView):
    model= Course


class CourseCreate(CreateView):
    model = Course
    fields=('__all__')
    success_url = reverse_lazy('course_list')


class CourseUpdate(UpdateView):
    model = Course
    fields = ('__all__')
    template_name_suffix = '_update_form'
    error_url = reverse_lazy('course_list')

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')


class StudentCreate(LoginRequiredMixin,CreateView):
    model = Student
    # fields['user']=self.request.user
    fields=('__all__')
    # form_class = UserCreationForm
    success_url = reverse_lazy('course_list')
    # def get_form_kwargs(self):
    #     kwargs = super(StudentCreate, self).get_form_kwargs()
    #     kwargs.update({fields['user']: self.request.user})
    #     return kwargs


class StudentDetail(DetailView):
    model = Student


class StudentUpdate(UpdateView):
    model = Student
    fields = ('__all__')
    template_name_suffix = '_update_form'


class Login(LoginView):
    'student Login'
    template_name = 'Learning/studentlogin.html'
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('studentDetail', kwargs={'pk': Student.objects.get(user=self.request.user.pk).pk})



def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)

        if userForm.is_valid() and  studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENTLEARNING')
            my_student_group[0].user_set.add(user)

        return HttpResponseRedirect(reverse_lazy('studentlogin'))
    return render(request,'Learning/signup.html',context=mydict)

def enroll(request,pk):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user.pk)
        course =Course.objects.get(id=pk)
        student.courses.add(course)
        context={
           'student':student.courses,
           'course':course.name
        }
        return render(request,'Learning/test.html',context)
    else:
        return HttpResponseRedirect(reverse_lazy('studentlogin'))




def unenroll(request,pk):
    student = Student.objects.get(user=request.user.pk)
    course =Course.objects.get(id=pk)
    student.courses.remove(course)
    context={
           'student':student.courses,
           'course':course.name
        }
    return render(request,'Learning/test.html',context)





def eval(request):
    x=request.POST
    y=x.keys()
    grade=0
    for key in y:
        if key== 'csrfmiddlewaretoken':
            continue
        answer=Answer.objects.get(question=key)
        if answer.correct_answer==x[key]:
            grade+=1
    percentage=grade/(len(y)-1)
    g=Grade()
    g.student=request.user.student
    g.course=answer.question.exam.course
    g.grade=percentage
    g.save()

    context={
    'gg':x,
    'rr':y,
    'grade':grade,
    'percentage':percentage



    }
    return render(request,'Learning/test.html',context)

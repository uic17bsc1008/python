from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import datetime
import random
from .values import *

def dashboard(request):
    return render(request,'base/dashboard.html')

def studentForm(request):
    courses = Course.objects.all().order_by('coursename')
    context = {"courses":courses}
    return render(request,'student/register.html',context)

def studentRegister(request):
    error = {}
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        course = request.POST.get('course')
        course_code = request.POST.get('course_code')
        if fullname == '':
            error['fullname'] = "Full Name is required."
        if phone.isnumeric():
            pass
        else:
            error['phone'] = "Please enter a valid input."
        if phone == '':
            error['phone'] = "Phone number is required."
        if address =='':
            error['address'] = "Address is required."
        if course =='':
            error['course'] = "Course is required."
        if not error:
            year = str(datetime.date.today().year)
            student = Student()
            serial = (Student.objects.last()).id
            student.fullname = fullname
            student.phone = phone
            student.email = email
            student.address = address
            student.course_id = course
            student.enroll = year[2:]+str(course_code[:3])+str(serial+1000)
            student.save()
            return JsonResponse({'success':"Student has been registered successfully."})
        else:
            return JsonResponse(error)
        
def fetch_course_code(request):
    course_id = request.POST.get('id')
    if course_id is '':
        return JsonResponse({'course_code':''})
    else:
        course = Course.objects.get(id=int(course_id))
        return JsonResponse({'course_code':course.course_code})



def showStudent(request):
    students = Student.objects.all()
    context = {"students":students}
    return render(request,'student/student.html',context)

def editStudent(request,pk):
    courses = Course.objects.all().order_by('coursename')
    batches = Batch.objects.all().order_by('name')
    page = "edit"
    student = Student.objects.get(id=pk)
    context = {"courses":courses,"page":page,"student":student,"batches":batches}
    return render(request,'student/register.html',context)
    
def updateStudent(request):
    error = {}
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        guardian = request.POST.get('guardian') 
        reference = request.POST.get('reference') 
        course = request.POST.get('course')
        batch = request.POST.get('batch')
        if fullname == '':
            error['fullname'] = "Full Name is required."
        if phone.isnumeric():
            pass
        else:
            error['phone'] = "Please enter a valid input."
        if phone == '':
            error['phone'] = "Phone number is required."
        if address =='':
            error['address'] = "Address is required."
        if guardian =='':
            error['guardian'] = "Guardian is required."
        if course =='':
            error['course'] = "Course is required."
        if not error:
            student = Student.objects.get(id=student_id)
            student.fullname = fullname
            student.phone = phone
            student.email = email
            student.address = address
            student.guardian = guardian
            student.reference = reference
            student.course_id = course
            student.batch_id = batch
            student.save()
            return JsonResponse({'success':"Student has been updated successfully."})
        else:
            return JsonResponse(error)

def deleteStudent(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student-view')

def batchForm(request):
    return render(request,'batch/register.html')

def createBatch(request):
    error = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        batch_co_ordinator = request.POST.get('batch_co_ordinator')
        timming = request.POST.get('timming')
        if name == '':
            error['name'] = "Batch Name is required."
        if batch_co_ordinator == '':
            error['batch_co_ordinator'] = "Batch co-ordinator is required."
        if timming =='':
            error['timming'] = "Time is required."
        if not error:
            batch = Batch()
            batch.name = name
            batch.batch_co_ordinator = batch_co_ordinator
            batch.timming = timming
            batch.save()
            return JsonResponse({'success':"Batch has been registered successfully."})
        else:
            return JsonResponse(error)   

def updateBatch(request):
    error = {}
    if request.method == 'POST':
        batch_id = request.POST.get('batch_id')
        name = request.POST.get('name')
        batch_co_ordinator = request.POST.get('batch_co_ordinator')
        timming = request.POST.get('timming')
        if name == '':
            error['name'] = "Batch Name is required."
        if batch_co_ordinator == '':
            error['batch_co_ordinator'] = "Batch co-ordinator is required."
        if timming =='':
            error['timming'] = "Time is required."
        if not error:
            batch = Batch.objects.get(id=batch_id)
            batch.name = name
            batch.batch_co_ordinator = batch_co_ordinator
            batch.timming = timming
            batch.save()
            return JsonResponse({'success':"Batch has been updated successfully."})
        else:
            return JsonResponse(error)

def editBatch(request,pk):
    batch = Batch.objects.get(id=pk)
    page = "edit"
    context = {"page":page,"batch":batch}
    return render(request,'batch/register.html',context)

def viewBatch(request):
    batches = Batch.objects.all()
    context = {"batches":batches}
    return render(request,'batch/batch.html',context)

def deleteBatch(request,pk):
    student = Batch.objects.get(id=pk)
    student.delete()
    return redirect('batch-view')

def courseForm(request):
    return render(request,'course/course.html')

def registerCourse(request):
    error = {}
    if request.method == 'POST':
        coursename = request.POST.get('coursename')
        duration = request.POST.get('duration')
        fees = request.POST.get('fees')
        course_code = request.POST.get('course_code')
        remark = request.POST.get('remark')

        if coursename == '':
            error['coursename'] = "Course name is required."
        if duration == '':
            error['duration'] = "Course duration is required."
        if fees.isnumeric():
            pass
        else:
            error['fees'] = "Please enter a valid input."
        if fees == '':
            error['fees'] = "Course fees is required."
        if course_code == '':
            error['course_code'] = "Course code is required."
        if not error:
            course = Course()
            course.coursename = coursename
            course.duration = duration
            course.fees = fees
            course.course_code = course_code
            course.remark = remark
            course.save()
            return JsonResponse({'success':"Course has been registered successfully."})
        else:
            return JsonResponse(error)
        
def showCourse(request):
    courses = Course.objects.all()
    context = {"courses":courses}
    return render(request,'course/course_list.html',context)

def editCourse(request,pk):
    course = Course.objects.get(id=pk)
    page = "edit"
    context = {"page":page,"course":course}
    return render(request,'course/course.html',context)

def updateCourse(request):
    error = {}
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        coursename = request.POST.get('coursename')
        duration = request.POST.get('duration')
        fees = request.POST.get('fees').strip()
        course_code = request.POST.get('course_code')
        remark = request.POST.get('remark')
        if coursename == '':
            error['coursename'] = "Course name is required."
        if duration == '':
            error['duration'] = "Course duration is required."
        if decimal_numeric(fees):
            pass
        else:
            error['fees'] = "Fees must be a decimal or numeric type."
        if fees == '':
            error['fees'] = "Course fees is required."
        if course_code == '':
            error['course_code'] = "Course code is required."
            
        if not error:
            course = Course.objects.get(id=course_id)
            course.coursename = coursename
            course.duration = duration
            course.fees = fees
            course.course_code = course_code
            course.remark = remark
            course.save()
            return JsonResponse({'success':"Course has been updated successfully."})
        else:
            return JsonResponse(error)
        
def deleteCourse(request,pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('course-view')

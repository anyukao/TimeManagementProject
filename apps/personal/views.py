from __future__ import division
from ast import Try
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import *
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
import random
from django.utils import timezone
from datetime import date
from datetime import datetime, timedelta
@login_required
def adminpage_fun(request):
    datet = date.today()
    user = request.user
    user_info = Personal_Model.objects.get (user = user,user__is_active = True)
    organization = Organization_Model.objects.get(id=user_info.organization.id)
    personal= Personal_Model.objects.filter(organization = organization, user__is_active = True)
    obj = Date_Visit_Model.objects.filter(date_create=datet)    
   
    context = {"datevisit":obj, "personal":personal}
    return render(request, "adminpage.html",context)

def userpage_fun(request):
    user=request.user
    date_create = date.today()
    data_of_user_edit_all = Date_Visit_Model.objects.filter(user=user).exclude(date_create=date_create)
    for i in data_of_user_edit_all:
                if i.date_finish == None:
                    i.status = "Не завершен"
                    i.save()  
    try:
          
        data_of_user_edit = Date_Visit_Model.objects.get(user=user,date_create=date_create)
        date_inv_set = timezone.now() - data_of_user_edit.date_invite
        hours = date_inv_set.seconds // 3600
        minutes = (date_inv_set.seconds % 3600) // 60
        seconds = date_inv_set.seconds % 60

        if data_of_user_edit.date_finish == None:
            if data_of_user_edit.summ_pause_time == None:
                formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                data_of_user_edit.summ_work_time = formatted_time
                formatted_time_pause = "00:00:00"
                data_of_user_edit.save()
            else:
                formatted_time_info_result = str(hours)+ ":" + str(minutes) + ":"+ str(seconds)
                info_time = str(data_of_user_edit.summ_pause_time)
                time1 = datetime.strptime(formatted_time_info_result, "%H:%M:%S").time()
                time2 = datetime.strptime(info_time, "%H:%M:%S").time()
                
                datetime1 = datetime.combine(datetime.today(), time1)
                datetime2 = datetime.combine(datetime.today(), time2)
                time_difference = datetime1 - datetime2
                if data_of_user_edit.status != "Перерыв":
                    formatted_time_in = (datetime.min + time_difference).time()
                    data_of_user_edit.summ_work_time = formatted_time_in
                    data_of_user_edit.save()
                formatted_time = str(data_of_user_edit.summ_work_time)
                if data_of_user_edit.status == "Перерыв":
                            date_inv_set1 = timezone.now() - data_of_user_edit.pause_time
                            hours1 = date_inv_set1.seconds // 3600
                            minutes1 = (date_inv_set1.seconds % 3600) // 60
                            seconds1 = date_inv_set1.seconds % 60
                            formatted_time_info_result1 = "{:02d}:{:02d}:{:02d}".format(hours1, minutes1, seconds1)                            
                            summ_pause = str(data_of_user_edit.summ_pause_time)                           
                            time3 = datetime.strptime(formatted_time_info_result1, "%H:%M:%S")
                            time4 = datetime.strptime(summ_pause, "%H:%M:%S")
                            time3_seconds = time3.hour * 3600 + time3.minute * 60 + time3.second
                            time4_seconds = time4.hour * 3600 + time4.minute * 60 + time4.second                           
                            total_seconds1 = time3_seconds + time4_seconds
                            hours2, remainder2 = divmod(total_seconds1, 3600)
                            minutes2, seconds2 = divmod(remainder2, 60)
                            result_time1 = datetime.strptime(f"{hours2:02d}:{minutes2:02d}:{seconds2:02d}", "%H:%M:%S").time()
                            formatted_time_pause = str(result_time1)
                else:
                        formatted_time_pause = str(data_of_user_edit.summ_pause_time)
              
        else:
             formatted_time = str(data_of_user_edit.summ_work_time)
             formatted_time_pause = str(data_of_user_edit.summ_pause_time)
        data_of_user = Date_Visit_Model.objects.get(user=user,date_create=date_create)
    except:      
        data_of_user = None
        date_inv_set = None
        formatted_time = None
        formatted_time_pause = None

    if request.method == "POST":
            button =""
            button = request.POST.get("start")
            
            if button == "Начать":
                    try:
                        obj = Date_Visit_Model.objects.get(user=user,date_create=date_create)
                        obj.date_invite = timezone.now()
                        
                        status = "Активен"
                        obj.status = status
                        obj.save()
                    except:
                        date_invite = timezone.now()
                        status = "Активен"
                        Date_Visit_Model.objects.create(user=user, date_invite = date_invite,date_create=date_create, status = status)
           
            elif button == "Завершить":
                    obj = Date_Visit_Model.objects.get(user=user,date_create=date_create)
                    try:
                            status = "Завершено"
                            obj.status = status
                            time_now = obj.pause_time
                            if time_now != None:
                                time_pause = timezone.now()
                                time_difference = time_pause - time_now
                                hours = time_difference.seconds // 3600        
                                minutes = (time_difference.seconds % 3600) // 60
                                seconds = time_difference.seconds % 60
                                formatted_time_info = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                                time1 = datetime.strptime(formatted_time_info, "%H:%M:%S")
                                time2 = datetime.strptime(obj.summ_pause_time, "%H:%M:%S")
                                time1_seconds = time1.hour * 3600 + time1.minute * 60 + time1.second
                                time2_seconds = time2.hour * 3600 + time2.minute * 60 + time2.second

                                # Сложение времени в секундах
                                total_seconds = time1_seconds + time2_seconds

                                # Преобразование общего количества секунд в объект времени
                                hours, remainder = divmod(total_seconds, 3600)
                                minutes, seconds = divmod(remainder, 60)
                                result_time = datetime.strptime(f"{hours:02d}:{minutes:02d}:{seconds:02d}", "%H:%M:%S").time()
                                obj.summ_pause_time = result_time
                                obj.pause_time = timezone.now()
                        
                            obj.date_finish = timezone.now()
                            obj.save()
                        
                        
                        
                    except:
                         obj.date_finish = timezone.now()
            elif button == "Продолжить":
                            obj = Date_Visit_Model.objects.get(user=user,date_create=date_create)
                            status = "Активен"
                            obj.status = status
                            time_now = obj.pause_time
                            time_pause = timezone.now()
                            time_difference = time_pause - time_now
                            hours = time_difference.seconds // 3600        
                            minutes = (time_difference.seconds % 3600) // 60
                            seconds = time_difference.seconds % 60
                            formatted_time_info = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                            time1 = datetime.strptime(formatted_time_info, "%H:%M:%S")
                            time2 = datetime.strptime(obj.summ_pause_time, "%H:%M:%S")
                            time1_seconds = time1.hour * 3600 + time1.minute * 60 + time1.second
                            time2_seconds = time2.hour * 3600 + time2.minute * 60 + time2.second
                            total_seconds = time1_seconds + time2_seconds
                            hours, remainder = divmod(total_seconds, 3600)
                            minutes, seconds = divmod(remainder, 60)
                            result_time = datetime.strptime(f"{hours:02d}:{minutes:02d}:{seconds:02d}", "%H:%M:%S").time()
                            obj.summ_pause_time = result_time
                            obj.pause_time = timezone.now()
                            obj.save()
            elif button == "Пауза":
                        
                        obj = Date_Visit_Model.objects.get(user=user,date_create=date_create)
                        status = "Перерыв"
                        obj.status = status
                        if obj.summ_pause_time == None:
                             obj.summ_pause_time = "00:00:00"
                        obj.pause_time =  timezone.now()
                        obj.save()
            return redirect("userpage")
    return render(request, "userpage.html", {"data_of_user_edit_all":data_of_user_edit_all,"data_of_user":data_of_user,"formatted_time":formatted_time, 
                                             "formatted_time_pause":formatted_time_pause})

def registration_fun(request):
    return render(request, "registration.html")

def forgotPassword_fun(request):
    return render(request, "forgotPassword.html")

def uchetvremeni_fun(request):
    user = request.user
    user_info = Personal_Model.objects.get (user = user, user__is_active = True)
    organization = Organization_Model.objects.get(id=user_info.organization.id)
    datevisit = Date_Visit_Model.objects.all()
    personal= Personal_Model.objects.filter(organization = organization, user__is_active = True)
    context = { "personal":personal, "datevisit":datevisit}
    return render(request, "uchetvremeni.html",context)

def udalennyesotrudniki_fun(request):
    user = request.user
    user_info = Personal_Model.objects.get (user = user)
    organization = Organization_Model.objects.get(id=user_info.organization.id)
    personal= Personal_Model.objects.filter(user__is_active = False,organization =organization )
    current_time = date.today()
    print(personal)
    for i in personal:
        userinfo = User.objects.get(id=i.user.id)
        dattaaee = current_time - i.date_deactivate
        passwor = Password_User_Model.objects.get(user=userinfo)
        print(current_time)
        print(dattaaee.days)
        if dattaaee.days >= 30:
            i.delete()
            userinfo.delete()
            passwor.delete()
    context = {'personal':personal}
    return render(request, "udalennyesotrudniki.html",context)

def addemployees_fun(request):
    button = request.POST.get("updates")
    user = request.user
    user_info = Personal_Model.objects.get (user = user)
    organization = Organization_Model.objects.get(id=user_info.organization.id)
    personal= Personal_Model.objects.filter(user__is_active = True, organization = organization)
    
    error_log = ""
    if request.method == "POST":
            if button == "Создать":
                fam = request.POST.get("last_name")
                first_name = request.POST.get("first_name")
                number_of_phone = request.POST.get("number_of_phone")
                date_of_birth = request.POST.get("date_of_birth")
                inn = request.POST.get("inn")
                try:
                    try:
                        Personal_Model.objects.get(number_of_phone=number_of_phone)
                        error_log = "Ваш номер " + number_of_phone  + "  уже зарегистрирован в системе"
                    except:
                       
                        user = User.objects.create_user(username = first_name, first_name=first_name, last_name=fam)
                        Password_User_Model.objects.create(user = user)
                        
                        Personal_Model.objects.create(user=user, number_of_phone = number_of_phone, date_of_birth = date_of_birth, inn = inn, organization = organization)
                except:
                    error_log = "Сначала введите данные!"
            elif button=="Удалить":
                setid = request.POST.get("setid")
                try:
                    info = Personal_Model.objects.get(id=setid)
                    userinfo = User.objects.get(id=info.user.id) 
                    userinfo.is_active = False
                    info.date_deactivate = date.today()
                    userinfo.save()
                    info.save()

                    error_log = "Пользователь успешно удалён!"
                except:
                    error_log = "Пользователь успешно был уже удален!"
            elif  button == "Изменить":
                setidedit = request.POST.get("setidedit")
                usereditinfo = Personal_Model.objects.get(id=setidedit)
                userinfo1 = User.objects.get(id=usereditinfo.user.id) 
                usereditinfo.number_of_phone =  request.POST.get("number_of_phone")
                date_info = request.POST.get("date_of_birth")
                if date_info != None and date_info != "":
                    usereditinfo.date_of_birth = date_info  
                usereditinfo.inn =  request.POST.get("inn")
                usereditinfo.save()
                userinfo1.last_name = request.POST.get("last_name")
                userinfo1.first_name = request.POST.get("first_name")
                userinfo1.save()
                error_log = "Вы успешно изменили данные пользователя!"
            return redirect("employees")
    context = {"personal":personal, "error_log":error_log}
    return render(request, "addemployees.html", context)

def login_fun(request):
    number_of_phone = ""
    context = {"number_of_phone": number_of_phone}
    if request.method == "POST":
        number_of_phone = request.POST.get("number_of_phone")
        if 'phone' in request.POST:
            phone = "+996" + str(request.POST.get("phone"))
    
            try:
                obj = Personal_Model.objects.get(number_of_phone=phone)
                number_of_phone = phone
                check_pass = Password_User_Model.objects.get(user=obj.user)
                if obj.user.is_active:
                    if check_pass.checks == False:
                        random_number = random.randint(1000, 9999)
                        message = "Ваш пин для авторизации tm.unet.kg: " + str(random_number) + ", Никому не сообщайте код!"
                        print(message)
                        obj.pincode = random_number
                        obj.save()
                        context.update({"number_of_phone":number_of_phone})
                        return render(request, "login.html", context) 
                    else:
                        check = "pass"
                        context.update({"number_of_phone":number_of_phone, "check":check})
                        return render(request, "login.html", context) 
                else:
                    check = "nopass"
                    error_log = "Учетная запись не активна"
                    context.update({"number_of_phone":number_of_phone, "check":check, "error_log": error_log})
                    return render(request, "login.html", context) 
            except:
                error_log = "Ваш номер " + phone  + "  не зарегистрирован в системе"
                context.update({"error_log":error_log})
                return render(request, "login.html", context)  
       

        if "auth_code" in request.POST:
            auth_codes = request.POST.getlist('auth_code')
            number_of_phone = request.POST.get("number_of_phone")
            cleaned_list = [item for item in auth_codes if item.strip()]
            auth_code = ''.join(cleaned_list)
            print(auth_code)
            obj = Personal_Model.objects.get(number_of_phone=number_of_phone)
            if obj.pincode == str(auth_code):
                    check="newpass"
                    context.update({"number_of_phone":number_of_phone, "check":check})

            else:
                    error_log = "Неправильный код подтверждения!"
                    context.update({"error_log":error_log, "number_of_phone": number_of_phone})
            

        if "password" in request.POST:
            print(number_of_phone)
            obj = Personal_Model.objects.get(number_of_phone=number_of_phone)
            password = request.POST.get("password")
            user = authenticate(username=obj.user.username, password=password)
            if user == None:
                check = "pass"
                error_log = "Неверный пароль!"
                context.update({"number_of_phone":number_of_phone, "check":check,"error_log":error_log })
            else:
               if user.is_active:
                    login(request, user)
                    if obj.is_admin == True:
                            return redirect("userpage") 
                    else:
                        return redirect("userpage")
        if "newpassword" in request.POST:
            number_of_phone = request.POST.get("number_of_phone")
            obj = Personal_Model.objects.get(number_of_phone=number_of_phone)
            user_data = User.objects.get(id=obj.user.id)
            newpassword =request.POST.get("newpassword")
            user_data.set_password(newpassword)
            user_data.save()
            per = Password_User_Model.objects.get(user=user_data) 
            per.checks = True
            per.save()
            user = user_data
            if user == None:
                check = "pass"
                error_log = "Введенный пароль не верный"
                context.update({"number_of_phone":number_of_phone, "check":check,"error_log":error_log })
            else:
                    login(request, user)
                    if obj.is_admin == True:
                            return redirect("adminpage") 
                    else:
                        return redirect("userpage")
    return render(request, "login.html", context)

def kode6zn_fun(request):
    return render(request, "kode6zn.html")

def index_fun(request):
    return render(request, "index.html")


def logout_fun(request):
    logout(request)
    return redirect("home")


def check_add_fun(request):
    if request.method == "POST":
        user=request.user
        log1 = request.POST.get("log1")
        log2 = request.POST.get("log2")
        image_info = request.POST.get("image")
        geo = log1 + ", "  + log2
        print(geo)
        date_create = date.today()
        try:
                        obj = Date_Visit_Model.objects.get(user=user,date_create=date_create)
                        obj.date_invite = timezone.now()
                        obj.image_info = image_info
                        obj.geo = geo
                        status = "Активен"
                        obj.status = status
                        obj.save()
        except:
                        date_invite = timezone.now()
                        status = "Активен"
                        Date_Visit_Model.objects.create(user=user, date_invite = date_invite,date_create=date_create, status = status, image_info=image_info, geo=geo)
        return redirect("userpage")
    return render(request, "check_add.html")
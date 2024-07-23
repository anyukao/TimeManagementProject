from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _


class Organization_Model(models.Model):

    organization_name = models.CharField( verbose_name="Наименование организации",max_length=255, null=True, blank=True )
    
    def __str__(self):
        return self.organization_name
    
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

class Personal_Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="user", null=True, blank=True )
    number_of_phone = models.CharField(verbose_name="Номер телефона",max_length=255, null=True, blank=True )
    date_of_birth = models.DateField(verbose_name="Дата рождения",null=True, blank=True)
    inn = models.CharField(verbose_name="ИНН",max_length=255, null=True, blank=True )
    date_deactivate = models.DateField(verbose_name="Дата удаления",null=True, blank=True)
    is_admin = models.BooleanField(_("Администратор"),
        default=False,
        help_text=_( "Отметье это поле, если сотрудник является администратором."),)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    organization = models.ForeignKey(Organization_Model, verbose_name="Organization", on_delete=models.SET_NULL, blank=True, null=True, related_name="organization")
    def __str__(self):
        try:
            return self.user.username
        except:
            return "deleted"
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Password_User_Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL,related_name="user1", null=True,blank=True)
    checks = models.BooleanField(_("Пароль ввел пользователь"),
        default=False,
        help_text=_( "Отметье это поле, если пользователь ввел пароль самостоятельно."),)

    def __str__(self):
        try: 
            return self.user.username
        except: 
            return "deleted"
    class Meta:
        verbose_name = "Проверка на ввод пароля пользователя"
        verbose_name_plural = "Проверка на ввод паролей"
        

class Date_Visit_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,related_name="visitdate", null=True ,blank=True)
    date_create = models.DateField(null=True,blank=True)
    date_invite = models.DateTimeField(null=True,blank=True)
    date_finish = models.DateTimeField(null=True,blank=True)
    pause_time = models.DateTimeField(null=True,blank=True)
    image_info = models.TextField(max_length=10000, null=True, blank=True)
    geo = models.CharField(max_length=255, null=True,blank=True)
    summ_pause_time = models.CharField(verbose_name="Общий перерыв",max_length=255, null=True,blank=True )
    
    summ_work_time = models.CharField(verbose_name="Общие отработанные часы",max_length=255, null=True,blank=True )
    status = models.CharField(verbose_name="Статус",max_length=255,default = "Не активен", null=True,blank=True )
    def __str__(self):
        try:
            return self.user.username
        except:
            return "deleted"
    
    class Meta:
        verbose_name = "Табель"
        verbose_name_plural = "Табели"
        ordering = ['-date_create',]

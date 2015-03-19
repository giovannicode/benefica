from django.db import models

# Create your models here.

from django import forms
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core import validators

from django.utils.translation import ugettext_lazy as _

from decimal import Decimal

class UserManager(BaseUserManager):
  def create_user(self, first_name, last_name, user_handle, email, password):

    user = self.model(
      first_name=first_name,
      last_name=last_name,
      user_handle=user_handle,
      email=email,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, first_name, last_name, password):
    user = self.model(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
   
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
  first_name = models.CharField(_('First Name'),max_length=30, blank=False)
  last_name = models.CharField(_('Last Name'), max_length=30, blank=False)
  
  user_handle = models.CharField(max_length=20, unique=False, null=True)

  email = models.EmailField(_('Email Address'), max_length=255, unique=True)
  
  #new fields - profile_pic, donation_total
  profile_pic = models.FileField(_('Profile Picture'), null=True)
  ###############
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)

  objects = UserManager()
  
  def get_full_name(self):
    return self.email
  
  
  def get_short_name():
    return self.email

  def __unicode__(self):
    return  self.email + "  id:" + str(self.id)


class UserCreatorForm(forms.ModelForm):  

  error_message = {
      'duplicate_email': "A user with that email already exists.",
      'password_mismatch': "The two password fields didn't match.",
  }

  password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
  password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ("first_name", "last_name", "email")

  def clean_username(self):
    email = self.cleaned_data["email"]
    try:
      User._default_manager.get(email=email)
    except User.DoesNotExist:
      return email
    raise forms.ValidationError(
      self.error_messages['duplicate_email'],
      code='duplicate_email',
    )

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError(
        self.error_messages['password_mismatch'],
        code='password_mismatch',
      )
    return password2

  def save(self, commit=True):
    user = super(UserCreatorForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
      user.save()
    return user

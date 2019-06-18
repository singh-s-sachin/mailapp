from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def email(request):
	send_mail( 'Ionixx Technologies', 'You are hired', 'sachinkumar.s@ionixxtech.com', ['singh.s.kshetriya@gmail.com'] )
	return('Direct to mai')

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
import json
# Create your views here.
def email(request):
	send_mail( 'Ionixx Technologies', 'You are hired', 'sachinkumar.s@ionixxtech.com', ['singh.s.kshetriya@gmail.com'] )
	return('Direct to mai')

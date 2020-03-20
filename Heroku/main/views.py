from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import UserDetail
from django.contrib import messages
from django.urls import reverse
from datetime import date
import urllib
import json
from django.conf import settings
# Create your views here.

def index(request):

	recaptcha_response = request.POST.get('g-recaptcha-response')
	url = 'https://www.google.com/recaptcha/api/siteverify'
	values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
	}
	data = urllib.parse.urlencode(values).encode()
	req =  urllib.request.Request(url, data=data)
	response = urllib.request.urlopen(req)
	result = json.loads(response.read().decode())

	if request.method=="POST":
		first_name = request.POST["first_name"]
		last_name = request.POST.get("last_name")
		email = request.POST["email"]
		password = request.POST["password"]
		confirm_password = request.POST["confirm_password"]
		ip_address = request.POST.get("ip_address")

		if password!=confirm_password:
			messages.error(request, "Password and Confirm Password should be same")
			return redirect('main:index')

		existed_user_with_email = UserDetail.objects.filter(email=email)

		if existed_user_with_email:
			messages.error(request, "User with email {} already exists".format(email))
			return redirect('main:index')


		try:
			registered_count_three = False
			date_today = date.today()
			ip_address_record = list(UserDetail.objects.filter(ip_address=ip_address, date_created=date_today))
			if len(ip_address_record)>3 and not result['success']:
				registered_count_three = True
				data={"first_name": first_name, "last_name": last_name,
				"email": email, "password": password, "confirm_password": confirm_password}
				return render(request,"index.html", {"registered_count_three":registered_count_three,
					"data": data,
					})
			
			UserDetail.objects.get_or_create(first_name=first_name, last_name=last_name,
				email=email, password=password, ip_address=ip_address, date_created=date_today)
			messages.success(request, "User with email {} registered sucessfully.".format(email))
		except Exception as e:
			raise e

	return render(request, "index.html")
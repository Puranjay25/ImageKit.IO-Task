from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import UserDetail
from django.contrib import messages
from django.urls import reverse
from datetime import date
# Create your views here.

def index(request):
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
			messages.error(request, "User with Email {} already exists".format(email))
			return redirect('main:index')


		try:
			date_today = date.today()
			ip_address_record = list(UserDetail.objects.filter(ip_address=ip_address, date_created=date_today))
			if len(ip_address_record)>3:
				print("More than 3 times")
			else:
				print("All fine")
				
			UserDetail.objects.get_or_create(first_name=first_name, last_name=last_name,
				email=email, password=password, ip_address=ip_address, date_created=date_today)
		except Exception as e:
			raise e

	return render(request, "index.html")
# ImageKit.IO


## Generate Recaptcha keys

> Go to [google recaptcha console](https://www.google.com/recaptcha/admin/create) and genrate keys for reCaptcha v2 "I am not a robot" type.
>
> Enter domain name as 127.0.0.1
>
> Assign Secret key to 'GOOGLE_RECAPTCHA_SECRET_KEY' in Task/settings.py line #
>
> Assign site key to 'data-sitekey' in main/index.html line #


## Requirements.txt:

Install the requirements using:
> pip install -r requirements.text

Run <b>python manage.py makemigrations</b> for model changes(if any).

Run <b>python manage.py migrate</b> for migrating the changes

Run <b>python manage.py runserver</b> to run the app on server.
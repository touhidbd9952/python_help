settings.py
------------------------------

INSTALLED_APPS = [
		.
		.
	   'amphibious',  //your application register
	   'App_Login',
	   'App_Blog',
	   'django_cleanup.apps.CleanupConfig',  //old image delete
	]

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
'DIRS':  [TEMPLATES_DIR,],
	
#css, js, font
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR,]
STATIC_URL  = '/static/'

#Image
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL  = '/media/'

LOGIN_URL = '/account/login/'

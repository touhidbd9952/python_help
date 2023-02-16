settings.py
------------------------------
#application
INSTALLED_APPS = [
		.
		.
	   'amphibious',
	]

#css, js, font
STATIC_URL  = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

#Image
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL  = '/media/'

LOGIN_URL = '/account/login/'

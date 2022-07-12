# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j)i+f2@n+qs+v627+7ck&ateihx8dp+01)*q*!p7kua9y@j%hy'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '11235813213455Ali.'
    }
}
django-admin startproject <projectname> -- to initiate a new django project

cd <projectname>

python manage.py startapp <appname> -- to create a new app

python manage.py runserver

Note: Add app names to settings.py in INTERNAL_APPS or create a new custom array and add it to INTERNAL_APPS

Created a ```base.html``` template as a cover code for all other html code.

Need to use {% extends "base.html %}

--------------------------------

Shell

python manage.py shell

from <appname>.models import *

<variable> = <modelname>(<input all data>)

<variable>.save()

<variable> // Write this to print the object

else

<variable> = <modelname>.objects.create(<input all data>)

// no need to do the save step

To query via shell:-

<model>.objects.all()[0].<anyproperty_name_from_the_model>

To update

Way 1: <modelname>.objects.filter(id=2).update(<propertyname> = "xyz")

Way 2: <variable> =  <modelname>.objects.get(id=)

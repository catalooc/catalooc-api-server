from django.contrib.auth.models import User
from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from django.contrib.auth.models import User
from project.apps.users.forms import *

class ShowUsersHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    @validate(ShowUsersForm, 'GET')
    def read(self, request):
        try:
            return User.objects.get(
                id          = request.form.cleaned_data['id'],
                is_active   = True
            )
        except:
            return Response.http(rc.NOT_FOUND, "")

show_users_handler      = Resource(ShowUsersHandler)
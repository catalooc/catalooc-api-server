from django.contrib.auth import authenticate, logout
from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.account.forms import *
from project.apps.account.mongo import *

class VerifyCredentialsAccountHandler(BaseHandler):
    allowed_methods = ('GET',)

    @validate(VerifyCredentialsAccountForm, 'GET')
    def read(self, request):
        cleaned     = request.form.cleaned_data
        user        = authenticate(
            username=cleaned['username'],
            password=cleaned['password']
        )
        
        if user is not None:
            if user.is_active:
                return Response.http(rc.ALL_OK, "")
            else:
                return Response.http(rc.BAD_REQUEST, "Your account has been disabled.")
        else:
            return Response.http(rc.BAD_REQUEST, "Your username or password were incorrect.")

class EndSessionAccountHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    def delete(self, request):
        logout(request)
        return Response.http(rc.DELETED, "Your session is ended.")

class UpdateProfileAccountHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(UpdateProfileAccountForm, 'PUT')
    def update(self, request):
        return Profile.managers.update(
            { 'user' : request.user.id },
            request.form.cleaned_data
        )

class UpdateProfileImageAccountHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(UpdateProfileImageAccountForm, 'PUT')
    def update(self, request):
        return Response.http(rc.ALL_OK,"")

class TotalsAccountHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Response.http(rc.ALL_OK, "")

class SettingsAccountHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT',)

    @validate(ReadSettingsAccountForm, 'PUT')    
    def read(self, request):
        return Settings.managers.filter({ 'user' : request.user.id })

    @validate(UpdateSettingsAccountForm, 'PUT')    
    def update(self, request):
        return Settings.managers.update(
            { 'user' : request.user.id },
            request.form.cleaned_data
        )

verify_credentials_account_handler      = Resource(VerifyCredentialsAccountHandler)
end_session_account_handler             = Resource(EndSessionAccountHandler)
update_profile_account_handler          = Resource(UpdateProfileAccountHandler)
update_profile_image_account_handler    = Resource(UpdateProfileImageAccountHandler)
totals_account_handler                  = Resource(TotalsAccountHandler)
settings_account_handler                = Resource(SettingsAccountHandler)
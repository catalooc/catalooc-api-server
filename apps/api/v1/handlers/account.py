from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.account.forms import *

class VerifyCredentialsAccountHandler(BaseHandler):
    allowed_methods = ('GET',)

    @validate(VerifyCredentialsAccountForm, 'GET')
    def read(self, request):
        return Response.http(rc.ALL_OK, "")

class EndSessionAccountHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    def delete(self, request):
        return Response.http(rc.DELETED,"")

class UpdateProfileAccountHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(UpdateProfileAccountForm, 'PUT')
    def update(self, request):
        return Response.http(rc.ALL_OK,"")

class UpdateProfileImageAccountHandler(BaseHandler):
    allowed_methods = ('PUT',)

    @validate(UpdateProfileImageAccountForm, 'PUT')
    def update(self, request):
        return Response.http(rc.ALL_OK,"")

class TotalsAccountHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class SettingsAccountHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT',)

    def read(self, request):
        return Response.http(rc.ALL_OK,"")

    @validate(SettingsAccountForm, 'PUT')    
    def update(self, request):
        return Response.http(rc.ALL_OK,"")

verify_credentials_account_handler      = Resource(VerifyCredentialsAccountHandler)
end_session_account_handler             = Resource(EndSessionAccountHandler)
update_profile_account_handler          = Resource(UpdateProfileAccountHandler)
update_profile_image_account_handler    = Resource(UpdateProfileImageAccountHandler)
totals_account_handler                  = Resource(TotalsAccountHandler)
settings_account_handler                = Resource(SettingsAccountHandler)
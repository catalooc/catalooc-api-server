from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.favorites.forms import *

class ListFavoritesHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Response.http(rc.ALL_OK, "")

class CreateFavoritesHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateFavoritesForm, 'POST')
    def create(self, request):
        return Response.http(rc.CREATED, "")

class DestroyFavoritesHandler(BaseHandler):
    allowed_methods = ('DELETE',)

    @validate(DestroyFavoritesForm, 'DELETE')
    def delete(self, request):
        return Response.http(rc.DELETED, "")

list_favorites_handler      = Resource(ListFavoritesHandler)
create_favorites_handler    = Resource(CreateFavoritesHandler)
destroy_favorites_handler   = Resource(DestroyFavoritesHandler)
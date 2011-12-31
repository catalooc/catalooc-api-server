from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc, validate
from project.libs.rest import Response
from project.apps.photos.forms import *

class PhotosPartOfHandler(BaseHandler):
    allowed_methods = ('GET',)

    @validate(PhotosPartOfForm, 'GET')
    def read(self, request, post_id):
        return Response.http(rc.ALL_OK,"")

class ShowPhotosHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    @validate(ShowPhotosForm, 'GET')
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class CreatePhotosHandler(BaseHandler):
    allowed_methods = ('POST',)
    
    @validate(CreatePhotosForm, 'POST')
    def create(self, request, post_id):
        return Response.http(rc.CREATED,"")

class DestroyPhotosHandler(BaseHandler):
    allowed_methods = ('DELETE',)
    
    @validate(DestroyPhotosForm, 'DELETE')
    def create(self, request):
        return Response.http(rc.DELTED,"")

photos_part_of_handler  = Resource(PhotosPartOfHandler)
show_photos_handler     = Resource(ShowPhotosHandler)
create_photos_handler   = Resource(CreatePhotosHandler)
destroy_photos_handler  = Resource(DestroyPhotosHandler)
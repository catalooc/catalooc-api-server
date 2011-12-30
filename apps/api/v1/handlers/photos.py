from piston.handler import BaseHandler
from piston.resource import Resource
from piston.utils import rc
from project.libs.rest import Response

class PhotosPartOfHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        return Response.http(rc.ALL_OK,"")

class ShowPhotosHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request):
        return Response.http(rc.ALL_OK,"")

photos_part_of_handler  = Resource(PhotosPartOfHandler)
show_photos_handler     = Resource(ShowPhotosHandler)
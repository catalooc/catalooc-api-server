import math
import inspect
from django.conf import settings
from django.core.paginator import Paginator

class MongoWrapper(object):    
    def __init__(self, index):
        self.db         = settings.MONGO_CONNECTION[settings.MONGO_COLLECTIONS[index][0]]
        self.collection = self.db[settings.MONGO_COLLECTIONS[index][1]]

    def filter(self, request=None, *args, **kwargs):
        self.skip       = 0
        self.limit      = 20
        
        if request is not None:
            if 'skip' in request:
                self.skip = int(float(request.get('skip', None)))
            
            if 'limit' in request:
                self.limit  = int(float(request.get('limit', None)))
        
        self.records    = self.collection.find(*args, **kwargs)
        result          = self.records.skip(self.skip).limit(self.limit)
        total_count     = self.records.count()
        current_total   = result.count()
        
        pagination      = Paginator(result, self.limit)
        total_page      = int(math.ceil(total_count/self.limit))
        page            = int(math.ceil((self.skip+1)/self.limit))
        
        if page < 1:
            page        = 1
        elif page > total_page:
            page        = total_page
        
        this_page       = pagination.page(page)
        
        return {
            'meta'      : {
                'skip'          : self.skip,
                'limit'         : self.limit,
                'total_count'   : total_count,
                'current_total' : current_total,
                'has_next'      : this_page.has_next(),
                'has_previous'  : this_page.has_previous()
            },
            'objects'   : list(result)
        }
    
    def all(self, request):
        return self.filter(request)
        
    def get(self, *args, **kwargs):
        return self.collection.find_one(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.collection.remove(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        return self.collection.save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        return self.collection.update(*args, **kwargs)
    
    def update_all(self, *args, **kwargs):
        return self.collection.update(multi=True, *args, **kwargs)
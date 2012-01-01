from project.libs.mongodb import MongoWrapper

class Post:
    managers    = MongoWrapper("Post")
    
    @classmethod
    def valid_id(self, id):
        return True if self.managers.find( { '_id', 'id' } ).count() > 0 else False
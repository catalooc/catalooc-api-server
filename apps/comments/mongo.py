from project.libs.mongodb import MongoWrapper

class Comments:
    managers    = MongoWrapper("Comments")
    
    @classmethod
    def valid_id(self, id):
        return True if self.managers.find( { '_id', 'id' } ).count() > 0 else False
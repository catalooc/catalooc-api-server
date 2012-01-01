from project.libs.mongodb import MongoWrapper

class Photos:
    managers    = MongoWrapper("Photos")
    
    @classmethod
    def valid_id(self, id):
        return True if self.managers.find( { '_id', 'id' } ).count() > 0 else False
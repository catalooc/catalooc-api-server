from project.libs.mongodb import MongoWrapper

class Profile:
    managers    = MongoWrapper("Profile")

class Settings:
    managers    = MongoWrapper("Comments")
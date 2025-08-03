import pymongo
client = pymongo.MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/calisto_flask1")
db = client["hey_blog"]
db = db["blog"]
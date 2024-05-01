from pymongo.mongo_client import MongoClient


URI = "mongodb+srv://vdunkin:<password>@cluster0.vmj7irm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(URI)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.db

def print_cats(param={}):
    cats = db.cats.find(param)

    for cat in cats:
        # if "color" in cat:
        print(cat)
        
    print(f"\n{'*' * 50} \n")

db.cats.insert_many([
    {"name": "Panther", "age" : 10},
    {"name": "Tiger", "age" : 10}
    ])
        
        
print_cats()

tiger = db.cats.update_one({"name": "British"}, {"$set": {"age": 10, "color": "black"}})

print_cats()

db.cats.delete_many({"age": 10})

print_cats()

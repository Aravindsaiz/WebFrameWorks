import pymongo
import hashlib

class DB():
    is_initialized = False
    def __init__(self):
        try:
            if not DB.is_initialized:
                print("initializing ... ")
                self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
                self.mydb = self.client["passwordStore"]
                DB.is_initialized = True
                print(self.client.list_database_names())
                print(self.mydb)
        except Exception as error:
            raise error
    
    def save_login_details(self, data):
        id = data['email']
        username = data['username']
        pwd = hashlib.sha256((data['password'].encode())).hexdigest()
        phoneno = data['phoneno']
        login_collection = self.mydb["userDetails"]
        response = login_collection.insert_one({"_id" : id, "userName":username, "secret": pwd, "phone":phoneno})
        print(response)
    
    def get_one_document(self,primaryKey,value):
        collection = self.mydb["userDetails"]
        document = collection.find_one({primaryKey:value})
        return document


if __name__ == "__main__":
    obj = DB()
    

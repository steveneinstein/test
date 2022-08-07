import pymongo
client = pymongo.MongoClient("mongodb://steve:stevendsouza@ac-ncw9elm-shard-00-00.gllqoyu.mongodb.net:27017,ac-ncw9elm-shard-00-01.gllqoyu.mongodb.net:27017,ac-ncw9elm-shard-00-02.gllqoyu.mongodb.net:27017/?ssl=true&replicaSet=atlas-48j2oo-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"einstein",
    "email":"einstein@gmail.com",
    "surname":"dsouza"

}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
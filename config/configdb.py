
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

user = 'interlandacris'
pwd = 'NefYEf5j70VCzmXd'


uri = f"mongodb+srv://{user}:{pwd}@clustermine.fhlinut.mongodb.net/?retryWrites=true&w=majority&appName=clusterMine"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.publicaciones
publicaciones_collection = db['publicaciones']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
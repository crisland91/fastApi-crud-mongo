from fastapi import APIRouter
from models.models import publicacionesModel
from config.configdb import publicaciones_collection
from bson.objectid import ObjectId

root = APIRouter()

@root.get("/")
def home():
    return 'Hellow from FastApi'

@root.post("/new_pub")
def post_pub(pub:publicacionesModel):

    newPub = dict(pub)
    res = publicaciones_collection.insert_one(newPub)
    id = res.inserted_id

    return f"Post have been inserted: {id}"

@root.get("/api/pubs")
def get_all_pub():
    res = publicaciones_collection.find()
    pubs = []
    for x in res:
        one_pub = ''
        one_pub = {
            "id": str(x['_id'])
            ,"title": x['title']
            ,"description": x['description']
            ,"created_at" : x['created_at']
            ,"status": x['status']
        }
        pubs.append(one_pub)
    return pubs

@root.get("/api/pub/{id_pub}")
def get_one_pub(id_pub:str):
    one_pub = publicaciones_collection.find_one({'_id': ObjectId(id_pub)})

    one_pub['_id'] = str(one_pub['_id'])
    return one_pub

@root.delete("/api/del_pub/{id_pub}")
def remove_one_pub(id_pub:str):
    print(id_pub)
    publicaciones_collection.delete_one({'_id': ObjectId(id_pub)})
    return 'Pub deleted'


@root.put("/api/upt/{id_pub}")
def update_pub(id_pub:str, pub:publicacionesModel):
    newPub = dict(pub)

    newValues = {
        "title":newPub['title']
        ,"description":newPub['description']
        ,"status":newPub['status']
    }
    res = publicaciones_collection.find_one_and_update({'_id': ObjectId(id_pub)}, { "$set": newValues })
    return f'Pub updated: {res}' 

@root.put("/api/upt_status/{id_pub}")
def update_status_pub(id_pub:str, pub:publicacionesModel):
    newPub = dict(pub)

    newStatus = {
        "status": newPub['status']
    }
    res = publicaciones_collection.find_one_and_update({'_id': ObjectId(id_pub)}, { "$set": newStatus })
    return f'The pub is change the status'

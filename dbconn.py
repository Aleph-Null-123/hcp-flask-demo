from firebase_admin import credentials, firestore, initialize_app, auth

cred = credentials.Certificate('./key.json')

default_app = initialize_app(cred)

db = firestore.client()

def create(collection, new):
    coll = db.collection(collection)
    update_time, ref = coll.add(new)
    return ref.id
	
def read(collection):
    coll = db.collection(collection)
    return {i.id : i.to_dict() for i in coll.stream()}


def update(collection, id, new):
	coll = db.collection(collection)
	coll.document(id).set(new)

def delete(collection, id):
	coll = db.collection(collection)
	coll.document(id).delete()
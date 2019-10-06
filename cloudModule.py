import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase-private-key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://car-protect-53116.firebaseio.com/'
})

ref = db.reference('/')
def writeListToFirebase(l):
	# list format {time_stamp, numpy_array, driver, permit}
	ref.update({'Time' : l[0]})
	ref.update({'Face' : l[1]})
	ref.update({'Driver' : l[2]})
	ref.update({'Permit' : l[3]})
	#print(ref.get())
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('smoke-firebase-cred.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smoke-detect.firebaseio.com/'
})

ref = db.reference('/')
def uploadList(l):
	ref.update({'LPG' : l['GAS_LPG']})
	ref.update({'CO' : l['CO']})
	ref.update({'SMOKE' : l['SMOKE']})
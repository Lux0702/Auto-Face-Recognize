from firebase_admin import credentials, firestore,storage
from firebase_admin import db
import firebase_admin
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognize-fc38b-default-rtdb.firebaseio.com/"
})
 
ref = db.reference('Students')
 
data = {
    "20110771":
        {
            "Tên": "Nguyen Thanh Sang",
            "Ngành": "CNTT",
            "Khóa": 2020,
            "Sinh viên năm": 3
        },
    "20133018":
        {
            "Tên": "Nguyen Thi Thanh Ngan",
            "Ngành": "KTDL",
            "Khóa": 2020,
            "Sinh viên năm": 3
            
        },
    "20133038":
        {
            "Tên": "Tran Le Ngoc Gia Han",
            "Ngành": "KTDL",
            "Khóa": 2020,
            "Sinh viên năm": 3
        },
        "20133099":
        {
            "Tên": "Nguyen Thi Hoang Trang",
            "Ngành": "KTDL",
            "Khóa": 2020,
            "Sinh viên năm": 3
        }
        
}


ref1 = db.reference('Checkin')
 
data1 = {
    "2023-09-04 00:00:00":
        {
            "student_id":20133018
        },
    "2023-09-04 02:00:00":
        {
            "student_id":20133038
        },
    "2023-09-04 02:50:00":
        {
            "student_id":20133099
        }
}
 
for key, value in data.items():
    ref.child(key).set(value)
for key, value in data1.items():
    ref1.child(key).set(value)



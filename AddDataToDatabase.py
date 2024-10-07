import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://newproject-d86a3-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "20001":
        {
            "name": "Vivek Chaurasia",
            "major": "CSE-Aiml",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "10001":
        {
            "name": "Arijit chatterjee",
            "major": "CSE-Sec-A",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "30001":
        {
            "name": "Krishna Agarwal",
            "major": "CSBS",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "40001":
        {
            "name": "Avinash Burnawal",
            "major": "CSBS",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "50001":
        {
            "name": "Ayush Kasyap",
            "major": "IOT",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"90001":
        {
            "name": "Adarsh Shaw",
            "major": "Electrical Eng",
            "starting_year": 2022,
            "total_attendance": 9,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)


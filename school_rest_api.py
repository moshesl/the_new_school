from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/students/',methods=['GET'])
def get_all_students():
    # מחזיר שמות כל התלמידים ת"ז וכיתה
    pass


@app.route('/students/',methods=['POST'])
def add_student(name, t_z, class_):
    #     מוסיף תלמיד למסד נתונים ומחזיר את המילים WHELCOM
    pass


@app.route('/students/<int:stu_id>/',methods=['GET'])
def get_years_student(stu_id):
    #     מחזיר את רשימת שנות לימודיו של אותו תלמיד
    pass


@app.route('/students/<int:stu_id>/', methods=['PUT'])
def update_student(stu_id):
    #     מעדכן את נתוניו של תלמיד מסויים
    pass


@app.route('/students/<int:stu_id>/<int:year>/')
def get_subject(year):
    #   מחזיר רשימת מקצועות והID שלהם לאותה שנה
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg():
    pass


# yakov


@app.route('/students/<int:stu_id>/<ray_of_years>/')
def get_subject(*year):
    # מחזיר רשימת מקצועות וה ID שלהם לפי רישמת השנים בצורה כזאת: 2016,2015,2014
    pass


@app.route('/students/<int:stu_id>/all_years/')
def get_subject():
    # צריך פונקציה שנותנת את כל המקצועות לפי השנים בלי פרמטרים רק תז
    pass



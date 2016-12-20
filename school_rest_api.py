from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = 'pass'


@app.route('/?username', methods=['GET', 'POST', 'PUT', 'DELETE'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')


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


@app.route('/students/<int:stu_id>/<int:year>/', methods=['GET'])
def get_subject(year):
    #   מחזיר רשימת מקצועות והID שלהם לאותה שנה
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_test():
    #  מחזיר רשימת מבחנים
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg(stu_id, year, sub_id):
    # ממוצע של תלמיד במקצוע מסויים
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['POST'])
def add_test(stu_id, year, sub_id):
    pass


@app.route('/students/<int:stu_id>/<int:year>/', methods=['GET'])
def get_subjects(stu_id, year):
    # מחזיר רשימת מקצועות שאותו תלמיד למד
    pass


@app.route('/students/<int:stu_id>/<int:year>/all_sub_avg/', methods=['GET'])
def get_avg_of_year(stu_id, year):
    # ממוצע כללי של כל המקצועות
    pass


@app.route('/students/<int:stu_id>/<int:year>/tests/', methods=['GET'])
def get_subjects_tests(stu_id, year):
    # מחזיר רשימת מבחנים שאותו תלמיד נבחן
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg_by_sub(stu_id, year, sub_id):
    # מחזיר ממוצע לפי מקצוע
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['GET'])
def get_subs_test(stu_id, year, sub_id):
    # מחזיר מבחן ספציפי
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['POST'])
def post_test_by_sub(stu_id, year, sub_id, test_id):
    # מוסיף מבחן ספציפי
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['PUT'])
def get_subs_test(stu_id, year, sub_id, test_id):
    # מעדכן מבחן ספציפי
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg_by_sub(stu_id, year):
    # מחזיר רשימת מקצועות שאותו תלמיד למד
    pass


@app.route('/students/<int:stu_id>/<ray_of_years>/', methods=['GET'])
def get_subject(stu_id,*year):
    # מחזיר רשימת מקצועות וה ID שלהם לפי רישמת השנים בצורה כזאת: 2016,2015,2014
    pass


@app.route('/students/<int:stu_id>/all_years/', methods=['GET'])
def get_all_subjects(stu_id):
    #  צריך לתת פונקציה לקבלת כל המקצועות שאי פעם למד אותו תלמיד בלי פרמטרים לשנה מסויימת
    pass


@app.route('/students/<int:stu_id>/all_years/all_subs/', methods=['GET'])
def get_all_subs_avg(stu_id):
    # מחזיר ממוצע של כל המקצועות
    pass


@app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['GET'])
def get_avg_by_sub(stu_id, sub_id):
    #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
    pass


@app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['POST'])
def post_test_by_sub(stu_id, sub_id):
    #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
    pass

@app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['PUT'])
def update_stu_by_sub(stu_id, sub_id):
    #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
    pass


@app.route('/teacher/')
def teacher():
    pass

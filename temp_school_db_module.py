import sqlite3
con = sqlite3.connect('tables.db3', check_same_thread=False)
con.row_factory = sqlite3.Row
c = sqlite3.connect('tables.db3')


class Student:
    def __init__(self, name, m_z, birthday, class_stu=1):
        self._name = None
        self.name = name
        self._m_z = None
        self.m_z = m_z
        self._birthday = None
        self.birthday = birthday
        self._class_stu = None
        self.class_stu = class_stu

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_stu):
        if type(name_stu) is str:
            self._name = name_stu
        else:
            raise ValueError

    @property
    def m_z(self):
        return self._m_z

    @m_z.setter
    def m_z(self, t_z):
        test = con.execute('SELECT * FROM students WHERE t_z = ?',(t_z,)).fetchone()
        if type(t_z) is int and len(str(t_z)) < 10 and test == None :
            self._m_z = t_z
        else:
            raise ValueError('unavail t_z or already exists! ')

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birth):
        if type(birth) is str and len(birth) <= 10:
            self._birthday = birth
        else:
            raise ValueError

    @property
    def class_stu(self):
        return self._class_stu

    @class_stu.setter
    def class_stu(self, class_s=1):
        if type(class_s) is int and 0 < class_s < 13:
            self._class_stu = class_s
        else:
            raise ValueError


# def get_all_stu():
#     l = []
#     for stu in con.execute('SELECT id,name,class FROM students'):
#         stu = dict(stu)
#         l.append(stu)
#     return l
#
#
# def get_stu(num):
#     sele = con.execute('SELECT * FROM students WHERE id = ?',(num,))
#     sele = sele.fetchone()
#     if sele:
#         return dict(sele)
#     else:
#         raise ValueError ('There is no such student')
#
#
# def add_stu(name, m_z, birthday, class_stu=1):
#     new_ob = Student(name, m_z, birthday, class_stu)
#     stud = con.execute('INSERT INTO students(name,t_z,birthday,class)VALUES (?,?,?,?)',(new_ob.name,new_ob.m_z,new_ob.birthday,new_ob.class_stu))
#     idd = stud.lastrowid
#     con.commit()
#     return get_stu(idd)


def remove_stu(num):
    stu_delete = get_stu(num)
    con.execute('DELETE FROM students WHERE id = ?',(num,))
    con.commit()
    return stu_delete


def update_stu(num, changes):
    a = {'num':num}
    upde = 'UPDATE students SET id=id'
    if 'name' in changes:
        upde += ', name=:name'
        a['name'] = changes['name']
    if 't_z' in changes:
        upde += ', t_z=:t_z'
        a['t_z'] = changes['t_z']
    if 'birthday' in changes:
        upde += ', birthday=:birthday'
        a['birthday'] = changes['birthday']
    if 'class' in changes:
        upde += ', class=:class'
        a['class'] = changes['class']
    upde += ' WHERE id =:num'
    con.execute(upde, a)
    con.commit()
    return get_stu(num)


# מחזיר את כל הפרטים עבור תלמיד מסוים לפי האי די שלו
def get_stu(num):
    sele = con.execute('SELECT * FROM students WHERE id = ?', (num,))
    sele = sele.fetchone()
    if sele:
        return dict(sele)
    else:
        raise ValueError('There is no such student')


# מוסיף תלמידים לבית הספר,בתנאים הנדרשים
def add_stu(name, m_z, birthday, class_stu=1):
    new_ob = Student(name, m_z, birthday, class_stu)
    stud = con.execute(
        'INSERT INTO students(name,t_z,birthday,class)VALUES (?,?,?,?)',
        (new_ob.name, new_ob.m_z, new_ob.birthday, new_ob.class_stu))
    idd = stud.lastrowid
    con.commit()
    return get_stu(idd)


# מחזיר שמות אי די וכיתה של כל ההתלמידים
def get_all_stu():
    l = []
    for stu in con.execute('SELECT id,name,class FROM students'):
        stu = dict(stu)
        l.append(stu)
    return l


# מחזיר רשימת שנים בהם למד התלמיד בבית הספר
def get_students_year(id_stu):
    sele = c.execute(
        """SELECT year FROM students_grade WHERE id_student = ?""",
        (id_stu,)).fetchall()

    return list(set([i[0] for i in sele]))


# מחזיר רשימת מקצועות שלמד התלמיד בשנה זו
def subject_per_year(id_stu, year):
    sele = c.execute("""SELECT subject FROM subjects INNER JOIN
                        students_grade ON id_subject = subjects.id WHERE
                        id_student = ? AND year = ?""",
                     (id_stu, year)).fetchall()
    if sele:
        return list(set([i[0] for i in sele]))
    raise ValueError(
        'No record for student:{} in year:{}'.format(id_stu, year))


def avg_all_grade(id_stu, year):
    sele = c.execute(
        """SELECT AVG(grade) FROM students_grade WHERE id_student = ? AND year = ? """
        , (id_stu, year)).fetchone()[0]
    return round(sele, 2)


def avg_sub(id_stu, year, id_sub):
    sele = c.execute(
        """SELECT AVG(grade) FROM students_grade WHERE id_student = ? AND year = ? AND id_subject = ?"""
        , (id_stu, year, id_sub)).fetchone()[0]
    return round(sele, 2)


# הפונקציה הבאה מקבלת שנה מסוימת ו- id של תלמיד מסוים,ומחזירה טפל עם שמות מקצוע והציון של אותו תלמיד בהם


def grade_per_year(id_stu, year):
    sele = con.execute("""SELECT subject,grade FROM subjects INNER JOIN
                        students_grade ON id_subject = subjects.id WHERE
                        id_student = ? AND year = ?""", (id_stu, year))
    sele = sele.fetchall()
    if sele:
        return dict(sele)
    raise ValueError('No record for studedent:{} in year:{}'.format(id_stu, year))


# הפונקציה הבאה מקבלת שנה מסוימת ומחזירה list of tupples שבכל טאפל יש id של תלמיד,מקצוע,וציון

def all_grade_year(year):
    lst = []
    sele = con.execute("""SELECT subject,grade,id_student FROM subjects INNER JOIN
                         students_grade ON id_subject = subjects.id WHERE
                          year = ?""", (year,))
    for i in sele:
        lst.append({'id_stu': i[2], 'subject': i[0], 'grade': i[1]})
    if lst:
        return lst
    raise ValueError('No record for year:{}'.format(year))


def get_tests(id_stu, year, id_sub):
    pass

def stu_by_year_sub_test(stu_id, year, sub_id, test_id):
    pass

def get_avg(id_stu, year, id_sub):
    pass


def add_test(id_stu, id_sub, grade, year, class_):
    pass


# הפונקציה הבאה מחזירה מקבלת id של תלמיד ןמחזירה את השנים שבהם למד(נבחן)בביה"ס

def get_years_student(id_stu):
    return c.execute("""SELECT year FROM students_grade WHERE id_student=? """,
                     (id_stu,)).fetchall()

# print(add_stu('yisrael',67657509,'21-12-2000',2))

# print(get_all_stu())
# print(update_stu(3,{'class': 555,'name':'barchun'}))
# print(grade_per_year(1,2016))
# print(all_gread_year(2016))
# print(get_years_student(1))
# chang = {'name':'davad', 't_z': 34473375, 'birthday':'1999-12-11', 'class':4}
# print(update_stu(5, chang))

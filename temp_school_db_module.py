import sqlite3
con = sqlite3.connect('tables.db3', check_same_thread=False)
con.row_factory = sqlite3.Row


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
        if type(t_z) is int and len(str(t_z)) < 10:
            self._m_z = t_z
        else:
            raise ValueError

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


def get_all_stu():
    l = []
    instance = con.execute('SELECT id,name,t_z FROM students')
    for stu in tuple(instance):
        stu = dict(stu)
        l.append(stu)
    return l


def get_stu(num):
    sele = con.execute('SELECT * FROM students WHERE id = ?',(num,))
    sele = sele.fetchone()
    if sele:
        return dict(sele)
    else:
        raise ValueError ('There is no such student')


def add_stu(name, m_z, birthday, class_stu=1):
    new_ob = Student(name, m_z, birthday, class_stu)
    stud = con.execute('INSERT INTO students(name,t_z,birthday,class)VALUES (?,?,?,?)',(new_ob.name,new_ob.m_z,new_ob.birthday,new_ob.class_stu))
    idd = stud.lastrowid
    return get_stu(idd)


def remove_stu(num):
    stu_delete = get_stu(num)
    con.execute('DELETE FROM students WHERE id = ?',(num,))
    return stu_delete



# moshe = ('moshe', 987654321, '1900-16-04', 8)
# yakov = ('Yakov', 304499932, '1980-05-12')
# add_stu(*moshe)
# print(get_all_stu())



con.commit()

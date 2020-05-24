from lib.API.ClassApi import sclass
from lib.API.TeacherApi import steacher
from hyrobot.common import INFO
from lib.API.StudentApi import sstudent


def suite_setup():
    INFO("初始化清除所有学生，老师，班级")
    sstudent.del_student_all()
    steacher.del_teacher_all()
    sclass.del_class_all()


def suite_teardown():
    pass

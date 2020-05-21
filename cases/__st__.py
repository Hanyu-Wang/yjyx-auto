from lib.API.ClassApi import sclass
from lib.API.TeacherApi import steacher
from hyrobot.common import INFO


def suite_setup():
    INFO("初始化清除所有老师，班级")
    steacher.del_teacher_all()
    sclass.del_class_all()


def suite_teardown():
    pass

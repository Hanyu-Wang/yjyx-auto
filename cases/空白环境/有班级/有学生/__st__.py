from lib.API.StudentApi import sstudent
from hyrobot.common import GSTORE, INFO


def suite_setup():
    INFO("初始化新建一个学生")
    r = sstudent.add_student("yuchigong", "尉迟恭", 3, GSTORE["g_classid"], 13451810000)
    addret = r.json()
    GSTORE["g_student_id"] = addret["id"]


def suite_teardown():
    sstudent.del_student(GSTORE["g_student_id"])

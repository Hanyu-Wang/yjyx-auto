from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
from lib.UI.TeacherAction import teacherOp
from lib.API.StudentApi import sstudent
from lib.UI.StudentAution import studentOp


class C44:
    name = "tc000044"

    def teardown(self):
        teacherOp.quit_browser()

    def teststeps(self):
        STEP(1, "使用不存的教师账号登录")
        logininfo = teacherOp.teacher_loginno()
        expect = '登录失败 : 用户或者密码错误'
        CHECK_POINT("给出错误提示", logininfo == expect)


class C45:
    name = "tc000045"

    def teardown(self):
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, "使用不存的学生账号登录")
        info = studentOp.student_loginno()
        expect = '登录失败 : 用户或者密码错误'
        CHECK_POINT("给出错误提示", info == expect)

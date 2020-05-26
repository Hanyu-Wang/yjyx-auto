from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.UI.TeacherAction import teacherOp
from lib.API.StudentApi import sstudent
from lib.UI.StudentAution import studentOp


class C19:
    name = "tc005001"

    def teardown(self):
        steacher.del_teacher(self.addtid)
        teacherOp.quit_browser()

    def teststeps(self):
        STEP(1, "新建一个老师")
        data = [{"id": GSTORE["g_classid"]}]
        classid = json.dumps(data)
        r = steacher.add_teacher(
            "qsh",
            "秦始皇",
            1,
            classid,
            "13451813456",
            "jcysdf@123.com",
            "3209251983090987899",
        )
        addret = r.json()
        self.addtid = addret["id"]
        STEP(2, "老师账号登录")
        teacherOp.teacher_login("qsh", "888888")
        homeinfo = teacherOp.gethomepageinfo()
        expect = ["白月学院00002", "秦始皇", "初中数学", "0", "0", "0"]
        STEP(3, "验证主页信息")
        CHECK_POINT("主页信息显示正确", homeinfo == expect)
        STEP(4, "验证学生列表")
        classinfo = teacherOp.getclassstudentinfo_none()
        expect1 = "该班级还没有学生注册"
        CHECK_POINT("班级学生列表为空", classinfo == expect1)


class C21:
    name = "tc005081"

    def teardown(self):
        sstudent.del_student(self.addtid)
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, "新建一个学生")
        r = sstudent.add_student(
            "yuchigong", "尉迟恭", 3, GSTORE["g_classid"], 13451810000
        )
        addret = r.json()
        self.addtid = addret["id"]
        STEP(2, "学生账号登录")
        studentOp.student_login("yuchigong", "888888")
        homeinfo = studentOp.gethomepageinfo()
        expect = ['尉迟恭', '白月学院00002', '0', '0']
        STEP(3, "验证主页信息")
        CHECK_POINT("主页信息显示正确", homeinfo == expect)
        STEP(4, "验证学生列表")
        classinfo = studentOp.getwrong_questionsinfo_none()
        expect1 = "您尚未有错题入库哦"
        INFO(expect1)
        CHECK_POINT("班级学生列表为空", classinfo == expect1)

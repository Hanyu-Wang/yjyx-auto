from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.UI.TeacherAction import teacherOp


class C20:
    name = "tc005002"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)

    def teststeps(self):
        STEP(1, "添加一个老师")
        data = [{"id": GSTORE["g_classid"]}]
        classid = json.dumps(data)
        r = steacher.add_teacher(
            "hwd",
            "汉武帝",
            1,
            classid,
            "13600000000",
            "jcysdf@123.com",
            "3209251983090987899",
        )
        addret = r.json()
        self.addteacherid = addret["id"]
        STEP(2, "验证参数返回值")
        CHECK_POINT("返回的retcode值=0", addret["retcode"] == 0)
        STEP(3, "老师账号登录")
        teacherOp.teacher_login("hwd", "888888")
        homeinfo = teacherOp.gethomepageinfo()
        expect = ["白月学院00002", "汉武帝", "初中数学", "0", "0", "0"]
        STEP(3, "验证主页信息")
        CHECK_POINT("主页信息显示正确", homeinfo == expect)
        STEP(4, "验证学生列表")
        classinfo = teacherOp.getclassstudentinfo()
        INFO(classinfo)
        expect1 = ["尉迟恭"]
        CHECK_POINT("班级学生数据", classinfo == expect1)

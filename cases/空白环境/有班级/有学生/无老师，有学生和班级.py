from lib.API.TeacherApi import steacher
from lib.API.StudentApi import sstudent
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.UI.TeacherAction import teacherOp
from lib.UI.StudentAution import studentOp


class C20:
    name = "tc000020"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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


class C57:
    name = "tc000057"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        sstudent.del_student(self.addstudentid)
        teacherOp.quit_browser()
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, "新建一个老师")
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('hwd', '汉武帝', 1, classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        self.addteacherid = addret['id']
        STEP(2, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(3, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '教师发布作业')
        teacherOp.teacher_login('hwd', '888888')
        teacherOp.pushtask()

        STEP(5, "学生账号登录")
        studentOp.student_login("cyj", "888888")
        info = studentOp.getMyTask()
        INFO(info)
        expect = ['汉武帝', '初中数学']
        CHECK_POINT("任务信息显示正确", info == expect)


class C58:
    name = "tc000058"

    def teardown(self):
        sstudent.del_student(self.addstudentid)
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(2, "学生账号登录")
        studentOp.student_login("cyj", "888888")
        info = studentOp.getMyTask()
        INFO(info)
        expect = '没有发现作业任务'
        CHECK_POINT("内容显示正确", info == expect)


class C59:
    name = "tc000059"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        sstudent.del_student(self.addstudentid)
        teacherOp.quit_browser()
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, "新建一个老师")
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('hwd', '汉武帝', 1, classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        self.addteacherid = addret['id']
        STEP(2, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(3, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '教师发布作业')
        teacherOp.teacher_login('hwd', '888888')
        teacherOp.pushtask()

        STEP(5, "学生账号提交作业并检查统计信息")
        studentOp.student_login("cyj", "888888")
        studentOp.submittask()
        info = studentOp.get_statistics_info()
        INFO(info)
        expect = ['初中数学', '1', '3', '0', '3']
        CHECK_POINT("任务信息显示正确", info == expect)


class C60:
    name = "tc000060"

    def teardown(self):
        sstudent.del_student(self.addstudentid)
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(2, "学生账号登录")
        studentOp.student_login("cyj", "888888")
        info = studentOp.get_statistics_info()
        INFO(info)
        expect = '没有题目统计数据'
        CHECK_POINT("内容显示正确", info == expect)


class C61:
    name = "tc000061"

    def teardown(self):
        sstudent.del_student(self.addstudentid)
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(2, "学生账号登录")
        studentOp.student_login("cyj", "888888")
        info = studentOp.get_Personal_Info()
        INFO(info)
        expect = ['cyj', '13451810000', '程咬金', '七年级 高三25班', '白月学院00002', '广东省深圳市南山区']
        CHECK_POINT("内容显示正确", info == expect)


class C62:
    name = "tc000062"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        sstudent.del_student(self.addstudentid)
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, "新建一个老师")
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('hwd', '汉武帝', 1, classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        self.addteacherid = addret['id']
        STEP(2, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(3, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP('4', '有班主任')
        studentOp.student_login("cyj", "888888")
        info = studentOp.get_Personal_Info()
        INFO(info)
        expect = '初中数学老师：汉武帝'
        CHECK_POINT("班主任信息显示正确", info == expect)


class C63:
    name = "tc000063"

    def teardown(self):
        sstudent.del_student(self.addstudentid)
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(2, "学生账号登录")
        studentOp.student_login("cyj", "888888")
        info = studentOp.modify_user_info()
        INFO(info)
        expect = '用户信息修改成功'
        CHECK_POINT("内容显示正确", info == expect)


class C64:
    name = "tc000064"

    def teardown(self):
        sstudent.del_student(self.addstudentid)
        studentOp.quit_browser()

    def teststeps(self):
        STEP(1, '新建一个学生')
        r = sstudent.add_student('cyj', '程咬金', 1, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(2, "学生账号登录")
        studentOp.student_login("cyj", "888888")
        studentOp.modify_user_info()
        info = studentOp.get_Personal_Info()
        INFO(info)
        expect = ['cyj', '13451810000', '三板斧', '七年级 高三25班', '白月学院00002', '广东省深圳市南山区']
        CHECK_POINT("内容显示正确", info == expect)

from lib.API.StudentApi import sstudent
from lib.UI.TeacherAction import teacherOp
from lib.UI.StudentAution import studentOp
from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
import time


class C22:
    name = "tc000022"

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
        student_info = studentOp.submittask()
        INFO(student_info)
        STEP(6, "教师登录检查作业")
        time.sleep(2)
        teacherOp.teacher_login('hwd', '888888')
        teacher_info = teacherOp.checktask().strip()
        INFO(teacher_info)
        CHECK_POINT("答题正确率正确", student_info == teacher_info)


class C23:
    name = "tc000023"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '教师发布作业')
        teacherOp.teacher_login('hwd', '888888')
        task_name = teacherOp.pushtaskran(100)
        INFO(task_name)
        INFO(GSTORE['g_ransrt'])
        CHECK_POINT("作业名称正确", task_name == GSTORE['g_ransrt'])


class C24:
    name = "tc000024"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '教师发布作业')
        teacherOp.teacher_login('hwd', '888888')
        task_name = teacherOp.pushtaskran(1)
        INFO(task_name)
        INFO(GSTORE['g_ransrt'])
        CHECK_POINT("作业名称正确", task_name == GSTORE['g_ransrt'])


class C25:
    name = "tc000025"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '教师发布作业')
        teacherOp.teacher_login('hwd', '888888')
        task_name = teacherOp.pushtask0(0)
        expect = '请输入作业名称'
        CHECK_POINT("作业名称正确", task_name == expect)


class C46:
    name = "tc000046"

    def teardown(self):
        teacherOp.quit_browser()

    def teststeps(self):
        STEP(1, "教师登录")
        teacherOp.teacher_login('qsh', '888888')
        classinfo = teacherOp.getclassstudentinfo()
        INFO(classinfo)
        expect1 = ['尉迟恭']
        CHECK_POINT("班级列表学员正确", classinfo == expect1)


class C47:
    name = "tc000047"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '查看统计分析')
        teacherOp.teacher_login('hwd', '888888')
        info = teacherOp.get_analysis()
        expect = ['学生', '任务', '错题榜']
        CHECK_POINT("统计分析主页信息正确", info == expect)


class C48:
    name = "tc000048"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '查看统计分析-学生')
        teacherOp.teacher_login('hwd', '888888')
        info = teacherOp.get_analysis_student()
        expect = '尉迟恭'
        CHECK_POINT("统计分析主页信息正确", info == expect)


class C49:
    name = "tc000049"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '查看统计分析-任务(没有发布作业)')
        teacherOp.teacher_login('hwd', '888888')
        info = teacherOp.get_analysis_task()
        expect = ['初中数学', '0']
        CHECK_POINT("统计分析主页信息正确", info == expect)


class C50:
    name = "tc000050"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '查看统计分析-任务(发布作业)')
        teacherOp.teacher_login('hwd', '888888')
        teacherOp.pushtask()
        info = teacherOp.get_analysis_task()
        expect = ['初中数学', '1']
        CHECK_POINT("统计分析主页信息正确", info == expect)


class C51:
    name = "tc000051"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        sstudent.del_student(self.addstudentid)
        # teacherOp.quit_browser()
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
        student_info = studentOp.submittask()
        INFO(student_info)
        STEP(6, "教师登录检查错题")
        time.sleep(2)
        teacherOp.teacher_login('hwd', '888888')
        info = teacherOp.get_analysis_error()
        expect = '共有3道错题上榜'
        CHECK_POINT('错题数目正确', info == expect)


class C52:
    name = "tc000052"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '查看统计分析-任务(发布作业)')
        teacherOp.teacher_login('hwd', '888888')
        info = teacherOp.check_push_task()
        INFO(info)
        expect = "没有找到作业任务"
        CHECK_POINT("统计分析主页信息正确", info == expect)


class C53:
    name = "tc000053"

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        teacherOp.quit_browser()

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
        STEP(4, '查看统计分析-任务(发布作业)')
        teacherOp.teacher_login('hwd', '888888')
        teacherOp.pushtask()
        info = teacherOp.check_push_task()
        INFO(info)
        expect = '发布作业'
        CHECK_POINT("发布作业信息正确", info == expect)
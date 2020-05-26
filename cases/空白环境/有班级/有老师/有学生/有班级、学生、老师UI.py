from lib.API.StudentApi import sstudent
from lib.UI.TeacherAction import teacherOp
from lib.UI.StudentAution import studentOp
from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
import time


class C22:
    name = "tc005101"

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
    name = "tc005104"

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
        task_name = teacherOp.pushtask100()
        CHECK_POINT("答题正确率正确", task_name == GSTORE['g_ransrt'])

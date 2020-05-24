from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.UI.TeacherAction import teacherOp


class C19:
    name = 'tc005001'

    def teardown(self):
        steacher.del_teacher(self.addtid)

    def teststeps(self):
        STEP(1, '新建一个老师')
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('qsh', '秦始皇', 1, classid,
                                 '13451813456', 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        self.addtid = addret['id']
        STEP(2, '老师账号登录')
        teacherOp.teacher_login('qsh', '888888')
        homeinfo = teacherOp.gethomepageinfo_none()
        expect = ['白月学院00002', '秦始皇', '初中数学', '0', '0', '0']
        STEP(3, '验证主页信息')
        CHECK_POINT('主页信息显示正确', homeinfo == expect)
        STEP(4, '验证学生列表')
        classinfo = teacherOp.getclassstudentinfo_none()
        expect1 = '该班级还没有学生注册'
        CHECK_POINT('班级学生列表为空', classinfo == expect1)

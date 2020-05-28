from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.API.StudentApi import sstudent
from lib.UI.TeacherAction import teacherOp
from lib.UI.StudentAution import studentOp


class C17:
    name = 'tc000017'

    def teardown(self):
        sstudent.del_student(self.addstudentid)

    def teststeps(self):
        STEP(1, '先列出学生')
        r = sstudent.student_list()
        listret = r.json()
        studentlist = listret["retlist"]
        STEP(2, '添加一个学生')
        r = sstudent.add_student('cyj', '程咬金', 6, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentid = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = sstudent.student_list()
        listrest = r.json()
        expected = {
            "retlist": studentlist + [
                {
                    "classid": GSTORE['g_classid'],
                    "realname": "程咬金",
                    "username": "cyj",
                    "phonenumber": "13451810000",
                    "id": addret['id']
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C18:
    name = 'tc000018'

    def teststeps(self):
        STEP(1, '先列出学生')
        r = sstudent.student_list()
        listret = r.json()
        studentlist = listret["retlist"]
        STEP(2, '添加一个学生')
        r = sstudent.add_student('cyj', '程咬金', 6, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        STEP(3, '删除新增的学生')
        r = sstudent.del_student(addret['id'])
        STEP(4, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(5, '检查系统数据')
        r = sstudent.student_list()
        listrest = r.json()
        expected = {
            "retlist": studentlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C26:
    name = 'tc000026'

    def teststeps(self):
        STEP(1, '先列出学生')
        r = sstudent.student_list()
        listret = r.json()
        studentlist = listret["retlist"]
        STEP(2, '添加一个学生')
        r = sstudent.add_student('yuchigong', '尉迟恭', 6, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=1',
                    addret['retcode'] == 1)
        STEP(4, '检查系统数据')
        r = sstudent.student_list()
        listrest = r.json()
        expected = {
            "retlist": studentlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C27:
    name = 'tc000027'

    def teststeps(self):
        STEP(1, '先列出学生')
        r = sstudent.student_list()
        listret = r.json()
        studentlist = listret["retlist"]
        STEP(2, '修改一个不存在的学生')
        r = sstudent.modify_student('0', '尉迟恭', '13451810000')
        addret = r.json()
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=404',
                    addret['retcode'] == 404)
        STEP(4, '检查系统数据')
        r = sstudent.student_list()
        listrest = r.json()
        expected = {
            "retlist": studentlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C28:
    name = 'tc000028'

    def teardown(self):
        sstudent.del_student(self.addstudentid)

    def teststeps(self):
        STEP(1, '先列出学生')
        r = sstudent.student_list()
        listret = r.json()
        studentlist = listret["retlist"]
        STEP(2, '添加一个学生')
        r = sstudent.add_student('cyj', '程咬金', 6, GSTORE['g_classid'], 13400000000)
        addret = r.json()
        self.addstudentid = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '修改新增的学员信息')
        r = sstudent.modify_student('addret["id"]', '三板斧', 13400000000)
        r = sstudent.student_list()
        listrest = r.json()
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        expected = {
            "retlist": studentlist + [
                {
                    "classid": GSTORE['g_classid'],
                    "realname": "三板斧",
                    "username": "cyj",
                    "phonenumber": "13400000000",
                    "id": addret['id']
                }
            ],
            "retcode": 0
        }
        INFO(expected)
        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C29:
    name = 'tc000029'

    def teardown(self):
        sstudent.del_student(self.addstudentid)

    def teststeps(self):
        STEP(1, '先列出学生')
        r = sstudent.student_list()
        listret = r.json()
        studentlist = listret["retlist"]
        STEP(2, '添加一个学生')
        r = sstudent.add_student('cyj', '程咬金', 6, GSTORE['g_classid'], 13400000000)
        addret = r.json()
        self.addstudentid = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '修改新增的学员信息')
        r = sstudent.modify_student('addret["id"]', '程咬金', 13411111111)
        r = sstudent.student_list()
        listrest = r.json()
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        expected = {
            "retlist": studentlist + [
                {
                    "classid": GSTORE['g_classid'],
                    "realname": "程咬金",
                    "username": "cyj",
                    "phonenumber": "13411111111",
                    "id": addret['id']
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C30:
    name = 'tc000030'

    def teststeps(self):
        STEP(1, '先列出学生')
        r = sstudent.student_list()
        listret = r.json()
        studentlist = listret["retlist"]
        STEP(2, '删除不存在的学生')
        r = sstudent.del_student(0)
        addret = r.json()
        STEP(4, '验证参数返回值')
        CHECK_POINT('返回的retcode值=404',
                    addret['retcode'] == 404)
        STEP(5, '检查系统数据')
        r = sstudent.student_list()
        listrest = r.json()
        expected = {
            "retlist": studentlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)

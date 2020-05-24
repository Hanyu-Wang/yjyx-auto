from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.API.ClassApi import sclass
from lib.API.StudentApi import sstudent


class C17:
    name = 'tc002002'

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
    name = 'tc002081'

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



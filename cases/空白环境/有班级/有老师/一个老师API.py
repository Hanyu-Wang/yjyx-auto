from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.API.ClassApi import sclass
from lib.API.StudentApi import sstudent


class C10:
    name = 'tc001002'

    def teardown(self):
        steacher.del_teacher(self.addteacherid)

    def teststeps(self):
        STEP(1, '先列出老师')
        r = steacher.teacher_list()
        listret = r.json()
        teacherlist = listret["retlist"]
        STEP(2, '添加一个老师')
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('hwd', '汉武帝', 1, classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        self.addteacherid = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": teacherlist + [
                {
                    "username": "hwd",
                    "teachclasslist": [
                        GSTORE['g_classid']
                    ],
                    "realname": "汉武帝",
                    "id": addret['id'],
                    "phonenumber": "13600000000",
                    "email": "jcysdf@123.com",
                    "idcardnumber": "3209251983090987899"
                }
            ],
            "retcode": 0
        }
        INFO(expected)

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C11:
    name = 'tc001003'

    def teststeps(self):
        STEP(1, '先列出老师')
        r = steacher.teacher_list()
        listret = r.json()
        teacherlist = listret["retlist"]
        STEP(2, '添加一个老师')
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('qsh', '秦始皇', 14, classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=1',
                    addret['retcode'] == 1)
        STEP(4, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": teacherlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C12:
    name = 'tc001051'

    def teststeps(self):
        STEP(1, '先列出老师')
        r = steacher.teacher_list()
        listret = r.json()
        teacherlist = listret["retlist"]
        STEP(2, '修改不存在老师')
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.modify_teacher('0', '秦始皇', 1, classid, '13600000000',
                                    'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=1',
                    addret['retcode'] == 1)
        STEP(4, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": teacherlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C13:
    name = 'tc001052'

    def teardown(self):
        steacher.del_teacher(self.addteacherid)
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出老师')
        r = steacher.teacher_list()
        listret = r.json()
        teacherlist = listret["retlist"]
        STEP(2, '添加一个老师')
        n_data = [{"id": GSTORE['g_classid']}]
        n_classid = json.dumps(n_data)
        r = steacher.add_teacher('hwd', '汉武帝', 1, n_classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addtret = r.json()
        self.addteacherid = addtret['id']
        STEP(3, '添加一个班级')
        r = sclass.add_class(5, '高二17班', 50)
        addcret = r.json()
        self.addcid = addcret['id']
        STEP(4, '修改教师')
        m_data = [{"id": GSTORE['g_classid']}, {"id": addcret['id']}]
        m_classid = json.dumps(m_data)
        r = steacher.modify_teacher(addtret['id'], '诸葛亮', 14, m_classid, '13600000000',
                                    'jcysdf@123.com', '3209251983090987899')
        addretcode = r.json()
        STEP(5, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addretcode['retcode'] == 0)
        STEP(6, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": teacherlist + [
                {
                    "username": "hwd",
                    "teachclasslist": [
                        GSTORE['g_classid'], addcret['id']
                    ],
                    "realname": "诸葛亮",
                    "id": addtret['id'],
                    "phonenumber": "13600000000",
                    "email": "jcysdf@123.com",
                    "idcardnumber": "3209251983090987899"
                }
            ],
            "retcode": 0
        }
        INFO(expected)
        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C14:
    name = 'tc001081'

    def teststeps(self):
        STEP(1, '先列出老师')
        r = steacher.teacher_list()
        listret = r.json()
        teacherlist = listret["retlist"]
        STEP(2, '删除不存在的老师')
        r = steacher.del_teacher(0)
        addret = r.json()
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=404',
                    addret['retcode'] == 404)
        STEP(4, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": teacherlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C15:
    name = 'tc001082'

    def teststeps(self):
        STEP(1, '先列出老师')
        r = steacher.teacher_list()
        listret = r.json()
        teacherlist = listret["retlist"]
        STEP(2, '添加一个老师')
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('hwd', '汉武帝', 1, classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        STEP(3, '删除老师')
        r = steacher.del_teacher(addret['id'])
        delret = r.json()
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    delret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": teacherlist,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C16:
    name = 'tc002001'

    def teardown(self):
        sstudent.del_student(self.addstudentret)

    def teststeps(self):
        STEP(1, '新增一个学生 ')
        r = sstudent.add_student('yuchigong', '尉迟恭', 6, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        self.addstudentret = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = sstudent.student_list()
        listrest = r.json()
        expected = {
            "retlist": [
                {
                    "classid": GSTORE['g_classid'],
                    "realname": "尉迟恭",
                    "username": "yuchigong",
                    "phonenumber": "13451810000",
                    "id": addret['id']
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)




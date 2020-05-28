from lib.API.ClassApi import sclass
from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json
from lib.API.StudentApi import sstudent


class C2:
    name = 'tc000002'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出客户')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1 + [
                {
                    "name": "高三26班",
                    "grade__name": "高三",
                    "invitecode": addret["invitecode"],
                    "studentlimit": 50,
                    "studentnumber": 0,
                    "id": addret['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C3:
    name = 'tc000003'

    def teststeps(self):
        STEP(1, '先列出所有班级')
        r = sclass.class_list()
        listret1 = r.json()
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三25班', 50)
        addret = r.json()
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 1)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = listret1

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C4:
    name = 'tc000004'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出班级')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(3, '修改班级名称')
        r = sclass.modify_class(addret['id'], '高三27班', 50)
        mret = r.json()
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=0',
                    mret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1 + [
                {
                    "name": "高三27班",
                    "grade__name": "高三",
                    "invitecode": addret["invitecode"],
                    "studentlimit": 50,
                    "studentnumber": 0,
                    "id": addret['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C5:
    name = 'tc000005'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出班级')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(3, '修改班级名称')
        r = sclass.modify_class(addret['id'], '高三25班', 50)
        mret = r.json()
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=1',
                    mret['retcode'] == 1)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1 + [
                {
                    "name": "高三26班",
                    "grade__name": "高三",
                    "invitecode": addret["invitecode"],
                    "studentlimit": 50,
                    "studentnumber": 0,
                    "id": addret['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C6:
    name = 'tc000006'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出班级')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(3, '修改班级名称')
        r = sclass.modify_class(0, '高三25班', 50)
        mret = r.json()
        INFO('52')
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=404',
                    mret['retcode'] == 404)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1 + [
                {
                    "name": "高三26班",
                    "grade__name": "高三",
                    "invitecode": addret["invitecode"],
                    "studentlimit": 50,
                    "studentnumber": 0,
                    "id": addret['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C8:
    name = 'tc000008'

    def teststeps(self):
        STEP(1, '先列出班级')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        STEP(3, '删除班级')
        r = sclass.del_class(addret["id"])
        mret = r.json()
        INFO('')
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=0',
                    mret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C9:
    name = 'tc000009'

    def teardown(self):
        steacher.del_teacher(self.addtid)

    def teststeps(self):
        STEP(1, '新建一个老师')
        data = [{"id": GSTORE['g_classid']}]
        classid = json.dumps(data)
        r = steacher.add_teacher('qsh', '秦始皇', 1, classid,
                                 '13451813456', 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        self.addtid = addret["id"]
        STEP(2, '验证返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(3, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": [
                {
                    "username": "qsh",
                    "teachclasslist": [GSTORE['g_classid']],
                    "realname": "秦始皇",
                    "id": addret["id"],
                    "phonenumber": "13451813456",
                    "email": "jcysdf@123.com",
                    "idcardnumber": "3209251983090987899"
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C35:
    name = 'tc000035'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出班级')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(3, '修改班级名称')
        r = sclass.modify_class(addret['id'], '高三26班', 80)
        mret = r.json()
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=0',
                    mret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1 + [
                {
                    "name": "高三26班",
                    "grade__name": "高三",
                    "invitecode": addret["invitecode"],
                    "studentlimit": 80,
                    "studentnumber": 0,
                    "id": addret['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C36:
    name = 'tc000036'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出班级')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(3, '修改班级名称')
        r = sclass.modify_class(addret['id'], '高三28班', 80)
        mret = r.json()
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=0',
                    mret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1 + [
                {
                    "name": "高三28班",
                    "grade__name": "高三",
                    "invitecode": addret["invitecode"],
                    "studentlimit": 80,
                    "studentnumber": 0,
                    "id": addret['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C37:
    name = 'tc000037'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '先列出班级')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '添加一个班级')
        r = sclass.add_class(6, '高三26班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(3, '修改班级名称')
        r = sclass.modify_class(addret['id'], '', 50)
        mret = r.json()
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=1',
                    mret['retcode'] == 1)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1 + [
                {
                    "name": "高三26班",
                    "grade__name": "高三",
                    "invitecode": addret["invitecode"],
                    "studentlimit": 50,
                    "studentnumber": 0,
                    "id": addret['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C39:
    name = 'tc000039'

    def teststeps(self):
        STEP(1, '添加一个username为空的老师')
        n_data = [{"id": GSTORE['g_classid']}]
        n_classid = json.dumps(n_data)
        r = steacher.add_teacher('', '汉武帝', 1, n_classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addretcode = r.json()
        STEP(2, '验证参数返回值')
        CHECK_POINT('返回的retcode值=1',
                    addretcode['retcode'] == 1)
        STEP(3, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": [],
            "retcode": 0
        }
        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C40:
    name = 'tc000040'

    def teardown(self):
        steacher.del_teacher(self.addretcodeid)

    def teststeps(self):
        STEP(1, '添加一个realname为空的老师')
        n_data = [{"id": GSTORE['g_classid']}]
        n_classid = json.dumps(n_data)
        r = steacher.add_teacher('hwd', '', 1, n_classid, '13600000000',
                                 'jcysdf@123.com', '3209251983090987899')
        addretcode = r.json()
        self.addretcodeid = addretcode['id']
        STEP(2, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addretcode['retcode'] == 0)
        STEP(3, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "retlist": [
                {
                    "username": "hwd",
                    "teachclasslist": [
                        GSTORE['g_classid']
                    ],
                    "realname": "",
                    "id": addretcode['id'],
                    "phonenumber": "13600000000",
                    "email": "jcysdf@123.com",
                    "idcardnumber": "3209251983090987899"
                }
            ],
            "retcode": 0
        }
        INFO(expected)
        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C41:
    name = 'tc000041'

    # def teardown(self):
    #     sstudent.del_student(self.addstudentret)

    def teststeps(self):
        STEP(1, '新增一个学生 ')
        r = sstudent.add_student('', '尉迟恭', 6, GSTORE['g_classid'], 13451810000)
        addret = r.json()
        # self.addstudentret = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=1',
                    addret['retcode'] == 1)
        STEP(4, '检查系统数据')
        r = sstudent.student_list()
        listrest = r.json()
        expected = {
            "retlist": [],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C42:
    name = 'tc000042'

    def teardown(self):
        sstudent.del_student(self.addstudentret)

    def teststeps(self):
        STEP(1, '新增一个学生 ')
        r = sstudent.add_student('yuchigong', '', 6, GSTORE['g_classid'], 13451810000)
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
                    "realname": "",
                    "username": "yuchigong",
                    "phonenumber": "13451810000",
                    "id": addret['id']
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)


class C43:
    name = 'tc000043'

    def teardown(self):
        sstudent.del_student(self.addstudentret)

    def teststeps(self):
        STEP(1, '新增一个学生 ')
        r = sstudent.add_student('yuchigong', '尉迟恭', 6, GSTORE['g_classid'], '')
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
                    "phonenumber": "",
                    "id": addret['id']
                }
            ],
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)
from lib.API.ClassApi import sclass
from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE


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
    name = 'tc000051'

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
    name = 'tc000052'

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
        INFO('52')
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
    name = 'tc000053'

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
    name = 'tc000082'

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
    name = 'tc001001'

    def teststeps(self):
        STEP(1, '新建一个老师')
        data = 'lishiming', '李世民', 1, [{"id": GSTORE['g_classid']}], 13451813456, 'jcysdf@123.com', 3209251983090987899
        r = steacher.add_teacher(data)
        addret = r.json()
        STEP(2, '验证返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {

        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)

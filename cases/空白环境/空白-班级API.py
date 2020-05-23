from lib.API.ClassApi import sclass
from hyrobot.common import STEP, CHECK_POINT, INFO


class C1:
    name = 'tc000001'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '添加一个班级')
        r = sclass.add_class(6, '高三23班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(2, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(3, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": [
                {
                    "name": "高三23班",
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


class C7:
    name = 'tc000081'

    def teststeps(self):
        STEP(1, '先列出客户')
        r = sclass.class_list()
        listret1 = r.json()
        classlist1 = listret1["retlist"]
        STEP(2, '删除不存在的班级')
        r = sclass.del_class(0)
        delret = r.json()
        INFO('')
        STEP(4, '验证返回值')
        CHECK_POINT('返回的retcode值=404',
                    delret['retcode'] == 404)
        STEP(4, '检查系统数据')
        r = sclass.class_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": classlist1,
            "retcode": 0
        }

        CHECK_POINT('返回的消息体数据正确', expected == listrest)

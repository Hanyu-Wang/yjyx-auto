from lib.WEBAPI import sclass
from hyrobot.common import STEP, CHECK_POINT, INFO


class C1:
    name = 'tc000001'

    def teardown(self):
        sclass.del_class(self.addcid)

    def teststeps(self):
        STEP(1, '添加一个班级')
        r = sclass.add_class(6, '高三25班', 50)
        addret = r.json()
        self.addcid = addret['id']
        STEP(2, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(3, '检查系统数据')
        r = sclass.class_list(6)
        listrest = r.json()
        expected = {
            "gradeid": 6,
            "retlist": [
                {
                    "name": "高三25班",
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

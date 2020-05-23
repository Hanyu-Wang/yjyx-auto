from lib.API.TeacherApi import steacher
from hyrobot.common import STEP, CHECK_POINT, INFO, GSTORE
import json


class C2:
    name = 'tc000002'

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
        r = steacher.add_teacher('hwd', '汉武帝', 1, classid, '13451813456', 'jcysdf@123.com', '3209251983090987899')
        addret = r.json()
        self.addteacherid = addret['id']
        STEP(3, '验证参数返回值')
        CHECK_POINT('返回的retcode值=0',
                    addret['retcode'] == 0)
        STEP(4, '检查系统数据')
        r = steacher.teacher_list()
        listrest = r.json()
        expected = {
            "gradeid": None,
            "retlist": teacherlist + [
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
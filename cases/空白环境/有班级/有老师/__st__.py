from lib.API.TeacherApi import steacher
from hyrobot.common import GSTORE, INFO
import json


def suite_setup():
    INFO('初始化新建一个老师')
    data = [{"id": GSTORE['g_classid']}]
    classid = json.dumps(data)
    r = steacher.add_teacher('qsh', '秦始皇', 14, classid, '13451813456', 'jcysdf@123.com', '3209251983090987899')
    addret = r.json()
    GSTORE['g_teacher_id'] = addret['id']


def suite_teardown():
    steacher.del_teacher(GSTORE['g_teacher_id'])
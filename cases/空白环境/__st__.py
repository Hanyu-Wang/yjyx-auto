from lib.WEBAPI import sclass
from hyrobot.common import GSTORE, INFO


def suite_setup():
    INFO('初始化新建一个班级')
    r = sclass.add_class(6, '高三25班', 50)
    addret = r.json()
    GSTORE['g_classid'] = addret['id']


def suite_teardown():
    sclass.del_class(GSTORE['g_classid'])

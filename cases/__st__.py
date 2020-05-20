from lib.WEBAPI import sclass
from hyrobot.common import INFO


def suite_setup():
    INFO("初始化清除所有班级")
    sclass.del_all()


def suite_teardown():
    pass

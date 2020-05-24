from selenium import webdriver
from cfg.cfg import g_login_teacher
import time


class TeacherOp:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def teacher_login(self, username, password):
        self.driver.implicitly_wait(10)
        self.driver.get(g_login_teacher)
        # 登录系统
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_tag_name('button').click()

    def gethomepageinfo(self):
        self.driver.find_element_by_css_selector('a[href="#/home"]>li').click()
        time.sleep(2)
        els = self.driver.find_elements_by_css_selector('.ng-binding')
        ele = []
        for i in els:
            ele.append(i.text)
        return ele[1:]
        # return [ele.text for ele in els]

    def getclassstudentinfo_none(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('a[href="#/student_group"]>li span').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('.panel-heading>a').click()
        time.sleep(2)
        ele = self.driver.find_element_by_css_selector('.panel-body>div:nth-child(2)')
        return ele.text

    def getclassstudentinfo(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('a[href="#/student_group"]>li span').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('.panel-heading>a').click()
        time.sleep(2)
        els = self.driver.find_elements_by_css_selector('.ng-binding')
        ele = []
        for i in els:
            ele.append(i.text)
        return ele[4:]


teacherOp = TeacherOp()
if __name__ == '__main__':
    teacherOp.teacher_login('qsh', '888888')
    info = teacherOp.gethomepageinfo()
    info2 = teacherOp.getclassstudentinfo()
    print(info)
    print(info2)

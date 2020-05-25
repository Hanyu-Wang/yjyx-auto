from selenium import webdriver
from cfg.cfg import g_login_student
import time


class StudentOp:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def student_login(self, username, password):
        self.driver.implicitly_wait(10)
        self.driver.get(g_login_student)
        # 登录系统
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)

    def gethomepageinfo(self):
        self.driver.find_element_by_css_selector('a[href="#/home"]>li').click()
        time.sleep(2)
        els = self.driver.find_elements_by_css_selector(".ng-binding")
        ele = []
        for i in els:
            ele.append(i.text)
        for i in ele:
            if '注册码' in i:
                ele.remove(i)
        return ele[2:]
        # return [ele.text for ele in els]

    def getwrong_questionsinfo_none(self):
        self.driver.find_element_by_css_selector(
            'a[href="#/yj_wrong_questions"]>li'
        ).click()
        time.sleep(2)
        ele = self.driver.find_element_by_css_selector("div.row.ng-scope span")
        return ele.text

    def getwrong_questionsinfo(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            'a[href="#/student_group"]>li span'
        ).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".panel-heading>a").click()
        time.sleep(2)
        els = self.driver.find_elements_by_css_selector(".ng-binding")
        ele = []
        for i in els:
            ele.append(i.text)
        return ele[4:]


studentOp = StudentOp()
if __name__ == "__main__":
    studentOp.student_login("yuchigong", "888888")
    info = studentOp.gethomepageinfo()
    info2 = studentOp.getwrong_questionsinfo_none()
    print(info)
    print(info2)

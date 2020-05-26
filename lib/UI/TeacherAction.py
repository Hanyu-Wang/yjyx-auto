from selenium import webdriver
from cfg.cfg import g_login_teacher
import time
import random
from hyrobot.common import GSTORE


def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt


GSTORE['g_ransrt'] = ranstr(100)


class TeacherOp:

    def quit_browser(self):
        return self.driver.quit()

    def teacher_login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(g_login_teacher)
        # 登录系统
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()

    def gethomepageinfo(self):
        self.driver.find_element_by_css_selector('a[href="#/home"]>li').click()
        time.sleep(2)
        els = self.driver.find_elements_by_css_selector(".ng-binding")
        ele = []
        for i in els:
            ele.append(i.text)
        return ele[1:]
        # return [ele.text for ele in els]

    def getclassstudentinfo_none(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            'a[href="#/student_group"]>li span'
        ).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".panel-heading>a").click()
        time.sleep(2)
        ele = self.driver.find_element_by_css_selector(".panel-body>div:nth-child(2)")
        return ele.text

    def getclassstudentinfo(self):
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

    def pushtask(self):
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5) span').click()
        self.driver.find_element_by_css_selector('#btn_pick_question').click()
        time.sleep(1)
        self.driver.switch_to.frame('pick_questions_frame')
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons>button').click()
        for i in range(1, 4):
            self.driver.find_element_by_xpath(
                f'//*[@id="serach_result_table"]/div[{i}]/div[3]/div/label[2]').click()
            time.sleep(1)
        self.driver.find_element_by_css_selector('#cart_footer div.btn.btn-blue').click()
        time.sleep(2)
        # 切换回原来的iframe界面
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('exam_name_text').send_keys('发布作业')
        self.driver.find_element_by_id('btn_submit').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            '.bootstrap-dialog-footer-buttons>button:nth-child(2)').click()
        time.sleep(2)
        # 跳转到另一个窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if '下发学习任务' in self.driver.title:
                break
        self.driver.find_element_by_css_selector('body tr:nth-last-child(1) div>label').click()
        self.driver.find_element_by_css_selector('.fa.fa-check').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.btn.btn-primary').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons button').click()

    def pushtask100(self):
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5) span').click()
        self.driver.find_element_by_css_selector('#btn_pick_question').click()
        time.sleep(1)
        self.driver.switch_to.frame('pick_questions_frame')
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons>button').click()
        for i in range(1, 4):
            self.driver.find_element_by_xpath(
                f'//*[@id="serach_result_table"]/div[{i}]/div[3]/div/label[2]').click()
            time.sleep(1)
        self.driver.find_element_by_css_selector('#cart_footer div.btn.btn-blue').click()
        time.sleep(2)
        # 切换回原来的iframe界面
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('exam_name_text').send_keys(GSTORE['g_ransrt'])
        self.driver.find_element_by_id('btn_submit').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            '.bootstrap-dialog-footer-buttons>button:nth-child(1)').click()
        time.sleep(2)
        ele = self.driver.find_element_by_css_selector('div div.div-search-result-one-text')
        return ele.text

    def checktask(self):
        self.driver.find_element_by_css_selector('a[href="#/home"]>li').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('.badge.badge-blue').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#dynamicView tr:nth-child(1) td:nth-child(5) i').click()
        eles = self.driver.find_elements_by_css_selector('.ng-binding.ng-scope')
        ele = []
        for i in eles:
            ele.append(i.get_attribute('textContent'))
        val = ele[-1].strip().split(':')
        return val[0]


teacherOp = TeacherOp()
if __name__ == "__main__":
    teacherOp.teacher_login("hwd", "888888")
    teacherOp.pushtask()
#     info = teacherOp.checktask().strip()
#     print(type(info))
#     print(info)
#     if info == '正确率 0 %':
#         print('验证成功')

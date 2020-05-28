from selenium import webdriver
from cfg.cfg import g_login_teacher
import time
import random
from hyrobot.common import GSTORE
from selenium.webdriver import ActionChains


def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt


GSTORE['g_ransrt100'] = ranstr(100)
GSTORE['g_ransrt0'] = ranstr(0)
GSTORE['g_ransrt1'] = ranstr(1)


class TeacherOp:

    def quit_browser(self):
        return self.driver.quit()

    def teacher_login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(g_login_teacher)
        # 登录系统
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()

    def teacher_loginno(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(g_login_teacher)
        # 登录系统
        self.driver.find_element_by_id('username').send_keys('why')
        self.driver.find_element_by_id('password').send_keys('888888')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        ele = self.driver.find_element_by_css_selector('.bootstrap-dialog-message')
        return ele.text

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
        time.sleep(2)
        self.driver.find_element_by_css_selector('#btn_pick_question').click()
        time.sleep(1)
        self.driver.switch_to.frame('pick_questions_frame')
        # self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons>button').click()
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
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)

    def pushtaskran(self, num):
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5) span').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#btn_pick_question').click()
        time.sleep(1)
        self.driver.switch_to.frame('pick_questions_frame')
        # self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons>button').click()
        for i in range(1, 4):
            self.driver.find_element_by_xpath(
                f'//*[@id="serach_result_table"]/div[{i}]/div[3]/div/label[2]').click()
            time.sleep(1)
        self.driver.find_element_by_css_selector('#cart_footer div.btn.btn-blue').click()
        time.sleep(2)
        # 切换回原来的iframe界面
        self.driver.switch_to.default_content()
        GSTORE['g_ransrt'] = ranstr(num)
        self.driver.find_element_by_id('exam_name_text').send_keys(GSTORE['g_ransrt'])
        self.driver.find_element_by_id('btn_submit').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            '.bootstrap-dialog-footer-buttons>button:nth-child(1)').click()
        time.sleep(2)
        ele = self.driver.find_element_by_css_selector('div div.div-search-result-one-text')

        return ele.text

    def pushtask0(self, num):
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5) span').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#btn_pick_question').click()
        time.sleep(1)
        self.driver.switch_to.frame('pick_questions_frame')
        # self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons>button').click()
        for i in range(1, 4):
            self.driver.find_element_by_xpath(
                f'//*[@id="serach_result_table"]/div[{i}]/div[3]/div/label[2]').click()
            time.sleep(1)
        self.driver.find_element_by_css_selector('#cart_footer div.btn.btn-blue').click()
        time.sleep(2)
        # 切换回原来的iframe界面
        self.driver.switch_to.default_content()
        GSTORE['g_ransrt'] = ranstr(num)
        self.driver.find_element_by_id('exam_name_text').send_keys(GSTORE['g_ransrt'])
        self.driver.find_element_by_id('btn_submit').click()
        time.sleep(2)
        ele = self.driver.find_element_by_css_selector('.modal-body>div>div')
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

    def get_analysis(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('li:nth-child(9) a:nth-child(3) span').click()
        time.sleep(1)
        eles = []
        for i in range(1, 4):
            ele = self.driver.find_element_by_css_selector(f'#stats_div tr:nth-child({i}) p')
            eles.append(ele.text)
        return eles

    def get_analysis_student(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('li:nth-child(9) a:nth-child(3) span').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#stats_div tr:nth-child(1) p').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.ng-binding.collapsed>i').click()
        ele = self.driver.find_element_by_css_selector('tbody>tr>td.ng-binding')
        time.sleep(2)
        return ele.text

    def get_analysis_task(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('li:nth-child(9) a:nth-child(3) span').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#stats_div tr:nth-child(2) p').click()
        time.sleep(1)
        ele = []
        eles = self.driver.find_elements_by_css_selector('.ng-binding')
        for i in eles:
            ele.append(i.text)
        time.sleep(2)
        return ele[1:]

    def get_analysis_error(self):
        self.driver.find_element_by_xpath('//*[@id="topbar"]/div/div/ul/li[4]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('li:nth-child(9) a:nth-child(3) span').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#stats_div tr:nth-child(3) p').click()
        time.sleep(1)
        ele = self.driver.find_element_by_css_selector('.ng-binding.ng-scope')
        return ele.text

    def check_push_task(self):
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#topbar li:nth-child(5) a:nth-child(4) span').click()
        time.sleep(1)
        flag = self.isElementExist('div:nth-child(2) div.ng-scope>div')
        if flag:
            ele = self.driver.find_element_by_css_selector('div:nth-child(2) div.ng-scope>div')
            return ele.text
        else:
            ele = []
            eles = self.driver.find_elements_by_css_selector('.ng-binding')
            for i in eles:
                ele.append(i.text)
            return ele[2]

    # 判断元素是否存在的函数
    def isElementExist(self, element):
        flag = True
        try:
            self.driver.find_element_by_css_selector(element)
            return flag
        except[Exception]:
            flag = False
            return flag


teacherOp = TeacherOp()
if __name__ == "__main__":
    teacherOp.teacher_login("hwd", "888888")
    teacherOp.pushtask()
    info = teacherOp.check_push_task()
    # teacherOp.quit_browser()
    print(info)
#     info = teacherOp.checktask().strip()
#     print(type(info))
#     print(info)
#     if info == '正确率 0 %':
#         print('验证成功')

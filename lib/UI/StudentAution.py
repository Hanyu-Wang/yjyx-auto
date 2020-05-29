from selenium import webdriver
from cfg.cfg import g_login_student
import time


class StudentOp:

    def quit_browser(self):
        return self.driver.quit()

    # 判断元素是否存在的函数
    def isElementExist(self, element):
        flag = True
        try:
            self.driver.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag

    def student_login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(g_login_student)
        # 登录系统
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)

    def student_loginno(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(g_login_student)
        # 登录系统
        self.driver.find_element_by_id("username").send_keys('why')
        self.driver.find_element_by_id("password").send_keys('888888')
        self.driver.find_element_by_tag_name("button").click()
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

    def submittask(self):
        self.driver.find_element_by_css_selector('a[href="#/task_manage"]>li').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#page-wrapper td:nth-child(7) > button').click()
        time.sleep(1)
        for i in range(1, 4):
            self.driver.find_element_by_css_selector(
                f'#exam_question_list_choice > div > div > div:nth-child({i}) button:nth-child(1)').click()
            time.sleep(1)
        self.driver.find_element_by_css_selector('#page-wrapper div.col-lg-12.ng-scope > button').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons button:nth-child(2)').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#page-wrapper div:nth-child(4) > div > img').click()
        ele = self.driver.find_element_by_css_selector('.col-lg-12.pull-left.ng-scope > span:nth-child(4)')
        return ele.text

    def getMyTask(self):
        self.driver.find_element_by_css_selector('a[href="#/task_manage"]>li').click()
        time.sleep(2)
        flag = self.isElementExist('div:nth-child(2) div.ng-scope')
        if flag:
            ele = self.driver.find_element_by_css_selector('div:nth-child(2) div.ng-scope')
            return ele.text
        else:
            ele = []
            eles = self.driver.find_elements_by_css_selector('td.ng-binding')
            for i in eles:
                ele.append(i.text)
            return ele[1:3]

    def get_statistics_info(self):
        self.driver.find_element_by_css_selector('a[href="#/stats"]>li').click()
        time.sleep(2)
        flag = self.isElementExist('div:nth-child(2) div.ng-scope')
        if flag:
            ele = self.driver.find_element_by_css_selector('div:nth-child(2) div.ng-scope')
            return ele.text
        else:
            ele = []
            eles = self.driver.find_elements_by_css_selector('td.ng-binding')
            for i in eles:
                ele.append(i.text)
            return ele

    def get_Personal_Info(self):
        self.driver.find_element_by_css_selector('li:nth-child(2) span.ng-binding').click()
        self.driver.find_element_by_css_selector('a[href="#/user_info"]').click()
        time.sleep(1)
        flag = self.isElementExist('.list-group>li')
        if flag:
            ele = self.driver.find_element_by_css_selector('.list-group>li')
            return ele.text
        else:
            ele = []
            eles = self.driver.find_elements_by_css_selector('label.ng-binding')
            time.sleep(2)
            for i in eles:
                ele.append(i.text)
            return ele[:6]

    def modify_user_info(self):
        self.driver.find_element_by_css_selector('li:nth-child(2) span.ng-binding').click()
        self.driver.find_element_by_css_selector('a[href="#/user_info"]').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('a[href="/#tab_two"]').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('form>div:nth-child(1) input').clear()
        self.driver.find_element_by_css_selector('form>div:nth-child(1) input').send_keys('三板斧')
        time.sleep(2)
        self.driver.find_element_by_css_selector('a.btn.btn-orange.show-ico-btn').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('a:nth-child(42)>img').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#tab_two button').click()
        ele = self.driver.find_element_by_css_selector('.bootstrap-dialog-message')
        time.sleep(2)
        self.driver.find_element_by_css_selector('.btn.btn-default').click()
        return ele.text


studentOp = StudentOp()
if __name__ == "__main__":
    info = studentOp.student_loginno()
    print(info)

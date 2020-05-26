*** Settings ***

Library  有班级、学生、老师UI.py   WITH NAME  M

Library  有班级、学生、老师UI.C22   WITH NAME  C22

Library  有班级、学生、老师UI.C23   WITH NAME  C23



*** Test Cases ***

tc005101
  [Teardown]  C22.teardown

  C22.teststeps


tc005104
  [Teardown]  C23.teardown

  C23.teststeps

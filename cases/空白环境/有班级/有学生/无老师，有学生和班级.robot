*** Settings ***

Library  无老师，有学生和班级.py   WITH NAME  M

Library  无老师，有学生和班级.C20   WITH NAME  C20



*** Test Cases ***

tc005002
  [Teardown]  C20.teardown

  C20.teststeps

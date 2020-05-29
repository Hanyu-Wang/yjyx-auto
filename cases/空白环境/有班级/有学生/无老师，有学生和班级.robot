*** Settings ***

Library  无老师，有学生和班级.py   WITH NAME  M

Library  无老师，有学生和班级.C20   WITH NAME  C20

Library  无老师，有学生和班级.C57   WITH NAME  C57

Library  无老师，有学生和班级.C58   WITH NAME  C58

Library  无老师，有学生和班级.C59   WITH NAME  C59

Library  无老师，有学生和班级.C60   WITH NAME  C60

Library  无老师，有学生和班级.C61   WITH NAME  C61

Library  无老师，有学生和班级.C62   WITH NAME  C62

Library  无老师，有学生和班级.C63   WITH NAME  C63

Library  无老师，有学生和班级.C64   WITH NAME  C64



*** Test Cases ***

tc000020
  [Teardown]  C20.teardown

  C20.teststeps


tc000057
  [Teardown]  C57.teardown

  C57.teststeps


tc000058
  [Teardown]  C58.teardown

  C58.teststeps


tc000059
  [Teardown]  C59.teardown

  C59.teststeps


tc000060
  [Teardown]  C60.teardown

  C60.teststeps


tc000061
  [Teardown]  C61.teardown

  C61.teststeps


tc000062
  [Teardown]  C62.teardown

  C62.teststeps


tc000063
  [Teardown]  C63.teardown

  C63.teststeps


tc000064
  [Teardown]  C64.teardown

  C64.teststeps

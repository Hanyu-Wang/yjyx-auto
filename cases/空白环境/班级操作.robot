*** Settings ***

Library  班级操作.py   WITH NAME  F

Library  班级操作.C1   WITH NAME  C1



*** Test Cases ***

tc000001
  [Teardown]  C1.teardown

  C1.teststeps

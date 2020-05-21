*** Settings ***

Library  空白-班级API.py   WITH NAME  F

Library  空白-班级API.C1   WITH NAME  C1

Library  空白-班级API.C7   WITH NAME  C7



*** Test Cases ***

tc000001
  [Teardown]  C1.teardown

  C1.teststeps


tc000081

  C7.teststeps

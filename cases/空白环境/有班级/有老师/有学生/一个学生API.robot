*** Settings ***

Library  一个学生API.py   WITH NAME  M

Library  一个学生API.C17   WITH NAME  C17

Library  一个学生API.C18   WITH NAME  C18



*** Test Cases ***

tc002002
  [Teardown]  C17.teardown

  C17.teststeps


tc002081

  C18.teststeps

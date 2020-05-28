*** Settings ***

Library  一个学生API.py   WITH NAME  M

Library  一个学生API.C17   WITH NAME  C17

Library  一个学生API.C18   WITH NAME  C18

Library  一个学生API.C26   WITH NAME  C26

Library  一个学生API.C27   WITH NAME  C27

Library  一个学生API.C28   WITH NAME  C28

Library  一个学生API.C29   WITH NAME  C29

Library  一个学生API.C30   WITH NAME  C30



*** Test Cases ***

tc000017
  [Teardown]  C17.teardown

  C17.teststeps


tc000018

  C18.teststeps


tc000026

  C26.teststeps


tc000027

  C27.teststeps


tc000028
  [Teardown]  C28.teardown

  C28.teststeps


tc000029
  [Teardown]  C29.teardown

  C29.teststeps


tc000030

  C30.teststeps

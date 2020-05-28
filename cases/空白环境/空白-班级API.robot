*** Settings ***

Library  空白-班级API.py   WITH NAME  M

Library  空白-班级API.C1   WITH NAME  C1

Library  空白-班级API.C7   WITH NAME  C7

Library  空白-班级API.C31   WITH NAME  C31

Library  空白-班级API.C32   WITH NAME  C32

Library  空白-班级API.C33   WITH NAME  C33

Library  空白-班级API.C34   WITH NAME  C34



*** Test Cases ***

tc000001
  [Teardown]  C1.teardown

  C1.teststeps


tc000007

  C7.teststeps


tc000031
  [Teardown]  C31.teardown

  C31.teststeps


tc000032
  [Teardown]  C32.teardown

  C32.teststeps


tc000033

  C33.teststeps


tc000034

  C34.teststeps

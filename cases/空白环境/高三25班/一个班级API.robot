*** Settings ***

Library  一个班级API.py   WITH NAME  F

Library  一个班级API.C2   WITH NAME  C2

Library  一个班级API.C3   WITH NAME  C3

Library  一个班级API.C4   WITH NAME  C4

Library  一个班级API.C5   WITH NAME  C5

Library  一个班级API.C6   WITH NAME  C6

Library  一个班级API.C8   WITH NAME  C8

Library  一个班级API.C9   WITH NAME  C9



*** Test Cases ***

tc000002
  [Teardown]  C2.teardown

  C2.teststeps


tc000003

  C3.teststeps


tc000051
  [Teardown]  C4.teardown

  C4.teststeps


tc000052
  [Teardown]  C5.teardown

  C5.teststeps


tc000053
  [Teardown]  C6.teardown

  C6.teststeps


tc000082

  C8.teststeps


tc001001
  [Teardown]  C9.teardown

  C9.teststeps

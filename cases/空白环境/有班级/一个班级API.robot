*** Settings ***

Library  一个班级API.py   WITH NAME  M

Library  一个班级API.C2   WITH NAME  C2

Library  一个班级API.C3   WITH NAME  C3

Library  一个班级API.C4   WITH NAME  C4

Library  一个班级API.C5   WITH NAME  C5

Library  一个班级API.C6   WITH NAME  C6

Library  一个班级API.C8   WITH NAME  C8

Library  一个班级API.C9   WITH NAME  C9

Library  一个班级API.C35   WITH NAME  C35

Library  一个班级API.C36   WITH NAME  C36

Library  一个班级API.C37   WITH NAME  C37

Library  一个班级API.C39   WITH NAME  C39

Library  一个班级API.C40   WITH NAME  C40

Library  一个班级API.C41   WITH NAME  C41

Library  一个班级API.C42   WITH NAME  C42

Library  一个班级API.C43   WITH NAME  C43



*** Test Cases ***

tc000002
  [Teardown]  C2.teardown

  C2.teststeps


tc000003

  C3.teststeps


tc000004
  [Teardown]  C4.teardown

  C4.teststeps


tc000005
  [Teardown]  C5.teardown

  C5.teststeps


tc000006
  [Teardown]  C6.teardown

  C6.teststeps


tc000008

  C8.teststeps


tc000009
  [Teardown]  C9.teardown

  C9.teststeps


tc000035
  [Teardown]  C35.teardown

  C35.teststeps


tc000036
  [Teardown]  C36.teardown

  C36.teststeps


tc000037
  [Teardown]  C37.teardown

  C37.teststeps


tc000039

  C39.teststeps


tc000040
  [Teardown]  C40.teardown

  C40.teststeps


tc000041

  C41.teststeps


tc000042
  [Teardown]  C42.teardown

  C42.teststeps


tc000043
  [Teardown]  C43.teardown

  C43.teststeps

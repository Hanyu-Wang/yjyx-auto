*** Settings ***

Library  一个老师API.py   WITH NAME  M

Library  一个老师API.C10   WITH NAME  C10

Library  一个老师API.C11   WITH NAME  C11

Library  一个老师API.C12   WITH NAME  C12

Library  一个老师API.C13   WITH NAME  C13

Library  一个老师API.C14   WITH NAME  C14

Library  一个老师API.C15   WITH NAME  C15

Library  一个老师API.C16   WITH NAME  C16



*** Test Cases ***

tc001002
  [Teardown]  C10.teardown

  C10.teststeps


tc001003

  C11.teststeps


tc001051

  C12.teststeps


tc001052
  [Teardown]  C13.teardown

  C13.teststeps


tc001081

  C14.teststeps


tc001082

  C15.teststeps


tc002001
  [Teardown]  C16.teardown

  C16.teststeps

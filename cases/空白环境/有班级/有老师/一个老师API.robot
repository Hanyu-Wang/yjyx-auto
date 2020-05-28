*** Settings ***

Library  一个老师API.py   WITH NAME  M

Library  一个老师API.C10   WITH NAME  C10

Library  一个老师API.C11   WITH NAME  C11

Library  一个老师API.C12   WITH NAME  C12

Library  一个老师API.C13   WITH NAME  C13

Library  一个老师API.C37   WITH NAME  C37

Library  一个老师API.C38   WITH NAME  C38

Library  一个老师API.C14   WITH NAME  C14

Library  一个老师API.C15   WITH NAME  C15

Library  一个老师API.C16   WITH NAME  C16



*** Test Cases ***

tc000010
  [Teardown]  C10.teardown

  C10.teststeps


tc000011

  C11.teststeps


tc000012

  C12.teststeps


tc000013
  [Teardown]  C13.teardown

  C13.teststeps


tc000037
  [Teardown]  C37.teardown

  C37.teststeps


tc000038
  [Teardown]  C38.teardown

  C38.teststeps


tc000017

  C14.teststeps


tc000015

  C15.teststeps


tc000016
  [Teardown]  C16.teardown

  C16.teststeps

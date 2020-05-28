*** Settings ***

Library  空白环境UI.py   WITH NAME  M

Library  空白环境UI.C44   WITH NAME  C44

Library  空白环境UI.C45   WITH NAME  C45



*** Test Cases ***

tc000044
  [Teardown]  C44.teardown

  C44.teststeps


tc000045
  [Teardown]  C45.teardown

  C45.teststeps

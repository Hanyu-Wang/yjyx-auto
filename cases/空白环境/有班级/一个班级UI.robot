*** Settings ***

Library  一个班级UI.py   WITH NAME  M

Library  一个班级UI.C19   WITH NAME  C19

Library  一个班级UI.C21   WITH NAME  C21



*** Test Cases ***

tc005001
  [Teardown]  C19.teardown

  C19.teststeps


tc005081
  [Teardown]  C21.teardown

  C21.teststeps

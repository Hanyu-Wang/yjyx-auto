*** Settings ***

Library  有班级、学生、老师UI.py   WITH NAME  M

Library  有班级、学生、老师UI.C22   WITH NAME  C22

Library  有班级、学生、老师UI.C23   WITH NAME  C23

Library  有班级、学生、老师UI.C24   WITH NAME  C24

Library  有班级、学生、老师UI.C25   WITH NAME  C25

Library  有班级、学生、老师UI.C46   WITH NAME  C46

Library  有班级、学生、老师UI.C47   WITH NAME  C47

Library  有班级、学生、老师UI.C48   WITH NAME  C48

Library  有班级、学生、老师UI.C49   WITH NAME  C49

Library  有班级、学生、老师UI.C50   WITH NAME  C50

Library  有班级、学生、老师UI.C51   WITH NAME  C51

Library  有班级、学生、老师UI.C52   WITH NAME  C52

Library  有班级、学生、老师UI.C53   WITH NAME  C53

Library  有班级、学生、老师UI.C54   WITH NAME  C54

Library  有班级、学生、老师UI.C55   WITH NAME  C55

Library  有班级、学生、老师UI.C56   WITH NAME  C56

Library  有班级、学生、老师UI.C65   WITH NAME  C65



*** Test Cases ***

tc000022
  [Teardown]  C22.teardown

  C22.teststeps


tc000023
  [Teardown]  C23.teardown

  C23.teststeps


tc000024
  [Teardown]  C24.teardown

  C24.teststeps


tc000025
  [Teardown]  C25.teardown

  C25.teststeps


tc000046
  [Teardown]  C46.teardown

  C46.teststeps


tc000047
  [Teardown]  C47.teardown

  C47.teststeps


tc000048
  [Teardown]  C48.teardown

  C48.teststeps


tc000049
  [Teardown]  C49.teardown

  C49.teststeps


tc000050
  [Teardown]  C50.teardown

  C50.teststeps


tc000051
  [Teardown]  C51.teardown

  C51.teststeps


tc000052
  [Teardown]  C52.teardown

  C52.teststeps


tc000053
  [Teardown]  C53.teardown

  C53.teststeps


tc000054
  [Teardown]  C54.teardown

  C54.teststeps


tc000055
  [Teardown]  C55.teardown

  C55.teststeps


tc000056
  [Teardown]  C56.teardown

  C56.teststeps


tc000065
  [Teardown]  C65.teardown

  C65.teststeps

*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/variables.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Site Administrator can access settings page
    Login in as role 'Administrators'
     Open the control panel
     Page Should Contain  Collective Mobify.js settings

Mobify.js meta element resize_url is in page
    Go to  ${PLONE_URL}
     Page has meta element with name 'mobify:resize_url' and value '//cdn.mobify.com/mobifyjs/build/mobify-2.0.5.min.js'

Set different resize_url and backend_url and check meta elements
    Open settings page
    Input text  form.widgets.mobify_library_url  EXAMPLE_URL
    Input text  form.widgets.mobify_resize_backend  EXAMPLE_BACKEND
    Click Button  Save
    Go to  ${PLONE_URL}
    Page has meta element with name 'mobify:resize_url' and value 'EXAMPLE_URL'
    Page has meta element with name 'mobify:resize_backend' and value 'EXAMPLE_BACKEND'

Test if mobify.js is working
    Login in as role 'Administrators'
    Open example page
    Page has logo loaded from Mobify.js
    Pause


*** Keywords ***

Login in as role '${ROLE}'
    Enable autologin as  ${ROLE}
    Go to  ${PLONE_URL}

Open the control panel
    Click link  css=dl#portal-personaltools dt.actionMenuHeader a
    Click Link  link=Site Setup

Page has meta element with name ${name} and value ${value}
    Page should contain element  xpath=//meta[@name=${name} and @content=${value}]

Open settings page
   Go to  ${PLONE_URL}/@@collective.mobifyjs-settings

Open example page
   Go to  ${PLONE_URL}/test-mobifyjs

Page has logo loaded from Mobify.js
   Page should contain element  xpath=//img[@src='//ir0.mobify.com/project-oss-localhost/1080/https://plone.org/logo.png']



*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/variables.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Test if mobify.js is working
    Example page has logo loaded from Mobify.js

Site Administrator can access settings page
    Login in as role 'Administrators'
     Open the control panel
     Page Should Contain  Collective Mobify.js settings

Mobify.js meta element resize_url is in page
     Page source should contain one meta element with default values

Set different resize_url and backend_url and check meta elements
    Set example values in settings page
     Page source should contain two meta elements with example values


*** Keywords ***

Login in as role '${ROLE}'
    Enable autologin as  ${ROLE}
    Go to  ${PLONE_URL}

Open the control panel
    Click link  css=dl#portal-personaltools dt.actionMenuHeader a
    Click Link  link=Site Setup

Page source should contain meta element with name ${name} and value ${value}
    Page should contain element  xpath=//meta[@name=${name} and @content=${value}]

Page source should contain one meta element with default values
    Go to  ${PLONE_URL}
    Page source should contain meta element with name 'mobify:resize_url' and value '//cdn.mobify.com/mobifyjs/build/mobify-2.0.5.min.js'

Page source should contain two meta elements with example values
     Page source should contain meta element with name 'mobify:resize_url' and value 'EXAMPLE_URL'
     Page source should contain meta element with name 'mobify:resize_backend' and value 'EXAMPLE_BACKEND'

Open settings page
   Go to  ${PLONE_URL}/@@collective.mobifyjs-settings

Set example values in settings page
   Open settings page
     Input text  form.widgets.mobify_library_url  EXAMPLE_URL
     Input text  form.widgets.mobify_resize_backend  EXAMPLE_BACKEND
     Click Button  Save

Example page has logo loaded from Mobify.js
   Go to  ${PLONE_URL}/test-mobifyjs
   Page should contain element  xpath=//img[@src='//ir0.mobify.com/project-oss-localhost/1080/https://plone.org/logo.png']



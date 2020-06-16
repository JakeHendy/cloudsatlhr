Feature: CloudsAtLHR Push System

    Scenario: Daily update
        Given a user has subscribed to the daily update
        When the email is generated
        Then all articles in the past 24 hours are included in the email

    Scenario: Friday update
        Given a user has subscribed to the Friday update
        When the email is generated
        Then all articles in the past 7 days are included in the email

    Scenario: MWF Update
        Given a user has subscribed to the MWF Update
        When the email is generated
        Then all articles since the past email update are included in the email

    Scenario: Login to Subscription Management 
        Given the user is not authenticated
        When the user visits the login page
        Then they are given the option to login with email
        And they are given the option to login with Google
        And they are given the option to login with Microsot
        And they are given the option to login with Apple

    Scenario: Visit login when authenticated
        Given the user is authenticated
        When the user visits the login page
        Then they are redirected to the management page

    Scenario: Subscription Management whilst authenticated
        Given the user is authenticated
        When the user loads the management page
        Then they are able to change the frequency of their email

    Scenario: Subscription Management whilst unauthenticated
        Given the user is not authenticated
        When the user loads the management page
        Then they are redirected to the login page
        
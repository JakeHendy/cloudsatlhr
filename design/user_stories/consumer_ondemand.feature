Feature: CloudsAtLHR On Demand

    A web interface that allows users to view stories and content on line.

    Scenario: Viewing the homepage
        Given a user visits the homepage
        When the page is rendered
        Then there is a list of categories 
        And the 10 most recent articles are displayed in summary form

    Scenario: Viewing all articles for a category
        Given a user has clicked on a category
        When the page is rendered
        Then the 10 most recent articles are displayed in summary form
        And the results are paginated

    Scenario: Viewing a single article
        Given a user has clicked on an article
        When the page is rendered
        Then the article is fully rendered with no page breaks
        And the 3 most recent articles are displayed in summary form

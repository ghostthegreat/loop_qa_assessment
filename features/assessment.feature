Feature: Verify tasks and tags in Asana

  Background:
    Given I am logged into Asana

  Scenario: Verify "Draft project brief" in the "To do" column
    When I navigate to "Cross-functional project plan, Project"
    Then I should see "Draft project brief" in the "To do" column
    And it should have the tags:
      | Non-Priority |
      | On track     |

  Scenario: Verify "Schedule kickoff meeting" in the "To do" column
    When I navigate to "Cross-functional project plan, Project"
    Then I should see "Schedule kickoff meeting" in the "To do" column
    And it should have the tags:
      | Medium  |
      | At risk |

  Scenario: Verify "Share timeline with teammates" in the "To do" column
    When I navigate to "Cross-functional project plan, Project"
    Then I should see "Share timeline with teammates" in the "To do" column
    And it should have the tags:
      | High      |
      | Off track |

  Scenario: Verify "[Example] Laptop setup for new hire" in the "New Requests" column
    When I navigate to "Work Requests"
    Then I should see "[Example] Laptop setup for new hire" in the "New Requests" column
    And it should have the tags:
      | Medium priority |
      | Low effort      |
      | New hardware    |
      | Not Started     |

  Scenario: Verify "[Example] Password not working" in the "In Progress" column
    When I navigate to "Work Requests"
    Then I should see "[Example] Password not working" in the "In Progress" column
    And it should have the tags:
      | Low effort    |
      | Low priority  |
      | Password reset|
      | Waiting       |

  Scenario: Verify "[Example] New keycard for Daniela V" in the "Completed" column
    When I navigate to "Work Requests"
    Then I should see "[Example] New keycard for Daniela V" in the "Completed" column
    And it should have the tags:
      | Low effort    |
      | New hardware  |
      | High Priority |
      | Done          |

*** Settings ***
Documentation
...     *UNCLASSIFIED//CUI*
...
...     === Health Test Suite ===
...     MICROSOFT_WORKSTATION_health_tests

...     === Test Suite Description ===
...     Tests for using various keywords

...     === Test Suite Notes ===
...     This is a test stub only, and is meant to be used as a template for other test scripts


Force Tags              health      microsoft_workstation


Library                         TafCoreLibrary
Library                         TafMicrosoftWorkstationLibrary


Suite Setup                     Test Suite Setup
Suite Teardown                  Test Suite Teardown


*** Variables ***
${MSG}      This is a Health Test Case stub, and is meant to be used as a template for other test scripts.   WARN
${RETURN_SUCCESS}               200


*** Test Cases ***
Health Test Case
    [Documentation]
    ...     === Test Name ===
    ...     Health Test Case
    ...
    ...     === Test Purpose ===
    ...     N/A

    ...     === Description ===
    ...     | *Field*                       | *Entry*                |
    ...     | *Current Classification*      | UNCLASSIFIED//CUI      |
    ...     | *Test Type*                   | Health                 |
    ...     | *Brief Decription*            |     |
    ...     | *Enclave*                     |     |
    ...     | *Scenario File Name (*zip)*   |     |
    ...     | *Scenario Description*        |     |

    ...     === Pass/Fail Crieria ===
    ...     N/A

    ...     === Test Case Notes ===
    ...     N/A

    Log     ${MSG}

    Verify Health Status    none        200     ${RETURN_SUCCESS}


*** Keywords ***
# -----------------------------------------------------------------------------------------
# -------------------------------  Custom Suite Keywords ----------------------------------
# This is the area where custom Keywords are defined.

# Verify Health Status is a custom keyword that was created to provide the ability to reuse
# high-level keywords from existing keywords.
Verify Health Status
    [Arguments]     ${req_num}      ${response}     ${expected}

    # This keyword verifies that ``${response}`` equals ``${expected}``.
    REQMNT Verify Requirement   ${req_num}  VERIFY Operation On Values  ${response}  eq  ${expected}


# -----------------------------------------------------------------------------------------
# ----------------------  Test Suite Setup and Teardown Keywords --------------------------
Test Suite Setup
    Log         Setup

Test Suite Teardown
    Log         Teardown

# -----------------------------------------------------------------------------------------
# ----------------------  Test Case Setup and Teardown Keywords ---------------------------
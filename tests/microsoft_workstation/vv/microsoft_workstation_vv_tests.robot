*** Settings ***
Documentation
...     *UNCLASSIFIED//CUI*
...
...     === V&V Test Suite ===
...     MICROSOFT_WORKSTATION_vv_tests

...     === Test Suite Description ===
...     Tests for using various keywords

...     === Test Suite Notes ===
...     This is a test stub only, and is meant to be used as a template for other test scripts


Force Tags              vv      microsoft_workstation


Library                         TafCoreLibrary
Library                         TafMicrosoftWorkstationLibrary


Suite Setup                     Test Suite Setup
Suite Teardown                  Test Suite Teardown


*** Variables ***
${MSG}      This is a V&V Case stub, and is meant to be used as a template for other test scripts.   WARN


*** Test Cases ***
VV Test Case
    [Documentation]
    ...     === Test Name ===
    ...     VV Test Case
    ...
    ...     === Test Purpose ===
    ...     N/A

    ...     === Description ===
    ...     | *Field*                       | *Entry*                |
    ...     | *Current Classification*      | UNCLASSIFIED//CUI      |
    ...     | *Test Type*                   | Verification and Validation |
    ...     | *Brief Decription*            |     |
    ...     | *Enclave*                     |     |
    ...     | *Scenario File Name (*zip)*   |     |
    ...     | *Scenario Description*        |     |

    ...     === Pass/Fail Crieria ===
    ...     N/A

    ...     === Test Case Notes ===
    ...     N/A

    Log     ${MSG}



*** Keywords ***
# -----------------------------------------------------------------------------------------
# -------------------------------  Custom Suite Keywords ----------------------------------
# This is the area where custom Keywords are defined.


# -----------------------------------------------------------------------------------------
# ----------------------  Test Suite Setup and Teardown Keywords --------------------------
Test Suite Setup
    Log         Setup

Test Suite Teardown
    Log         Teardown

# -----------------------------------------------------------------------------------------
# ----------------------  Test Case Setup and Teardown Keywords ---------------------------

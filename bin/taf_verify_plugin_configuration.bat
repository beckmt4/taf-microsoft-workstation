REM  This is a plugin specific test for TAF MICROSOFT_WORKSTATION,
REM  this script is meant to be run from taf_verify_configuration.bat in TAF CORE
REM  rather than standalone.

ECHO.
ECHO.
ECHO RUNNING TAF-MICROSOFT-WORKSTATION CONFIGURATION CHECK
REM  Add functionality to verify functionality of the plugin
ECHO WARNING: THIS IS JUST A STUB WITH NO CURRENT FUNCTIONALITY
REM  Currently this acts as a template and does not verify anything
ECHO.
ECHO.

SET MICROSOFT_WORKSTATION_CHECKS_PASSED=1


IF NOT %MICROSOFT_WORKSTATION_CHECKS_PASSED%==1 (
    ECHO.
    ECHO ERROR: ONE OR MORE OF TAF MICROSOFT_WORKSTATION CONFIG CHECKS FAILED!!!
    ECHO.
    EXIT /B 1
) ELSE (
    ECHO.
    ECHO TAF MICROSOFT_WORKSTATION CONFIG CHECK SUCCESS!!!
    ECHO.
    EXIT /B 0
)
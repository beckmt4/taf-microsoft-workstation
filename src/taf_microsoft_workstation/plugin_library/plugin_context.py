
"""
The purpose of this module is to allow for keyword libraries and other context values using a 
"self.keywordid_keywords." or "self.variable_name" syntax.  Type hinting can be added to permit
intelli-sense dot expansion of properties and methods of the context values.
"""

# Selenium is not provided with the TAF minimum installer
# and must be separately installed within a TAF Add-on.
try:
    from SeleniumLibrary.errors import NoOpenBrowser
except (ModuleNotFoundError, ImportError, NotImplementedError):
    pass


from robot.libraries.BuiltIn import BuiltIn

# Import classes used only for type references.
do_import = False
if do_import:
    # Skip import errors for non-TAF imports by ignoring (ModuleNotFoundError, ImportError) errors.
    # These are used for type hinting during development and errors at run time are not relevant.
    try:
        from SSHLibrary import SSHLibrary
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass
    try:
        from SeleniumLibrary import SeleniumLibrary
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass
    try:
        from SeleniumLibrary.keywords.webdrivertools import WebDriverCache
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass
    try:
        from selenium.webdriver.firefox.webdriver import WebDriver
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass
    try:
        import uiautomation
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass
    try:
        from TafCoreLibrary import TafCoreLibrary
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass
    try:
        from taf_core.plugin_library.plugin_keyword_library_components \
            import TafKeywordLibraryComponents as TafCoreKeywordLibraryComponents
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass

    # TAF Core keyword module imports.
    try:
        from taf_app.log.logger import RobotLogger
        from taf_app.properties.common_properties import CommonProperties
    except (ModuleNotFoundError, ImportError, NotImplementedError):
        pass

    from TafMicrosoftWorkstationLibrary import TafMicrosoftWorkstationLibrary


class TafContextAware(object):

    def __init__(self, ctx):
        """Base class exposing attributes from the common context.

        :param ctx: The library itself as a context object.
        :type ctx: taf.TafCoreLibrary
        """
        self.ctx: TafMicrosoftWorkstationLibrary = ctx

    @property
    def taf_core_library(self):  # type: () -> TafCoreLibrary
        instance = None
        error = ""

        try:
            instance = BuiltIn().get_library_instance("TafCoreLibrary")
        except Exception as ex:
            error = ex

        if instance is None:
            try:
                instance = BuiltIn().import_library("TafCoreLibrary")
            except Exception as ex:
                error = ex

        if instance is None:
            self.logger.exception(f"TafCoreLibrary could not be imported: {error}")

        return instance

    @property
    def taf_core_keywords(self): # type: () -> TafCoreKeywordLibraryComponents
        """
        The wrapped keywords for TafCoreLibrary
        """
        return self.taf_core_library.taf_keywords

    @property
    def logger(self):   # type: () -> RobotLogger
        return self.ctx._logger

    @property
    def props(self):  # type: () -> CommonProperties
        return self.ctx._props

    # -----------------------------------------------------------------------------------
    # SSHLibrary context properties
    # -----------------------------------------------------------------------------------
    @property
    def ssh_library(self):  # type: () -> SSHLibrary
        """
        The wrapped keywords for SeleniumLibrary
        """
        return self.ssh_library_instance

    @property
    def ssh_library_instance(self):  # type: () -> SSHLibrary
        """
        This instance allows for TAF to access the drivers object of the SeleniumLibrary.
        """
        instance = None
        error = ""

        try:
            instance = BuiltIn().get_library_instance("SSHLibrary")
        except Exception as ex:
            error = ex

        if instance is None:
            try:
                instance = BuiltIn().import_library("SSHLibrary")
            except Exception as ex:
                error = ex

        if instance is None:
            self.logger.exception(f"SSHLibrary could not be imported: {error}")

        return instance

    # -----------------------------------------------------------------------------------
    # Selenium context properties
    # -----------------------------------------------------------------------------------
    @property
    def selenium_library(self):  # type: () -> SeleniumLibrary
        """
        The wrapped keywords for SeleniumLibrary
        """
        return self.selenium_library_instance

    @property
    def selenium_library_instance(self):  # type: () -> SeleniumLibrary
        """
        This instance allows for TAF to access the drivers object of the SeleniumLibrary.
        """
        instance = None
        error = ""

        try:
            instance = BuiltIn().get_library_instance("SeleniumLibrary")
        except Exception as ex:
            error = ex

        if instance is None:
            try:
                instance = BuiltIn().import_library("SeleniumLibrary")
            except Exception as ex:
                error = ex

        if instance is None:
            self.logger.exception(f"SeleniumLibrary could not be imported: {error}")

        return instance

    @property
    def implicit_wait(self):  # type: () -> float
        """
        The valued by various Selenium functions to track the TAF selenium timeout value.
        """
        return self.selenium_library.get_selenium_implicit_wait()

    @property
    def drivers(self):   # type: () -> WebDriverCache
        """
        The drivers object of the SeleniumLibrary instance.
        """
        return self.selenium_library_instance._drivers

    @property
    def driver(self):  # type: () -> WebDriver
        """Current active driver that is active in the SeleniumLibrary.

        :rtype: selenium.webdriver.remote.webdriver.WebDriver
        :raises SeleniumLibrary.errors.NoOpenBrowser: If browser is not open.
        """

        if not self.selenium_library_instance._drivers.current:
            raise NoOpenBrowser('No browser is open.')

        try:
            # Try to find the driver based on the current user profile.
            self.selenium_library_instance._drivers.switch(self.taf_core_library.users.current_user.firefox_driver_alias)
        except RuntimeError as runtime_error:
            # No user driver was found for the user profile.  So, just return the
            # current driver.  This could happen if the SeleniumLibrary.Open Browser keyword was used.
            pass

        return self.selenium_library_instance._drivers.current
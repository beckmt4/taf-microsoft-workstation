# -*- coding: utf-8 -*-
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

import pathlib
import os

# =======================================================================================
# Robot framework imports
# ---------------------------------------------------------------------------------------
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from robot.running.model import TestCase as TestCaseRunning
from robot.running.model import TestSuite as TestSuiteRunning
from robot.result.model import TestCase as TestCaseResult
from robot.result.model import TestSuite as TestSuiteResult
from robot.libraries.BuiltIn import RobotNotRunningError
from robot.running.timeouts import TestTimeout
from robotlibcore import DynamicCore

# =======================================================================================
# TAF imports
# ---------------------------------------------------------------------------------------

from taf_microsoft_workstation.version import version as plugin_version
from taf_microsoft_workstation.plugin_library.plugin_keyword_library_components import TafKeywordLibraryComponents

from taf_app.log.logger import RobotLogger, FacadeLogger
from taf_app.properties.common_properties import CommonProperties
from taf_app.robot_resource.resource_imports_finder import ResourceImportsFinder


from taf_app.properties.get_props import get_python_properties


class TafMicrosoftWorkstationLibrary(DynamicCore):

    ROBOT_LIBRARY_SCOPE = 'SUITE'
    ROBOT_LIBRARY_VERSION = plugin_version
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(
            self,
            run_on_failure_keyword=None,
            test_case_timeout_minutes=None,
            import_resource_keywords=True,
            running_robot=True
        ):

        # Initializing the base class should always be the first statement
        DynamicCore.__init__(self, [])

        self.running_robot = running_robot

        # Setup values that help with resource files
        self.plugin_library_name = "TafMicrosoftWorkstationLibrary"
        self.plugin_name = "taf-microsoft-workstation"
        self.plugin_src_directory = pathlib.Path(__file__).parent.absolute()
        self.plugin_keywords_src_name = "taf_microsoft_workstation"
        self.plugin_property_name_prefix = "taf.microsoft.workstation"
        self.plugin_keywords_src_directory = os.path.join(self.plugin_src_directory, self.plugin_keywords_src_name)

        # TAF context properties
        self._props = get_python_properties()

        # Create the logger
        if self.running_robot:
            self._logger = RobotLogger(self._props.get_property('taf.app.logging.screenshots.directory'))
        else:
            self._logger = FacadeLogger()

        # Check the library parameters
        if str(import_resource_keywords).lower() == 'true':
            self.import_resource_keywords = True
        else:
            self.import_resource_keywords = False

        if test_case_timeout_minutes is not None:
            self.test_case_timeout_minutes = test_case_timeout_minutes
        else:
            self.test_case_timeout_minutes = f"{self._props.get_property('taf.app.robot.run.testcase.timeout.minutes')} minutes"

        self.run_on_failure_keyword_parameter = None

        if run_on_failure_keyword is not None:
            self.run_on_failure_keyword = run_on_failure_keyword
            self.run_on_failure_keyword_parameter = run_on_failure_keyword
        else:
            self.run_on_failure_keyword = self._props.get_property("taf.microsoft.workstation.logging.keyword.library.run.on.failure.keyword")

        self._running_on_failure_keyword = False
        
        # Prepare the keywords modules for use in the DynamicCore base class
        self.taf_keywords: TafKeywordLibraryComponents = TafKeywordLibraryComponents(self)

        # Class modules to include in the library that will share an instance of this class as the context.
        # This allows all classes that inherit from LibraryComponent to share the same ssh sessions,
        # log library, properties, etc
        self.libraries = []
        self._plugin_keywords = []
        self.libraries.extend(self.taf_keywords.libraries)

        # Initialize the library with all the LibraryComponents
        DynamicCore.__init__(self, self.libraries)

        # This line enables a lot of cool Robot Framework functionality
        # It allows us to define methods in this library class (examples below) like _end_suite that will
        # do whatever we want after every suite is executed.  For more information, see this link:
        # http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface
        # and for specifically using custom libraries as listeners, see this sub-section:
        # http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-libraries-as-listeners
        self.ROBOT_LIBRARY_LISTENER = self

        self.resource_imports_finder = None

        if self.import_resource_keywords:
            # Initialize the resource imports finder
            self.resource_imports_finder = ResourceImportsFinder(
                self.props,
                self._logger,
                plugin_library_name=self.plugin_library_name,
                plugin_name=self.plugin_name,
                plugin_src_directory=self.plugin_src_directory,
                plugin_keywords_src_name = self.plugin_keywords_src_name,
                plugin_keywords_src_directory = self.plugin_keywords_src_directory
            )

    @property
    def props(self):  # type: () -> CommonProperties
        return self._props

    def set_run_on_failure_keyword(self, run_on_failure_keyword=None):
        if run_on_failure_keyword is None:
            if self.run_on_failure_keyword_parameter is not None:
                self.run_on_failure_keyword = self.run_on_failure_keyword_parameter
            else:
                # Rest the failure keyword to default value
                self.run_on_failure_keyword = self._props.get_property(
                    "taf.microsoft.workstation.logging.keyword.library.run.on.failure.keyword")
        else:
            self.run_on_failure_keyword = run_on_failure_keyword

        self._logger.info(f"Run on failure keyword was set: {self.run_on_failure_keyword}")

    def run_keyword(self, name: str, args: tuple, kwargs: dict):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            self.failure_occurred()
            raise

    def get_keyword_tags(self, name: str) -> list:
        tags = list(DynamicCore.get_keyword_tags(self, name))
        if name in self._plugin_keywords:
            tags.append("plugin")
        return tags

    def get_keyword_documentation(self, name: str) -> str:
        return DynamicCore.get_keyword_documentation(self, name)

    def failure_occurred(self):
        if self._running_on_failure_keyword or not self.run_on_failure_keyword:
            return
        try:
            self._running_on_failure_keyword = True
            BuiltIn().run_keyword(self.run_on_failure_keyword)
        except Exception as err:
            logger.warn("Keyword '%s' could not be run on failure: %s"
                        % (self.run_on_failure_keyword, err))
        finally:
            self._running_on_failure_keyword = False

    # ===================================================================================
    # Robot test event handlers
    # -----------------------------------------------------------------------------------
    def end_suite(self, data: TestSuiteRunning, result: TestSuiteResult):
        pass

    def start_suite(self, data: TestSuiteRunning, result: TestSuiteResult):
        if self.import_resource_keywords:
            for resource_path in self.resource_imports_finder.resource_file_path_list:
                BuiltIn().import_resource(resource_path)

    def start_test(self, data: TestCaseRunning, result: TestCaseResult):
        pass

    def end_test(self, data: TestCaseRunning, result: TestCaseResult):
        pass


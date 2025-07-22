# -*- coding: utf-8 -*-

# Defines class that includes the keywords that will be included into the
# test framework.

# Components imports
from taf_microsoft_workstation.example_microsoft_workstation_component.example_microsoft_workstation_keywords import TafMicrosoftWorkstationExampleKeywords


# This class can be named anything, but the suggested name format is
# {Plugin_name}KeywordLibraryComponents where:
#      {Plugin_name} = name of plugin (ex: TafCore, TafDcgsn, Acs)
class TafKeywordLibraryComponents(object):
    def __init__(self, ctx):

        self.ctx = ctx

        # Add an instance of each keyword class to the "self" of this class
        self.example_keywords = TafMicrosoftWorkstationExampleKeywords(ctx)

        # Add each of these references to the list of libraries that should be
        # included in the library.  The method "add_libraries" is not bound
        # until run time.
        self.libraries = [
            self.example_keywords,
        ]


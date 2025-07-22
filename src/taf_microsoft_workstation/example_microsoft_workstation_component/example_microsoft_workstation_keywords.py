# -*- coding: utf-8 -*-

# Example MICROSOFT_WORKSTATION keywords

import time

from taf_microsoft_workstation.robot_library import LibraryComponent, keyword


# Keyword id for this help document
keyword_id = "EXAMPLE"
# Keyword id description is the description that displays in the table of
# keyword id's on the API launch page.
keyword_id_description = "Example Component"
# This filename is the name of the API page for this keyword id
keyword_doc_filename = keyword_id

# Keyword id help docstring.  Fill this docstring in with the help for the
# specific keyword id.  If left blank, then a default will be provided.
keyword_doc = """
Keyword documentation for interaction with EXAMPLE.
"""

main_keyword_class = True

class TafMicrosoftWorkstationExampleKeywords(LibraryComponent):

    @keyword(name="EXAMPLE Microsoft Workstation Keyword One")
    def example_microsoft_workstation_keyword_one(self):
        """
        This is a example keyword.
        """
        print("HERE I AM ONE")

    @keyword(name="EXAMPLE Microsoft Workstation Keyword Two")
    def example_microsoft_workstation_keyword_two(self):
        """
        This is another example keyword.
        """
        print("HERE I AM TWO")

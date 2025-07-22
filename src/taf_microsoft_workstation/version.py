# -*- coding: utf-8 -*-

import os
from xml.etree import ElementTree as et

def get_pom_version() -> str:
    pom_version: str = ""

    try:
        pom_file_path = os.path.join(os.path.normpath(os.path.expandvars("$TAF_MICROSOFT_WORKSTATION_HOME")), "pom.xml")

        ns = "http://maven.apache.org/POM/4.0.0"
        et.register_namespace('', ns)
        tree = et.ElementTree()
        tree.parse(pom_file_path)
        p = tree.getroot().find("{%s}version" % ns)
        pom_version = p.text
    except Exception as e:
        pom_version = "UNDEFINED"

    return pom_version


version = get_pom_version()


if __name__ == "__main__":
    print("Version: {version}".format(version=version))





#!/usr/bin/env bash
#
# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

# The path to output all built .py files to:
UI_PYTHON_PATH=./../widgets/ui
# The path to where the PySide binaries are installed
#PYTHON_BASE="D:/my_dev/pythonProject/facecap_frontend/venv"
#PYSIDE_BASE="${PYTHON_BASE}/Lib/site-packages/PySide"
#PYTHON="${PYTHON_BASE}/Scripts/python"

# Remove any problematic profiles from pngs.
#for f in *.png; do mogrify $f; done

# Helper functions to build UI files
function build_qt {


    "$1" "$2" > $UI_PYTHON_PATH/$3.py

#    # replace PySide imports with tank.platform.qt and remove line containing Created by date
#    sed -i $UI_PYTHON_PATH/$5.py -e "s/from PySide import/from tank.platform.qt import/g" -e "/# Created:/d"
}

function build_ui {
    build_qt "PySide6-uic.exe" "$1.ui" "$1"
}

# build UI's:
echo "building user interfaces..."
build_ui editor_view
build_ui stream_pane
# add any additional .ui files you want converted here!

#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2017, The Sumokoin Project (www.sumokoin.org)
## Copyright (c) 2018, The Fonero Project (www.fonero.org)
'''
App main function
'''

import sys, os, hashlib
from PySide import QtCore

from PySide.QtGui import QMessageBox

from app.QSingleApplication import QSingleApplication
from utils.common import DummyStream, getAppPath, readFile
from settings import APP_NAME

from app.hub import Hub
from webui import MainWebUI

file_hashes = [
        ('www/scripts/mustache.min.js', '3258bb61f5b69f33076dd0c91e13ddd2c7fe771882adff9345e90d4ab7c32426'),
        ('www/scripts/jquery.qrcode.min.js', 'f4ccf02b69092819ac24575c717a080c3b6c6d6161f1b8d82bf0bb523075032d')
    ]

def _check_file_integrity(app):
    ''' Check file integrity to make sure all resources loaded
        to webview won't be modified by an unknown party '''
    for file_name, file_hash in file_hashes:
        file_path = os.path.normpath(os.path.join(app.property("ResPath"), file_name))
        if not os.path.exists(file_path):
            return False
        data = readFile(file_path)
#         print( file_path, hashlib.sha256(data).hexdigest() )
        if hashlib.sha256(data).hexdigest() != file_hash:
            return False
        
    return True


def main():
    if getattr(sys, "frozen", False) and sys.platform in ['win32','cygwin','win64']:
        # and now redirect all default streams to DummyStream:
        sys.stdout = DummyStream()
        sys.stderr = DummyStream()
        sys.stdin = DummyStream()
        sys.__stdout__ = DummyStream()
        sys.__stderr__ = DummyStream()
        sys.__stdin__ = DummyStream()
              
    # Get application path
    app_path = getAppPath()
    if sys.platform == 'darwin' and hasattr(sys, 'frozen'):
        resources_path = os.path.normpath(os.path.abspath(os.path.join(app_path, "..", "Resources")))
    else:
        resources_path = os.path.normpath(os.path.abspath(os.path.join(app_path, "Resources")))
        
    # Application setup
    
    app = QSingleApplication(sys.argv)
    app.setOrganizationName('Fonero')
    app.setOrganizationDomain('www.fonero.org')
    app.setApplicationName(APP_NAME)
    app.setProperty("AppPath", app_path)
    app.setProperty("ResPath", resources_path)
    if sys.platform == 'darwin':
        app.setAttribute(QtCore.Qt.AA_DontShowIconsInMenus)
        
    if not _check_file_integrity(app):
        QMessageBox.critical(None, "Application Fatal Error", """<b>File integrity check failed!</b>
                <br><br>This could be a result of unknown (maybe, malicious) action<br> to wallet code files.""")
        app.quit()
    else:
        hub = Hub(app=app)
        ui = MainWebUI(app=app, hub=hub, debug=False)
        hub.setUI(ui)
        app.singleStart(ui)
        
        sys.exit(app.exec_())
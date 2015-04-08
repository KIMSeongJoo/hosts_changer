# -*- coding: utf-8 -*-

import sys
import os
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser
from PyQt4 import QtGui #, QtCore
from ui import main
from ui.settings import path

# global variables
CONFIG_FILE='hosts_changer.cfg'
USER_HOME_DIR = os.path.expanduser('~')
HOSTS_FILE = 'hosts'
HOSTS_DEFAULT_DIR = USER_HOME_DIR + '/Desktop/hosts/'

# host changer
class HostsChanger():
    config = None

    def __init__(self):
        self.init()

    def init(self):
        self.loadConfig()

    def loadConfig(self):
        self.config = ConfigParser.SafeConfigParser(allow_no_value=True)
        return self.config.read(CONFIG_FILE)

    def writeConfig(self):
        with open(CONFIG_FILE, 'w') as configfile:
            return self.config.write(configfile)

    def getHostsDir(self):
        try:
            hosts = self.config.get('hosts', 'path')
            if len(hosts) > 0: hosts = hosts.rstrip('/') + '/'
        except: hosts = HOSTS_DEFAULT_DIR

        return hosts

    def setHostsDir(self, hostsDir):
        try: self.config.add_section('hosts')
        except: pass
        finally: self.config.set('hosts', 'path', str(hostsDir))

        return True

    def getHostsList(self):
        path = self.getHostsDir()
        try:
            for item in os.listdir(path):
                if os.path.isdir(os.path.join(path, item)): continue
                yield item
        except:
            pass

    def readLink(self):
        if not self._existsLink(): return ''

        return os.readlink(self._getHostsLinkDir() + HOSTS_FILE)

    def changeHosts(self, hosts):
        curHosts = self.readLink()
        if curHosts != hosts:
            if curHosts != '': self._unlink()
            self._symlink(hosts)

        return True

    def _getHostsLinkDir(self):
        return USER_HOME_DIR + '/'

    def _existsLink(self):
        return os.path.islink(self._getHostsLinkDir() + HOSTS_FILE)

    def _unlink(self):
        return os.unlink(self._getHostsLinkDir() + HOSTS_FILE)

    def _symlink(self, hosts):
        return os.symlink(self.getHostsDir() + hosts, self._getHostsLinkDir() + HOSTS_FILE)

# main window
class MainWindow(QtGui.QMainWindow, main.Ui_MainWindow):
    hostsChanger = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self._centerOnScreen()
        self._connect()
        self.init()

    def init(self):
        self.hostsChanger = HostsChanger()
        self._setPathLable()
        self._setHostsLable()
        self._setHostsList()
        
    def _centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move(resolution.width()/2 - self.frameSize().width()/2, resolution.height()/2 - self.frameSize().height()/2)

        return True

    def _connect(self):
        self.hostsChangeButton.clicked.connect(self._change)
        self.refreshListButton.clicked.connect(self._setHostsList)
        self.hostsList.doubleClicked.connect(self._openEditor)
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionPath.triggered.connect(self._showPathWindow)

    def _setPathLable(self):
        return self.hostsPathLabel.setText(' ' + self.hostsChanger.getHostsDir())

    def _setHostsLable(self):
        self.hostsLine.setText(self.hostsChanger.readLink())

    def _setHostsList(self):
        hostsListModel = QtGui.QStandardItemModel(self.hostsList)
        curHosts = self.hostsChanger.readLink()
        hostsDir = self.hostsChanger.getHostsDir()
        listIdx = 0;
        curHostsListIdx = None

        for name in self.hostsChanger.getHostsList():
            item = QtGui.QStandardItem(name)
            hostsListModel.appendRow(item)
            if curHosts == (hostsDir + name): curHostsListIdx = listIdx
            listIdx += 1

        if listIdx == 0: self.hostsChangeButton.setEnabled(False)
        else: self.hostsChangeButton.setEnabled(True)

        self.hostsList.setModel(hostsListModel)
        if curHostsListIdx is not None: self.hostsList.setCurrentIndex(hostsListModel.index(curHostsListIdx, 0))

        return True

    def _getSelectedListItem(self):
        hosts = ''
        for item in self.hostsList.selectedIndexes(): hosts = item.data()

        return hosts

    def _change(self):
        self.hostsChanger.changeHosts(self._getSelectedListItem())
        self._setHostsLable()
        
    def _openEditor(self):
        os.system('kwrite ' + self.hostsChanger.getHostsDir() + self._getSelectedListItem() + ' &')

    def _showPathWindow(self):
        childWindow = SettingsPathWindow(self)
        childWindow.show()

# settings -> path window
class SettingsPathWindow(QtGui.QMainWindow, path.Ui_PathDialog):
    mainWindow = None

    def __init__(self, parent=None):
        super(SettingsPathWindow, self).__init__(parent)
        self.mainWindow = parent

        self.setupUi(self)
        self._centerOnScreen()
        self._connect()
        self.init()

    def init(self):
        self.mainWindow.hostsChanger.loadConfig()
        self.hostsDir.setText(self.mainWindow.hostsChanger.getHostsDir())

    def accept(self):
        self.mainWindow.hostsChanger.setHostsDir(self.hostsDir.text())
        self.mainWindow.hostsChanger.writeConfig()
        self.close()
        self.mainWindow.init()

    def reject(self):
        self.close()

    def _centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move(resolution.width()/2 - self.frameSize().width()/2, resolution.height()/2 - self.frameSize().height()/2)

        return True

    def _connect(self):
        pass

# main
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

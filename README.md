# QT-based Hosts changer - Python
<p align="center"><img src="https://github.com/parkjy76/hosts_changer/blob/master/images/hosts_changer.png"></p>
* QT based
* list of hosts files
* change, reload button
* define Hosts files' directory in settings of menu
* double-click to edit hosts in list-box

## Limitation
* No support Windows
* Only a user who have administrative rights is able to use hosts changer because you need to link at /etc/hosts.  
and hosts changer link selected hosts file to ~[USER]/hosts. see hosts_changer.py  
ex) ln -s ~[USER]/hosts /etc/hosts

## Requirements
* Python 3.X
* PyQT
* Qt Designer (Optional) - design GUI and convert to .py

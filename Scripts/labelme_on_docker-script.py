#!c:\users\administrator.sky-20120726ujy\desktop\qinzhen\python_workspace\python3\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'labelme==4.2.10','console_scripts','labelme_on_docker'
__requires__ = 'labelme==4.2.10'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('labelme==4.2.10', 'console_scripts', 'labelme_on_docker')()
    )

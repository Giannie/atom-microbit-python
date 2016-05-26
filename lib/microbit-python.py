from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import sys
import os
install = False
base_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(base_path, 'python'))
if len(sys.argv) >= 2 and sys.argv[1] == '--install':
    install_only = True
else:
    install_only = False
try:
    import uflash
except:
    install = True

if __name__ == '__main__':
    if install:
        uflash_link = "https://raw.githubusercontent.com/ntoll/uflash/e3eeb6504089963683f4cc141bba8901752cef8d/uflash.py"
        try:
            from urllib.request import urlopen
        except:
            from urllib import urlopen
        resp = urlopen(uflash_link)
        text = resp.read()
        install_dir = os.path.join(base_path, 'python')
        if not os.path.isdir(install_dir):
            os.mkdir(install_dir)
        with open(os.path.join(install_dir, 'uflash.py'), 'wb') as f:
            f.write(text)
            f.flush()
        print('Local uflash installed')
        try:
            import uflash
        except:
            pass
    if not install_only:
        uflash.main(sys.argv[1:])

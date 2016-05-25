from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import sys
install = False
try:
    import uflash
except:
    try:
        sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'python'))
        import uflash
    except:
        install = True

if __name__ == '__main__':
    if install:
        uflash_link = "https://pypi.python.org/packages/64/11/b9fb282500746d2d28765b6d5b8034c7339c80766c40bccc350e563d9894/uflash-1.0.0.tar.gz"
        try:
            from urllib.request import urlretrieve
        except:
            from urllib import urlretrieve
        import tarfile
        import os
        local_filename, headers = urlretrieve(uflash_link)
        uflash_tar = tarfile.open(name=local_filename)
        uflash_member = uflash_tar.getmember('uflash-1.0.0/uflash.py')
        uflash_member.name = 'python/uflash.py'
        install_path = os.path.dirname(os.path.realpath(__file__))
        uflash_tar.extract(uflash_member, path=install_path)
        sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'python'))
        import uflash
    uflash.main(sys.argv[1:])

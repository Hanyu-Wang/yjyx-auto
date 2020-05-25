import os,sys,pprint
#is_64bits = sys.maxsize > 2**32
#
#
#if not os.path.exists('hyrobot/core.pyd'):
#    from shutil import copyfile
#    if is_64bits:
#        copyfile('hyrobot/core.cp37-win_amd64.pyd', 'hyrobot/core.pyd')
#    else:        
#        copyfile('hyrobot/core.cp37-win32.pyd', 'hyrobot/core.pyd')

if not  (3, 6,0) <= sys.version_info < (3, 9,0) :
    print("黑羽robot只支持 Python 3.6、3.7、3.8 版本")
    exit()

from core import main
result = main()
pprint.pprint(result)
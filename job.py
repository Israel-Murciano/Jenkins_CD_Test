#!/usr/bin/env python3

import os.path
import os
from zipfile import ZipFile

testArry = ["1", "2", "3"]
testENV = os.environ['VERSION']

for i in list: 
    f= open("{}.txt".format(i),"w+")

for i in list:
    try:
        os.path.isfile("{}.txt".format(i))
    except Exception:
        quit()

for i in list:
    zipObj = ZipFile('{}+{}.zip'.format(i, testENV), 'w')
    zipObj.write("{}.txt".format(i))
    zipObj.close()

for i in list:
    try:
        os.path.isfile('{}+{}.zip'.format(i, testENV))
    except Exception:
        quit()
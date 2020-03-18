#!/usr/bin/python3

'''
-- Created by IntelliJ IDEA.
-- User: ProjectSky
-- Date: 2017/7/3
-- Time: 13:41
-- Check all json file encoding & syntax.
'''

import os
import sys
import os.path
import json
import pathlib

rootdir = "../translations"


def getFileExt(f):
    ext = pathlib.PurePosixPath(f).suffix
    return ext

def scanAllFile():
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if getFileExt(filename) == '.json' or getFileExt(filename) == '.patch':
                with open(os.path.join(parent, filename), 'r', encoding='utf-8') as f:
                    try:
                        json.load(f)
                    except ValueError as e:
                        print('[FAIL] ' + os.path.join(parent, filename) + ' 校验失败, 错误信息: ' + str(e))
                        sys.exit(1)

scanAllFile()
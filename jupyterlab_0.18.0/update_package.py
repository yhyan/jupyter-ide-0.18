#!/usr/bin/env python
#coding:utf-8

import os
import json
from collections import OrderedDict

CURDIR = os.path.dirname(os.path.abspath(__file__))

packages_dir = os.path.join(CURDIR, "packages")

def main():
    # print("hello world")
    ff = os.listdir(packages_dir)
    ret = {}
    for f in ff:
        with open(os.path.join(packages_dir, f, "package.json")) as fp:
            data = json.loads(fp.read())
        # print(data["dependencies"])
        ret.update(data["dependencies"])
    ret2 = OrderedDict()
    for k in sorted(ret.keys()):
        ret2[k] = ret[k]
    print(json.dumps(ret2, indent=True))
if __name__ == "__main__":
    main()
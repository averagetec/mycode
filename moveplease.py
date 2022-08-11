#!/usr/bin/env python3
#import statements

import shutil
import os

def main():
    #start in the home user directory
    os.chdir("/home/student/mycode/")

    #call shutil move
    shutil.move("raynor.obj", "ceph_storage/")

    #ask user for new name of kerrigan obj
    xname = input("What is the new name for kerrigan.obj?")

    shutil.move("ceph_storage/new obj", "ceph_storage/" + xname)

main()

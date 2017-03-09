#!/bin/env python 
# -*- coding: utf-8 -*-
 
import pexpect
from   config import *
  
child = pexpect.spawn (TARGET_SERVER)

child.expect   ('[Nn]ame .*: ')
child.sendline (TARGET_USER)

child.expect   ('[Pp]assword:')
child.sendline (TARGET_PASS)

child.expect   ('ftp> ')
child.sendline ('ls /pub/')
child.expect   ('ftp> ')

print child.before

child.sendline ('bye')
child.close()

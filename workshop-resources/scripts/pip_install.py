# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may
# not use this file except in compliance with the License. A copy of the License is located at
#
#        http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.

import pip
import logging
import sys
from subprocess import call
from subprocess import PIPE, run

def pipinstall():
    fname = "requirements.txt"
    with open(fname) as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            result=run("pip3 install " + line +" --no-deps", shell=True, stdout=PIPE, stderr=PIPE, text=True)
            if result.returncode == 0:
                next
            elif result.returncode == 1:
                errormsg=result.stderr
                error_lines = errormsg.split('\n')
                for line in error_lines:
                    if line.startswith("ERROR: No"):
                        print (line)
f = open('errors.txt', 'w')
sys.stdout = f
pipinstall()

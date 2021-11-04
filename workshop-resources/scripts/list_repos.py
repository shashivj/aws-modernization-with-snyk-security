# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may
# not use this file except in compliance with the License. A copy of the License is located at
# http://aws.amazon.com/apache2.0/
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
# This script essentially performs a pip freeze on a specified AWS CodeArtifact Repository
# Environment variables have to be set for the domainName, domainOwner & repository
# Currently only supports python repositories

import boto3
import sys
import os
from datetime import datetime

from botocore.exceptions import ClientError
client = boto3.client('codeartifact')

##############
# Parameters #
##############
# Get the environment variables 
domainName = os.environ.get('domainName')
domainOwner = os.environ.get('domainOwner')
repo = os.environ.get('repository')
pkgformat = 'pypi'
fname = 'requirements.txt'

#############
# Main Code #
#############

def getPackages():  
    response = client.list_packages(
    domain=domainName,
    domainOwner=domainOwner,
    repository=repo,
    format=pkgformat,
    maxResults=1000,
)
    for item in response.get('packages'):   
        pname = (item.get('package'))
        getVersion(pname)

def getVersion(pname):
    response = client.list_package_versions(
    domain=domainName,
    domainOwner=domainOwner,
    repository=repo,
    format=pkgformat,
    package=pname,
    )
    
    version = response.get('defaultDisplayVersion')
    #Added a retry as sometimes this parameter evaluates to none even when the version does exist
    if version == 'none':
        getVersion(pname)
    else:
        print (pname+"=="+version)
    
# Open file and set std out to write to file
f = open(fname, 'w')
sys.stdout = f

getPackages()
print("\n")

f.close()

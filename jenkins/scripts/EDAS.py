#!/usr/bin/env python
#coding=utf-8
import sys,os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from common import Common
from time import gmtime, strftime
import oss2

accessKeyId,accessKeySecret,endpoint,region,appid,ossbucketname,ossendpoint,securityToken = Common.LoadConfig()

client = AcsClient(accessKeyId, accessKeySecret, region)

def upload_war(warfilepath):
    auth = oss2.Auth(accessKeyId, accessKeySecret)
    bucket = oss2.Bucket(auth, ossendpoint, ossbucketname)

    oss2.resumable_upload(bucket, os.path.basename(warfilepath), warfilepath)
    
    warurl = "https://"+ossbucketname+"."+ossendpoint+"/"+os.path.basename(warfilepath)
    
    return warurl


def deploy(warurl):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_domain(endpoint)
    request.set_version('2017-08-01')

    packageversion=strftime("%Y%m%d%H%M%S", gmtime())

    request.add_query_param('RegionId', region)
    request.add_query_param('AppId',appid )
    request.add_query_param('PackageVersion',packageversion)
    request.add_query_param('DeployType','url')
    request.add_query_param('WarUrl',warurl)
    request.add_query_param('GroupId','all')
    #request.set_uri_pattern('/pop/v5/app/app_status')
    request.set_uri_pattern('/pop/v5/changeorder/co_deploy')
    body = ''''''
    response = ''
    request.set_content(body)

    response = client.do_action(request)

    # python2:  
    print(response) 
    #print(str(response, encoding = 'utf-8'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python EDAS.py warfilepath")
        sys.exit(1)
 
    print ('Using war url ', sys.argv[1])
    print (os.path.basename(sys.argv[1]))
    warobjecturl = upload_war(sys.argv[1])
    print (warobjecturl)
    deploy(warobjecturl)
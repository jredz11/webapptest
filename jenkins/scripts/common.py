#!/usr/bin/env python
#coding=utf8
import sys
import os
import time
import configparser

class Common:

    @staticmethod
    def LoadConfig():
        cfg_fn = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/edas.cfg")
        required_ops = [("Base", "AccessKeyId"), ("Base", "AccessKeySecret"), ("Base", "Endpoint"), ("Base", "Region"), ("Base", "AppId"), ("Base", "OSSBucketName"), ("Base", "OSSEndpoint")]
        optional_ops = [("Optional", "SecurityToken")]

        parser = configparser.ConfigParser()
        parser.read(cfg_fn)
        for sec,op in required_ops:
            if not parser.has_option(sec, op):
                sys.stderr.write("ERROR: need (%s, %s) in %s.\n" % (sec,op,cfg_fn))
                sys.stderr.write("Read README to get help inforamtion.\n")
                sys.exit(1)

        accessKeyId = parser.get("Base", "AccessKeyId")
        accessKeySecret = parser.get("Base", "AccessKeySecret")
        endpoint = parser.get("Base", "Endpoint")
        region = parser.get("Base", "Region")
        appid = parser.get("Base", "AppId")
        ossbucketname = parser.get("Base", "OSSBucketName")
        ossendpoint = parser.get("Base", "OSSEndpoint")
        securityToken = ""
        if parser.has_option("Optional", "SecurityToken") and parser.get("Optional", "SecurityToken") != "$SecurityToken":
            securityToken = parser.get("Optional", "SecurityToken")
            return accessKeyId,accessKeySecret,endpoint,region,appid,ossbucketname,ossendpoint,securityToken

        return accessKeyId,accessKeySecret,endpoint,region,appid,ossbucketname,ossendpoint,""

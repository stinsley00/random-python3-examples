#!/usr/bin/env python3
#                ___,,___
#            _,-='=- =-  -`"--.__,,.._
#         ,-;// /  - -       -   -= - "=.
#       ,'///    -     -   -   =  - ==-=\`.
#      |/// /  =    `. - =   == - =.=_,,._ `=/|
#     ///    -   -    \  - - = ,ndDMHHMM/\b  \\
#   ,' - / /        / /\ =  - /MM(,,._`YQ\    `|
#  <_,=^Kkm / / / / ///H|wnWWdMKKK#""-;. `\X  X|
#         `""QkmmmmmnWMMM\""WHMKKMM\   `--. \  \
#  rabidBadger      `""'  `->>>    ``WHMb,. -_<@)
#  @author stinsley           `"QMM`.         ""
#                                    `>>>     ..

import logging
import traceback
from os import environ
import boto3
import base64
from botocore.exceptions import ClientError
import json
import time
import datetime
import re

jSecret = dict()
secret = ''
decoded_binary_secret=''



logger=logging.getLogger()
logger.setLevel(logging.INFO)

endpoint=''
port=''
dbuser=''
password=''
database=''
cert=environ.get('###')


def log_err(errmsg):
    logger.error(errmsg)
    return {"body": errmsg , "headers": {}, "statusCode": 400,
        "isBase64Encoded":"false"}

logger.info("Cold start complete.") 

def lambda_handler(event, context):

    jSecret1 = get_secret() #need ssl cert verification fixed to impl

<REDACTED> 

    if event is None:
        query = "select schema.get_schedule('{}','{}')".format(d, r)
    else:
        regex = re.compile("rec[1-3]")
        dregex= re.compile("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]")
        r = event['params']['querystring']['param1']
        d = event['params']['querystring']['param2']
        if(regex.match(r) and dregex.match(d)):
            query = "select schema.get_schedule('{}', '{}')".format(d, r)
        else: 
            return log_err ("ERROR: ...\n")

    try:
        cnx = make_connection(...)
        cursor=cnx.cursor()

        try:
            cursor.execute(query)
        except:
            return log_err ("ERROR: Cannot execute cursor.\n{}".format(
                traceback.format_exc()) )

        try:
            final = str()
            x = str()
            for result in cursor:
                x += json.dumps(result)[1:-1]

            info = json.loads(x, encoding=json)
            for field, possible_values in info.items():
                for i in possible_values:

                    if('flex' in i):
                        if(i['flex'] != {}):
                            if(i['flex']['addRow'] in 'false'):
                                i['flex']['addRow'] = False
                            elif(i['flex']['addRow'] in 'true'):
                                i['flex']['addRow'] = True
                            if(i['flex']['removeRow'] in 'false'):
                                i['flex']['removeRow'] = False
                            elif(i['flex']['removeRow'] in 'true'):
                                i['flex']['removeRow'] = True
            final = json._default_encoder.encode(info)
            final_json = json._default_decoder.decode(final)
        except:
            return log_err ("ERROR: Cannot retrieve query data.\n{}".format(
                traceback.format_exc()))

        return final_json
    except:
        return log_err("ERROR: Cannot connect to database from handler.\n{}".format(
            traceback.format_exc()))


    finally:
        try:
            cnx.close()
        except:
            pass
def make_connection(endpoint,database,dbuser,password, port):

<REDACTED> 

def get_secret():
<REDACTED> 
    )
    try:
        print('trying secret:\n')
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            jSecret = json.loads(secret)
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            jSecret = json.loads(decoded_binary_secret)
    return jSecret

#lambda_handler(None, None)
#!/usr/bin/env python3
#   AWS LAMBDA EXAMPLE TO 
#   1) retrieve creds from a secrets manager
#   2) query a PL/SQL function
#   3) return data to aws api gateway 
# 
#   @author stinsley
#
import psycopg2
import logging
import traceback
from os import environ
import boto3
import base64
from botocore.exceptions import ClientError
import json
import time


#initialization 
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
#get an environment variable called 'DBCERT' from the lambda to retrieve the security certification
cert=environ.get('<REDACTED>')


def log_err(errmsg):
    logger.error(errmsg)
    return {"body": errmsg , "headers": {}, "statusCode": 400,
        "isBase64Encoded":"false"}

logger.info("Cold start complete.") 

#this is what lambda looks for when instanciating the code
def lambda_handler(event, context):

    jSecret1 = get_secret() #need ssl cert verification fixed to impl

    endpoint=jSecret1['host']
    port=jSecret1['port']
    dbuser=jSecret1['username']
    password=jSecret1['password']
    database=jSecret1['dbname']
    query = "select public.get_staffing_schedule('{}')".format(event['date'])

    try:
        cnx = make_connection(endpoint, database, dbuser, password, port)
        cursor=cnx.cursor()

        try:
            cursor.execute(query)
        except:
            return log_err ("ERROR: Cannot execute cursor.\n{}".format(
                traceback.format_exc()) )

        try:
            results_list=[]
            for result in cursor: results_list.append(result)
            print(results_list)
            cursor.close()

        except:
            return log_err ("ERROR: Cannot retrieve query data.\n{}".format(
                traceback.format_exc()))


        return {"body": str(results_list), "headers": {}, "statusCode": 200,
        "isBase64Encoded":"false"}

    
    except:
        return log_err("ERROR: Cannot connect to database from handler.\n{}".format(
            traceback.format_exc()))


    finally:
        try:
            cnx.close()
        except:
            pass

#make a postgres connection and return it        
def make_connection(endpoint,database,dbuser,password, port):

    conn_str="host={0} dbname={1} user={2} password={3} port={4} sslmode='verify-full' sslrootcert={5}".format(
        endpoint,database,dbuser,password,port, cert)
    print(conn_str)
    conn = psycopg2.connect(conn_str)
    conn.autocommit=True
    return conn 


   <REDACTED CODE>
        if 'SecretString' in get_secret_value_response:
            <REDACTED CODE>
    return jSecret

# uncomment if you want make this run outside of lambda for testing
#if __name__== "__main__":

    #lambda_handler(None,None)
#
#  "._`-.         /\-.
#    '-.`;.--.___/ _`>
#       `"( )    , )
#          \\----\-\
#    ~~~~~~ "" ~~ """ ~~~~~~~
#    datafox
#
#   @author stinsley
#   This program reads a xls by worksheet, creates a pandas dataframe, modifies the dataframe and imports the data to postgres. 
#   Once the data is in postgres this calls postgres procedures to transform the data. 
#   input: the file name you'd like to import
#   usage: python3 progname.py '~/Documents/data/myxls.xls' 
#   notes: xlsx is supported by this program  


#define imports 
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker
import pandas as pd
import configparser
import os
from os import sys
import hashlib, binascii, os
from cryptography.fernet import Fernet
import logging

#parse config file
def ConfigSectionMap(section):
    
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            #logging.warning("exception on %s!" % option)
            dict1[option] = None
    return dict1

def getPasswd(password_link):
    <redacted> 

Config = configparser.ConfigParser()
Config.read(r"C:\..\..\..\..\config.ini")

inpath = ConfigSectionMap("inlink")['file_input_link']
outpath = ConfigSectionMap("outlink")['file_output_link']
pathtopw = ConfigSectionMap("passwordfile")['pass_link']
connection_str = ConfigSectionMap("dbconnection")['connection_str']
dbschema = ConfigSectionMap("dbconnection")['dbschema']
log_dir = ConfigSectionMap("log_files")['log_dir']
log_lvl = ConfigSectionMap("log_files")['log_level']
headers = ConfigSectionMap("file_headers")['header_map']
#header_map = dict(i.split(':') for i in headers.split(','))

#options section
pd.options.mode.use_inf_as_na = True
#define vars and such
connection_str = connection_str.format(getPasswd(pathtopw))

< REDACTED > 

def move_files(path_from, path_to):
    os.rename(path_from, path_to)




def transfromations(min_case_id): 
    print('calling transformations')
    try: 
        connection = engine.raw_connection()
        cursor = connection.cursor()
        result = cursor.execute('call transform_raw_data({})'.format(min_case_id))
        connection.commit()
    finally:
        connection.close()

    try: 
        connection = engine.raw_connection()
        cursor = connection.cursor()
        result = cursor.execute('call Create_ref_tables()')
        connection.commit()
    finally:
        connection.close()
    
    try: 
        connection = engine.raw_connection()
        cursor = connection.cursor()
        result = cursor.execute('call Begin_transforms()')
        connection.commit()
    finally:
        connection.close()
    
    try: 
        connection = engine.raw_connection()
        cursor = connection.cursor()
        result = cursor.execute('call Create_Display()')
        connection.commit()
    finally:
        connection.close()


def import_data(path):
    #finds and excel workbook, imports it
    # Set up of the table in db and the file to import
    tableToWriteTo = 'date_intake_2'
    sheets_dict = pd.read_excel(path, dtype = str, sheet_name=None)
    df = pd.DataFrame()
    #print(sheets_dict)

    for name, sheet in sheets_dict.items():
        print(name)
        #print(sheet)
        if(name == 'Sheet1'):
            s1 = pd.read_excel(path, dtype = str, sheet_name='Sheet1', headers=0)
            cols = s1.columns
            print(cols)
            df = df.append(s1)
        
        else:
            sheet.columns = cols
            print(cols)
            df = df.append(sheet, sort = False)
   
   # df.reset_index(inplace=True, drop=True)
   # df.rename(columns=header_map, inplace=True)
    print(df)
    #Mods to the DF here. change headers for my sql friendly headers
    
    df['Date'] = df.Date.astype('str')
    #make NaTs and NaNs postgres compatible
<REDACTED> 

    print(min_id)
    #drop patient_name 
    if 'Patient Name' in df.columns:
        df = df.drop_duplicates(subset=None, keep='first', inplace=False)
        df = df.drop("= Name", axis=1)
        print('name dropped from data frame')

    print('importing to DB please wait...')
    # The orient='records' is the key of this, it allows to align with the format mentioned in the doc to insert in bulks.
    listToWrite = df.to_dict(orient='records')

    metadata = sqlalchemy.schema.MetaData(bind=engine,reflect=True)
    table = sqlalchemy.Table(tableToWriteTo, metadata, autoload=True)
    print(table.columns)
    # Open the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Inser the dataframe into the database in one bulk
    conn.execute(table.insert(), listToWrite)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
    session.expire_all()
    return min_id


if __name__ == "__main__":
    #init a list of file names to read in these should end in .xls
    filenames = []
    filenames = os.listdir(inpath)
    print(filenames)

    for filename in filenames:
        if '.xlsx' in filename: 
            inpath = inpath + filename.strip(chr(39))
            print(inpath)
            outpath = outpath + filename.strip(chr(39))

            print('calling import def')
            #import xls data
            min_case_id = import_data(inpath)
            print('calling transform defs')
            move_files(inpath, outpath.strip('.xlsx') + '.processed')
            #run data transformations
            transfromations(min_case_id)
            print('transforms completed.')


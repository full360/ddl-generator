import os,errno,sys

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred


def generateDDL(filename):
  
    current_path=os.getcwd()

    strDDL= ''
    strDType=''
    count= 1
    table_count=0
    strTable=''

    silentremove(current_path + '/output_table_ddl.sql')
    f = open(current_path + '/output_table_ddl.sql', 'a')
    import csv
    with open(current_path + '/' + filename) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
              strDType = row['DATA_TYPE'] 
                
              if strDDL <> '':
                if strTable <> row['TABLE_NAME']:
                   count = 1
                   strDDL = strDDL[:-2] 
                   strDDL = strDDL + '\n);\n'  
                    
              if count == 1:
                 strDDL = strDDL + '\nDROP TABLE IF EXISTS ' + row['TABLE_SCHEMA'] + '.' + row['TABLE_NAME'] + ' CASCADE;' 
                 strDDL = strDDL + '\nCREATE TABLE ' + row['TABLE_SCHEMA']+ '.' + row['TABLE_NAME']                 
                 strDDL = strDDL + ' \n(\n' + row['COLUMN_NAME'] + '  ' + strDType
                 table_count=table_count + 1
                    
                 if row['IS_NULLABLE'].strip() == 'NO':
                    strDDL = strDDL + ' NOT NULL' + ',\n' 
                 else:
                    strDDL = strDDL + ',\n'           
              else:
           
                 strDDL = strDDL + row['COLUMN_NAME'] + '  ' + strDType
                 if row['IS_NULLABLE'].strip() == 'NO':
                     strDDL = strDDL + ' NOT NULL' + ',\n' 
                 else:
                     strDDL = strDDL + ',\n' 

              strTable=row['TABLE_NAME']
              count = count + 1  
      
      strDDL = strDDL[:-2] + '\n);\n' 
      print(strDDL)
      print('\nTable_count:')
      print(table_count)
      f.write(strDDL)
      f.close()
  


if len(sys.argv) > 1:
  table_data=sys.argv[1]
  print table_data
  generateDDL(table_data)     
else:
  print 'Missing argument.Provide input file.'




import os.path
current_path=dir(os)
print(current_path)
strDDL= ''
strDType=''
count= 1
table_count=0
strTable=''
f = open('/Users/rmishra/Desktop/all-apps/Marketing/DDL-GENERATOR-BLOG/output_table_ddl.txt', 'a')
import csv
with open('/Users/rmishra/Desktop/all-apps/Marketing/DDL-GENERATOR-BLOG/data-for-ddl.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
          strDType = row['DATA_TYPE'] 
           
          if strDType[:10].upper() == 'CHARACTER(':
            intStart = strDType.index('(') +1
            #strDType = strDType[:10] +str(int(strDType[intStart:-1])*3)+')'
            strDType = 'VARCHAR(' +str(int(strDType[intStart:-1])*3)+')'
          else:

              if strDType[:5].upper() == 'CHAR(':
                 intStart = strDType.index('(') +1
                 #strDType = strDType[:5] +str(int(strDType[intStart:-1])*3)+')'
                 strDType = 'VARCHAR(' +str(int(strDType[intStart:-1])*3)+')'
              else:

                 if strDType[:8].upper() == 'VARCHAR(':
                     intStart = strDType.index('(') +1
                     #strDType = strDType[:8] +str(int(strDType[intStart:-1])*3)+')'
                     strDType = 'VARCHAR(' +str(int(strDType[intStart:-1])*3)+')'
                 else:

                     if strDType[:27].upper() == 'NATIONAL CHARACTER VARYING(':
                          intStart = strDType.index('(') +1
                          #strDType = 'NVARCHAR(' +str(int(strDType[intStart:-1])*3)+')'
                          strDType = 'VARCHAR(' +str(int(strDType[intStart:-1])*3)+')'
                     else:
                          if strDType[:19].upper() == 'NATIONAL CHARACTER(':
                             intStart = strDType.index('(') +1
                             #strDType = 'NCHAR(' +str(int(strDType[intStart:-1])*3)+')'
                             strDType = 'VARCHAR(' +str(int(strDType[intStart:-1])*3)+')'
                          else:
                             if strDType[:18].upper() == 'CHARACTER VARYING(':
                                intStart = strDType.index('(') +1
                                strDType = 'VARCHAR(' +str(int(strDType[intStart:-1])*3)+')'

          if strDType[:9].upper() == 'TIMESTAMP':
            strDType = 'TIMESTAMPTZ'
          
            
          if strDDL <> '':
            if strTable <> row['TABLE_NAME']:
               count = 1
               #strDDL = strDDL[:-2] 
               strDDL = strDDL + 'S3_BATCH_ID  BIGINT\n);\n'  
               #strDDL = strDDL + '\n);\n\n' 
          if count == 1:
             strDDL = strDDL + '\nDROP TABLE IF EXISTS ' + row['TABLE_SCHEMA'] + '.' + row['TABLE_NAME'] + ' CASCADE;' 
             strDDL = strDDL + '\nCREATE TABLE ' + row['TABLE_SCHEMA']+ '.' + row['TABLE_NAME'] 
             #strDDL = strDDL + ' \n(\n' + row['COLUMN_NAME'] + '  ' + row['DATA_TYPE']
             strDDL = strDDL + ' \n(\n' + row['COLUMN_NAME'] + '  ' + strDType
             table_count=table_count + 1
                
             if row['IS_NULLABLE'].strip() == 'NO':
                strDDL = strDDL + ' NOT NULL' + ',\n' 
             else:
                strDDL = strDDL + ',\n'           
          else:
       
             #strDDL = strDDL + row['COLUMN_NAME'] + '  ' + row['DATA_TYPE'] 
             strDDL = strDDL + row['COLUMN_NAME'] + '  ' + strDType
             if row['IS_NULLABLE'].strip() == 'NO':
                 strDDL = strDDL + ' NOT NULL' + ',\n' 
             else:
                 strDDL = strDDL + ',\n' 

          strTable=row['TABLE_NAME']
          count = count + 1  
  
  #strDDL = strDDL[:-2] + '\n);' 
  strDDL = strDDL + 'S3_BATCH_ID  BIGINT\n); ' 
  print(strDDL)
  print('\nTable_count:')
  print(table_count)
  f.write(strDDL)
  f.close()

#转化excel为sql#
#Data.xlsx---data.db#
import xlrd
import pymysql.cursors
connect = pymysql.Connect(
	host='localhost',
	port=3306,
	user='root',
	passwd='838444633',
	db='classroom',
	charset='utf8'
)
cursor = connect.cursor()
t=1
ExcelFile=xlrd.open_workbook('C:/Users/Administrator/Desktop/'+str(t)+'.xlsx')
sheet=ExcelFile.sheet_by_index(0)

cursor.execute('CREATE TABLE IF NOT EXISTS Data'+str(t)+'(Id INT PRIMARY KEY AUTO_INCREMENT)ENGINE = INNODB DEFAULT CHARSET = utf8')
for i in sheet.row_values(0):
	cursor.execute("alter table Data"+str(t)+" add "+str(i)+" varchar(225) default '0'")
str1=''
for i in sheet.row_values(0):#获取表头
	str1=str1+i+','
print(str1)
for j in range(1,sheet.nrows):
	str2=str(tuple([str(i) for i in sheet.row_values(j)]))[1:-1]
	print(str2)
	cursor.execute("INSERT INTO Data" +str(t)+"("+str1[:-1]+") VALUES("+str2+")")
connect.commit()
connect.close()

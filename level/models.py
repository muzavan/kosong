from django.db import models
from django.conf import settings
import MySQLdb as mdb
import json
# Create your models here.

# Table `level` : `id`,`image`,`answer`,`hint`,`contributor`,`a_contributor`,`viewed`
# TO-DO : Change to Proper Model
HOST = settings.HOST
USER = settings.USER
PASSWORD = settings.PASSWORD
DB_NAME = settings.DB_NAME

def newLevel(image,answer,hint,contributor,a_contributor):
	try:
		cnx = mdb.connect(HOST,USER,PASSWORD,DB_NAME)
		cur = cnx.cursor(mdb.cursors.DictCursor)
		q =  "INSERT INTO level(image,answer,hint,contributor,a_contributor) VALUES('%s','%s','%s','%s','%s')" % (image,answer,hint,contributor,a_contributor)
		cur.execute(q)
		cnx.commit()
		return True
	except Exception as e :
		print("Exception %d : %s" % (e[0],e[1]))
	except Error as e :
		print("Error %d : %s" % (e[0],e[1]))
	finally :
		cnx.close()
		return False

def setViewed(idx):
	try:
		cnx = mdb.connect(host,user,pw,db_name)
		cur = cnx.cursor(mdb.cursors.DictCursor)
		query = "UPDATE FROM `level` SET `viewed`=1 WHERE `id`= %d" % (idx)
		cur.execute(query)
		cnx.commit()
		return True
	except Exception as e :
		print("Exception %d : %s" % (e[0],e[1]))
	except Error as e :
		print("Error %d : %s" % (e[0],e[1]))
	finally :
		cnx.close()
		return False

def setNoViewed(idx):
	try:
		cnx = mdb.connect(host,user,pw,db_name)
		cur = cnx.cursor(mdb.cursors.DictCursor)
		query = "UPDATE FROM `level` SET `viewed`=1 WHERE `id`= %d" % (idx)
		cur.execute(query)
		cnx.commit()
		return True
	except Exception as e :
		print("Exception %d : %s" % (e[0],e[1]))
	except Error as e :
		print("Error %d : %s" % (e[0],e[1]))
	finally :
		cnx.close()
		return False

def deleteLevel(idx):
	try:
		cnx = mdb.connect(host,user,pw,db_name)
		cur = cnx.cursor(mdb.cursors.DictCursor)
		query = "DELETE FROM `level` WHERE `id`= %d" % (idx)
		cur.execute(query)
		cnx.commit()
		return True
	except Exception as e :
		print("Exception %d : %s" % (e[0],e[1]))
	except Error as e :
		print("Error %d : %s" % (e[0],e[1]))
	finally :
		cnx.close()
		return False

def getAllLevels():
	try:
		cnx = mdb.connect(host,user,pw,db_name)
		cur = cnx.cursor(mdb.cursors.DictCursor)
		query = "SELECT * FROM `level` WHERE `viewed`= 1"
		cur.execute(query)
		rows = cur.fetchall()
		hsl = {}
		i = 1
		for row in rows:
			hsl[i] = {}
			hsl[i] = row
			i+=1

		return json.dumps(hsl)

	except Exception as e :
		print("Exception %d : %s" % (e[0],e[1]))
	except Error as e :
		print("Error %d : %s" % (e[0],e[1]))
	finally :
		cnx.close()
		return False

def getRawAllLevels():
	try:
		cnx = mdb.connect(host,user,pw,db_name)
		cur = cnx.cursor(mdb.cursors.DictCursor)
		query = "SELECT * FROM `level`"
		cur.execute(query)
		rows = cur.fetchall()
		hsl = {}
		i = 1
		for row in rows:
			hsl[i] = {}
			hsl[i] = row
			i+=1

		return json.dumps(hsl)

	except Exception as e :
		print("Exception %d : %s" % (e[0],e[1]))
	except Error as e :
		print("Error %d : %s" % (e[0],e[1]))
	finally :
		cnx.close()
		return False

def getLevel(idx):
	try:
		cnx = mdb.connect(host,user,pw,db_name)
		cur = cnx.cursor(mdb.cursors.DictCursor)
		query = "SELECT * FROM `level` WHERE `id`=%d" % (idx)
		cur.execute(query)
		rows = cur.fetchall()
		hsl = {}
		for row in rows:
			hsl = row
		return json.dumps(hsl)

	except Exception as e :
		print("Exception %d : %s" % (e[0],e[1]))
	except Error as e :
		print("Error %d : %s" % (e[0],e[1]))
	finally :
		cnx.close()
		return False

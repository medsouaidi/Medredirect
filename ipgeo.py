#!/usr/bin/python
import sqlite3,os,sys
from datetime import datetime, timedelta
from flask import Flask, escape, request, jsonify
from ip2geotools.databases.noncommercial import DbIpCity
# ~ from flask_ipban import IpBan

app = Flask(__name__)



# ~ HADA SQLI3 I9AD IFCHIER .DB

def creat_db():
	
	hadaana = sqlite3.connect('ips_access.db')
	
	hadaana.execute('''CREATE TABLE COMPANY
			 (IP           TXT    NOT NULL,
			 Times           INT    NOT NULL );''')

try:
	creat_db()
except:
	pass
	
# ~ END ASAT



# ~ TIME ASAT 

def timer():
	global timeplus,timetime
	
	nine_hours_from_now = datetime.now() + timedelta(hours=12)
	
	timeplus = '{:%H:%M}'.format(nine_hours_from_now)
	timetime = '{:%H:%M}'.format(datetime.now())
	
	return timeplus,timetime
	

# ~ INSERT DATA F DB FILE 		 
def ip_insert(ips):
	databro.execute("INSERT INTO COMPANY (IP,Times) \
	VALUES ('"+ ips +"', 1)")
	databro.commit()
	

# ~ CHECK IP IF EXIST OR NOT 	
def filterit(ips):
	cursor = databro.execute("SELECT IP , Times from COMPANY WHERE IP = '"+ ips +"'")
	return "".join([ row[0] for row in cursor])


# ~ UPDATE STATU FOR IPS
def check(ips):
		cursor = databro.execute("SELECT IP , Times from COMPANY WHERE IP = '"+ ips +"'")
		for row in cursor:
			ip = row[0]
			times = row[1]
			if int(times) < int(foit):
				update = int(times) + 1
				databro.execute("UPDATE COMPANY set Times = "+ str(update) +" where IP = '"+ ips +"'")
				databro.commit()
				return update
			elif int(times) >= int(foit):
				timer()
				databro.execute("DELETE FROM COMPANY WHERE IP = '"+ ips +"'")
				databro.commit()
				os.system('iptables -A INPUT -s '+ ips +' -p tcp -m tcp --dport '+ str(PORT) +' --match time --timestart $(date -u -d @$(date "+%s" -d "'+ timetime +'") +%H:%M) --timestop $(date -u -d @$(date "+%s" -d "' + timeplus+ '") +%H:%M) -j DROP')
				return foit
			else:
				pass
				# ~ print("block")
		# ~ databro.close()
		

# ~ HOME PAGE 
@app.route("/", methods=["GET"])
def home():
	
	return ''' 
	
	Powered by msouaidi.site @M0H4MM33D
	'''


# ~ API DYALO
@app.route("/goto", methods=["GET"])
def get_my_ip():
	
	global databro
			
	databro = sqlite3.connect('ips_access.db')
	ips = str(request.remote_addr)
	
	if filterit(ips) != ips:
		ip_insert(ips)

	try:
		
		redirect = request.args['href']
		contry = request.args['contry']

	except:
		return ''' PROBLEM IN REQUEST .. please back ''', 200
	
	info = DbIpCity.get(ips, api_key='free')
	
	
	if info.country == contry:
		
		
		return '''
		
		<html>
		<head>
		<title>Redirection en HTML</title>
		<meta http-equiv="refresh" content="0; URL={}">
		</head>

		<body>
		
		<span>GOTO: {}, IP TIMES: {}</span>
		
		</body>

		</html>'''.format(redirect,redirect,check(ips))
		
	else:

		return ''' OFFRE EXPIRED .. please back ''', 404

    

if __name__ == "__main__":
	
	try:
		PORT = sys.argv[1]
		foit = int(sys.argv[2])
		app.run(host="0.0.0.0",port=int(PORT))
	except:
		print("USAGE script.py PORT TIMESTOBLOCKED : sudo python3 script.py 8080 4")

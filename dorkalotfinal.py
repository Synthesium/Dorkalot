 #a dorking tool #

## Imports
import time
import re
import requests
import sys
from bs4 import BeautifulSoup
## General  				
## variables
sleeptime=2
global domain
domain=""
browser="Mozilla/5.0_(MSIE;_Windows_11)"
gsite=""

### login pages ###
loginPageDict={
"lpadmin" : "inurl:admin",
"lplogin" : "inurl:login",
"lpadminlogin" : "inurl:adminlogin",
"lpcplogin" : "inurl:cplogin",
"lpweblogin" : "inurl:weblogin",
"lpquicklogin" : "inurl:quicklogin",
"lpwp1" : "inurl:wp-admin",
"lpwp2" : "inurl:wp-login",
"lpportal" : "inurl:portal",
"lpuserportal" : "inurl:userportal",
"lploginpanel" : "inurl:loginpanel",
"lpmemberlogin" : "inurl:memberlogin",
"lpremote" : "inurl:remote",
"lpdashboard" : "inurl:dashboard",
"lpauth" : "inurl:auth",
"lpexc" : "inurl:exchange",
"lpfp" : "inurl:ForgotPassword",
"lptest" : "inurl:test"	
}               

### fileTypes ###
fileTypesDict={
"ftdoc"   :  "filetype:doc",					## Filetype DOC (MsWord 97-2003)
"ftdocx"  :  "filetype:docx",						## Filetype DOCX (MsWord 2007+)
"ftxls"   :  "filetype:xls"	,					## Filetype XLS (MsExcel 97-2003)
"ftxlsx"  :  "filetype:xlsx",						## Filetype XLSX (MsExcel 2007+)
"ftppt"   :  "filetype:ppt"	,					## Filetype PPT (MsPowerPoint 97-2003)
"ftpptx"  :  "filetype:pptx",						## Filetype PPTX (MsPowerPoint 2007+)
"ftmdb"   :  "filetype:mdb"	,					## Filetype MDB (Ms Access)
"ftpdf"   :  "filetype:pdf"	,					## Filetype PDF
"ftsql"   :  "filetype:sql"	,					## Filetype SQL
"fttxt"   :  "filetype:txt"	,					## Filetype TXT
"ftrtf"   :  "filetype:rtf"	,					## Filetype RTF
"ftcsv"   :  "filetype:csv"	,					## Filetype CSV
"ftxml"   :  "filetype:xml"	,					## Filetype XML
"ftconf"  :  "filetype:conf",						## Filetype CONF
"ftdat"   :  "filetype:dat"	,					## Filetype DAT
"ftini"   :  "filetype:ini"	,					## Filetype INI
"ftlog"   :  "filetype:log"	,					## Filetype LOG
"ftidrsa" :  "index%20of:id_rsa%20id_rsa.pub"	## File ID_RSA
}

### Directory traversal ###
dirTravDict={

"dtparent"   :     "intitle:%22index%20of%22%20%22parent%20directory%22", 	## Common traversal
"dtdcim"     :     "intitle:%22index%20of%22%20%22DCIM%22", 				## Photo
"dtftp"      :     "intitle:%22index%20of%22%20%22ftp%22", 					## FTP
"dtbackup"   :     "intitle:%22index%20of%22%20%22backup%22",				## BackUp
"dtmail"     :     "intitle:%22index%20of%22%20%22mail%22",					## Mail
"dtpassword" :     "intitle:%22index%20of%22%20%22password%22",				## Password
"dtpub"      :     "intitle:%22index%20of%22%20%22pub%22"					## Pub
	
}

#### end of general variables and dictionaries  ####

## beginning ascii art function ##
def begin():
	print("Welcome to DORKALOT\n")
	print("DORKALOT-> a premier website reconnaissance tool.\nNow with reasonable privacy")

##  the input function ##
def giveInput():
	global domain
	domain = input("Enter the name of the site please: ")
## the query function ##
def query(searchvar):
	result=""
	resultNo=["0","10","20","30","40"]
	global gsite
	gsite="site:"+domain
	global alldata
	alldata=[]
	finalreg=""
	seperator=" \n"
	global linksfinal
	linksfinal=[]
	for start in resultNo:
		url = "https://www.google.com/search?q="+gsite+"%20"+searchvar+"&start="+start+"&client=firefox-b-e"
		page =requests.get(url)
		alldata.append(page.text) # 
		
	### to converttostr the list to string
		finalreg=seperator.join(alldata) #<-- step 1 til here .That is capturing the html data and storing it in a variable
	### the captcha ban thing ####<----step 2 to check the ban and if so exit
		checkban=re.findall("https://www.google.com/recaptcha",finalreg)
		if not checkban:
			time.sleep(2)
			linksfinal=re.findall("((http|https):\/\/[a-zA-Z0-9.\/?=_~-]*"+domain+"\/[a-zA-Z0-9.\/?=_~-]*)",finalreg)
			if not linksfinal:
				print("no results found.")
				return
			else:
				pass
		else:
			sys.exit("You've been blocked by google.So time out. Take your time ")
	### now to regex from the data #<--- step 4
	
	#print(alldata) # this will print the entire html code
	
	#print(linksfinal) # linksfinal is now a list with all the links harvested
	linksfinal= list(dict.fromkeys(linksfinal))# this to remove any duplicate entries
	print("\n\tResults found!!! Listing data....")
	c=1 ## a loop to print things out in a neat way
	for x in linksfinal:
		str(x)

		#print(+x[0])
		print("%d. %s" %(c,x[0]))
		c+=1

#### ####

####################################
### the actual code ###
begin()
giveInput()

print("Checking Login pages:\n")
c=1
for a,b in loginPageDict.items():
	cut=b.split(":")[1]
	cutcapital=cut.upper()
	f=cutcapital.replace("%20"," ")
	g=f.replace("%22"," ")
	print("\t\tChecking %s" % g , end=" ")
	query(b)
	c=c+1

print("Checking Files:\n")
c=1
for a,b in fileTypesDict.items():
	cut=b.split(":")[1]
	cutcapital=cut.upper()
	f=cutcapital.replace("%20"," ")
	g=f.replace("%22"," ")
	print("\t\tChecking %s" % g, end=" " )
	query(b)
	c=c+1

print("Checking Directories:\n")
c=1
for a,b in dirTravDict.items():
	cut=b.split(":")[1]
	cutcapital=cut.upper()
	f=cutcapital.replace("%20"," ")
	g=f.replace("%22"," ")
	print("\t\tChecking %s" % g, end=" " )
	query(b)
	c=c+1

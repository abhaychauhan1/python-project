#!/usr/bin/python

# Import modules for CGI handling 



import cgi,os
import sqlite3
import cgitb ;cgitb.enable()


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
last_name1  = form.getvalue('last_name1')
fileitem = form['filename']

if form.getvalue('breif_desc'):
    breif_desc = form.getvalue('breif_desc')
else:
    breif_desc = "Not set up" 

if form.getvalue('professional'):
   professional = "Yes"
else:
    professional = "No"
    
    
if form.getvalue('Radio'):
    gender = form.getvalue('Radio')
else:
    gender = "Not set up"
    
   

    

if fileitem.filename:
 fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
 open('/tmp/' + fn, 'wb').write(fileitem.file.read())

 message = 'The file "' + fn + '" was uploaded successfully'
   
else:
 message = 'No file was uploaded'


connection = sqlite3.connect('db12')
cursor = connection.cursor()





connection.commit()
connection.close()




print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<iframe>"
print "</iframe>"
print "<h2>%s</h2>" % (first_name)
print "<h2> %s</h2>" % (last_name)
print "<h2>%s</h2>" % (last_name1)
print "<h2>Is he professional ? %s</h2>" %(professional)
print "<h2>Gender %s</h2>" %(gender)
print "<h2>Brief Description %s</h2>" %(breif_desc)
print "<h2>Brief Description %s</h2>" %(message)
print "<img src='%s'></img>" %(fn)




print "</body>"
print "</html>"
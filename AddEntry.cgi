#!/usr/bin/python

import cgi, cgitb 
import mysql.connector as mariadb
form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"

print '<html>'
print '<head>'
print '<link rel="stylesheet" type="text/css" href="login.css">'
print '''<script>
function myFunction() {
    window.print();
}
</script>'''
print '</head>'
print '<body>'

f_type=form.getvalue('f_type')
name=form.getvalue('Name')
id=form.getvalue('Id')
branch=form.getvalue('branch')
semester=form.getvalue('sem')
email=form.getvalue('Email')
contact=form.getvalue('Mob')

if f_type=='Medical':
		F_ID='ML'+id
elif f_type=='Leave':
		F_ID='LE'+id
elif f_type=='Project':
		F_ID='PT'+id
elif f_type=='Railways':
		F_ID='RS'+id


mariadb_connection = mariadb.connect(user='pps', password='pps', database='student')

cursor = mariadb_connection.cursor(buffered=True)
cursor.execute("insert into Registartion_detail values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(F_ID,name,id,branch,semester,email,contact))


mariadb_connection.commit()

print '<h1><center>Your details has been saved successfully</center></h1>'
print F_ID
print f_type
print name
print id
print '<button onclick="myFunction()">Print this page</button>'
print '</body>'
print '</html>'



#!/usr/bin/python


print "Content-type:text/html\r\n\r\n"

print '<html>'
print '<head>'
print '<title>File Tracking System</title>'
print '<link rel="stylesheet" type="text/css" href="login.css">'
print '<script src="loginScript.js"></script>'
print '</head>'
print '<body>'

print '<div class="RegBox">'
print '<form id="NewEntry" action="AddEntry.cgi" target="_blank" method="post">'
print '''<select id="f1" name=f_type required>
  <option value="">--Select File Type--</option>
  <option name=f_type value="Medical">Medical Certificate</option>
  <option name=f_type value="Leave">Leave Application</option>
  <option name=f_type value="Project">Project File</option>
  <option name=f_type value="Railways">Railways Concession</option>
</select><br>'''




print '<input id="f1" type=text name=Name placeholder="Name" required><br>'
print '<input id="f1" type=text name=Id placeholder="ID Number" required><br>'
print '''<select  id="f1" name=branch required>
	  <option value="">--Select Your Branch--</option>
	  <option name="branch" value="CSE">CSE</option>
	  <option name="branch" value="ECE">ECE</option>
	  <option name="branch" value="ME">ME</option>
	  <option name="branch" value="CE">CE</option>
	  <option name="branch" value="EE">EE</option>
	  <option name="branch" value="IT">IT</option>
</select><br>
	  <select id="f1" name=sem required>
	  <option value="">--Select Your Semester--</option>
	  <option name="sem" value="1">1</option>
	  <option name="sem" value="2">2</option>
	  <option name="sem" value="3">3</option>
	  <option name="sem" value="4">4</option>
	  <option name="sem" value="5">5</option>
	  <option name="sem" value="6">6</option>
	  <option name="sem" value="7">7</option>
	  <option name="sem" value="8">8</option>

</select><br>'''

print '<input id="f1" type=email name=Email placeholder="Email Address" required><br>'
print '<input id="f1" type=num name=Mob placeholder="Contact Number" required><br>'



print '<input id="f1" type="submit" value="Submit Entry"><br>'
print '</form>'
print '</div>'
print '</body>'
print '</html>'

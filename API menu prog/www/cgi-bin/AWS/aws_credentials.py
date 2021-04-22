#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess

form = cgi.FieldStorage()
redirectURL = "http://localhost/AWS/aws.html"
access_key = form.getvalue("access")
secret_key = form.getvalue("secret")
region = form.getvalue("region")

if subprocess.getstatusoutput("ls /usr/share/httpd/.aws")[0]:
    subprocess.getoutput("sudo mkdir /usr/share/httpd/.aws")
    subprocess.getoutput("sudo chmod o+rwx /usr/share/httpd/.aws")

file1 = open("/usr/share/httpd/.aws/config", mode="w")
file1.write("""[default]
region = {}""".format(region))
file1.close()

file2 = open("/usr/share/httpd/.aws/credentials", mode="w")
file2.write("""[default]
aws_access _key_id ={}
aws_secret_access_key = {}""".format(access_key,secret_key))
file2.close()

print('<html>')
print('  <head>')
print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')
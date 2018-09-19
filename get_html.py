import cgi

form = cgi.FieldStorage()

input = form.getValue("testebox")

print "Ola"

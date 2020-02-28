#!/usr/bin/env python3
#!/usr/bin/env python2
#Ahmad Adnan Jaber 
#this has been coded without any third party libraries,but the standard.
import re
import sys
import urllib.request

#value is the amount to be converted using system argument to fill it out from the CLI
value = sys.argv[1] 
#source is the type of mesuarments to be converted from, using system argument to fill it out from the CLI
source = sys.argv[2] 
#destination is the type of mesuarments to be converted to, using system argument to fill it out from the CLI
destination = sys.argv[3] 
#in the urlretriever we are retrieving the html page and saving it in "webpage.txt" ps you need to create/touch a file called webpage.txt
a=urllib.request.urlretrieve("http://unitconverter.io/"+source+"/"+destination+"/"+value, "webpage.txt")
#in this part we are opening the webpage.txt file to read the webpage from
file = open("webpage.txt", "r")
#in this part we are reading line by line and saving it in "lines"
lines = file.readlines()
#after that we close the file
file.close()
#parsing the webpage using regex
find = re.findall(r'<\s*p[^>]*>(.*?)<\s*/\s*p>', str(lines))
l=re.findall(r'[\d.,]*',str(find))
l = ' '.join(l).split()
#This last part is the where we get the results
print (value+" "+source+" = "+l[1]+" "+destination)
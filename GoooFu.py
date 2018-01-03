# A simple script to automate Google Hacking & save the results to an HTML file during an authorized penetration test
#
#
# Author: B. Alex John
#
#
# GoooFu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GoooFu is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details <http://www.gnu.org/licenses/>.
import sys
try:
	#import mechanize
	from google import search
	from random import randint
	from time import sleep
except ImportError:
	print("Modules required to run this scirpt are: google, random, & time")
	print("\nModule(s) not found. Install prerequisites & try again!\nUse 'pip install module_name' to install missing prerequisites")
 
# INFORMATION
NAME		= "Gooo-Fu"
VERSION		= "1.0"
AUTHOR		= "Author: B. Alex John"
TWITTER     = "@Praetorian_GRD"
GITHUB		= "Github: https://github.com/west-wind/GoooFu"
LINKEDIN    = "LinkedIn: https://linkedin.com/in/alexsean"

# MAIN()
def main():
  try:
	
    print "\n\\\\\\\ Welcome to GoooFu //////// \n"
    print "WARNING: Executing this script multiple times may cause Google to block your IP address"
    fName = str(raw_input("Enter filename to save output to: "))
    fileName = fName + '.html'
    f = open(fileName,"w+")
    print "Search results for 'site' & 'string' directive: \n"
    searchSite = str(raw_input("Enter the URL: "))
    searchString = str(raw_input("Enter your search string: "))
    print "\nPlease wait. Fetching  .. .."
    f.write('<h1>Site: ' + searchSite + ' & String: ' + searchString + ' search output:</h1>')
    query = 'site:' + searchSite + ' ' + searchString
    #br = mechanize.Browser()
    #Session = br.open("https://www.google.com/")
    #print Session.info()
    #print Session.read()
    try:
		for j in search(query, tld="com", num=5, stop=1, pause=4):
			print(j)
			f.write('<p> <a href="' + j + '">' + j + '</a> </p>' + '\n')
			sleep(randint(0.5,1.5))

    except:
		print "HTTP Error"
	
    print "\nSearch results with 'inurl' directive: "
    searchPage = str(raw_input("\nEnter the page you want to check for: "))
    print "\nPlease wait. Fetching  .. .."
    f.write('<h1>Site: ' + searchSite + ' & Page: ' + searchPage + ' search output:</h1>')
    query2 = 'inurl:' + searchPage + ' ' + 'site:' + searchSite
    try:
		for i in search(query2, tld="com", num=5, stop=1, pause=4):
			print(i)
			f.write('<p> <a href="' + i + '">' + i + '</a> </p>' + '\n')
			sleep(randint(1.0,1.5))

    except:
		print "HTTP Error"
	
    print "\nFiletype search on supplied URL: "
    fileType = str(raw_input("\nEnter filetype to search: "))
    print "\nPlease wait. Fetching  .. .."
    f.write('<h1>Site: ' + searchSite + ' & File type: ' + fileType + ' search output:</h1>')
    query4 = 'site:' + searchSite + 'filetype:' + fileType
    try:
		for l in search(query4, tld="com", num=5, stop=1, pause=4):
			print(l)
			f.write('<p> <a href="' + l + '">' + l + '</a> </p>' + '\n')
			sleep(randint(1.0,1.5))

    except:
		print "HTTP Error"
		
    #print "\nExecuting 'allintitle' search:"
    #print "\nPlease wait. Fetching  .. .."
    #f.write('<h1>Allintitle search output:</h1>')
    #query5 = 'allintitle:' + searchString
    #try:
	#	for m in search(query5, tld="com", num=5, stop=1, pause=4):
	#		print(m)
	#		f.write('<p> <a href="' + m + '">' + m + '</a> </p>' + '\n')

    #except:
	#	print "HTTP Error"
	
    print "\nExecuting 'intitle' search:"
    print "\nPlease wait. Fetching  .. .."
    f.write('<h1>Intitle search output:</h1>')
    query6 = 'intitle:' + searchString
    try:
		for n in search(query6, tld="com", num=5, stop=1, pause=4):
			print(n)
			f.write('<p> <a href="' + n + '">' + n + '</a> </p>' + '\n')
			sleep(randint(0.5,1.9))

    except:
		print "HTTP Error"
    f.close()
    print "\nOutput has been saved to %s.html" %fName
    print "\nThank you for using Gooo-Fu. To contribute https://github.com/west-wind/GoooFu"
    print "\nExiting..."
  except KeyboardInterrupt:
    sys.exit(0)
main()
# GoooFu
A simple script to automate Google Hacking & save the results to an HTML file during an authorized penetration test.
WARNING: Executing this script multiple times may cause Google to block your IP address. Prerequisite python modules needed: google, random, & time. To install prerequisite modules, run 'pip install module_name'. 

To run the script: python GoooFu.py

When prompted, enter the target URL, keyword to search for, specific pages in the supplied website (login, admin, email, etc.), & the file type to search for.

Change the num value to a higher number to prevent IP ban. This might cause the script to slow down, so it is suggested to run it in the background. Currently working on changing the bot behaviour which results in Google blocking the IP. Tried 'mechanize' and sleep for a random interval during every iteration. I'd appreciate any help I can get in this matter.

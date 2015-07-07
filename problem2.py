import webbrowser
import time

urls = [['http://www.google.com',10], ['http://www.nairaland.com', 2], ['http://www.facebook.com', 30] ]
def run():
	s = ('')
	i = (0)
 	for item in urls:
 		s = item[0]
 		i = item[1]
		webbrowser.open(s)
		time.sleep(i)

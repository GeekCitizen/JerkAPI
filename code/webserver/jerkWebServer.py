from webserver.generic import genericWebServer

class JerkWebServer(genericWebServer):
    URLs = {} # Will contain all URLs
    URLsGET = {} # Will contain URL with Get method (Key = URL, Value = Action bloc)
    URLsPost = {} # Will contain URL with Post method (Key = URL, Value = "Last update date")

    def addURL(self, URL):
        print "ADDURL"

    def addURLGet (self, URL, block):
        print "addURLGet"

    def addURLPost (self, URL, block):
        print "addURLPost"

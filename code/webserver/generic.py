from utils.logs import Logger

class genericWebServer:
    IPAddress = "127.0.0.1"
    portNumber = 80

    def __init__ (self, alog):
        self.logger = alog;
        #self.logger.changeLogLevel(7)
        #print self.logger
        self.logger.log(5, "Initializing WebServer")
        #log("Initializing WebServer", 7)

    def __str__ (self):
        print "Working for IP Address : " + self.IPAddress
        print "Listening on port : " + self.portNumber


    def changeIP (self, IPA):
        self.IPAddress = IPA

    def changePort (self, portN):
        self.portNumber = portN

    def startServer (self):
        self.logger.log(5, "Starting")

    def stopServer (self):
        self.logger.log(5, "Stopping")

    def restartServer (self):
        self.stopServer
        self.startServer

from utils.logs import Logger
import socket, sys, os
from thread import *

class genericWebServer:
    IPAddress = "127.0.0.1"
    portNumber = 8080
    maxConnections = 2

    # logger # Will be set by constructor

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

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.log(7, "Socket created on IP " + str(self.IPAddress) + " and port " + str(self.portNumber) + ".")
        try:
            self.sock.bind((self.IPAddress, self.portNumber))
        except socket.error as msg:
            self.logger.log(0, 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit(2)
        self.logger.log(7, "Socket bind OK.")

        self.sock.listen(self.maxConnections)
        while 1:
            #wait to accept a connection - blocking call
            try:
                conn, addr = self.sock.accept()
                self.logger.log(7, 'Connected with ' + addr[0] + ':' + str(addr[1]))

                #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
                start_new_thread(self.serveclient, (conn,))
            except KeyboardInterrupt:
                self.logger.log(0, "System is shutting down due to keystroke")
                break
            except any as msg :
                self.logger.log(0, "System aborted due to error. Code: [" + str(msg[0])+ "] with message :[" + str(msg[1])+ "]")
                break

        try:
            self.sock.close()
            self.logger.log(0, "System is stopping")
            os._exit(3)
        except socket.error as msg:
                self.logger.log(0, "Error with Socket. Code: [" + str(msg[0]) + "] and message: [" + str(msg[1]) + "]")

    def serveclient (self, conn):
        conn.sendall("This is default Connection. Please, redefine ServeClient() in your own code.")
        conn.close()

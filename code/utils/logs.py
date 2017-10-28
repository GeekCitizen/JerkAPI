class Logger:
    logLvl = 1
    logLvlMax = 7

    strLvl0 = "FATAL"
    strLvl1 = "ALERT"
    strLvl2 = "CRITICAL"
    strLvl3 = "ERROR"
    strLvl4 = "WARNING"
    strLvl5 = "NOTICE"
    strLvl6 = "INFO"
    strLvl7 = "DEBUG"

    def __init__(self):
        self.log(5, "Logger Initializing")

    def __str__(self):
        return "Current Log Level: " + str(self.logLvl)

    def changeLogLevel (self, newLogLvl):
        try:
            x = int(newLogLvl)
            if newLogLvl <= self.logLvlMax:
                self.logLvl = newLogLvl
                self.__log1("Changing log level to "+str(newLogLvl))
            else:
                self.__log4(str(newLogLvl) + " is above " + str(self.logLvlMax))
        except ValueError:
            # Not a fatal error
            self.__log1(str(newLogLvl) + " is not an integer")


    def log(self, lvl, msg=""):
        #print ("here " + str(lvl) + " " + msg + " " + str(self.logLvl))
        try:
            x = int(lvl)
            if lvl <= self.logLvl:
                if lvl == 0:
                    self.__log0(msg)
                elif lvl == 1:
                    self.__log1(msg)
                elif lvl == 2:
                    self.__log2(msg)
                elif lvl == 3:
                    self.__log3(msg)
                elif lvl == 4:
                    self.__log4(msg)
                elif lvl == 5:
                    self.__log5(msg)
                elif lvl == 6:
                    self.__log6(msg)
                elif lvl == 7:
                    self.__log7(msg)
        except ValueError:
            print self.strLvl1 + str(newLogLvl) + " is not an integer"


    # Private method for logging
    def __logIT(self, lvl, msg):
        print "[LOG - " + lvl + "] " + msg
    def __log0(self, msg):
        self.__logIT(self.strLvl0, msg)
    def __log1(self, msg):
        self.__logIT(self.strLvl1, msg)
    def __log2(self, msg):
        self.__logIT(self.strLvl2, msg)
    def __log3(self, msg):
        self.__logIT(self.strLvl3, msg)
    def __log4(self, msg):
        self.__logIT(self.strLvl4, msg)
    def __log5(self, msg):
        self.__logIT(self.strLvl5, msg)
    def __log6(self, msg):
        self.__logIT(self.strLvl6, msg)
    def __log7(self, msg):
        self.__logIT(self.strLvl7, msg)

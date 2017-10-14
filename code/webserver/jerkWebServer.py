from webserver.generic import genericWebServer
import json, os

class JerkWebServer (genericWebServer):
    URLs = {} # Will contain all URLs
    URLsGET = {} # Will contain URL with Get method (Key = URL, Value = Action bloc)
    URLsPost = {} # Will contain URL with Post method (Key = URL, Value = "Last update date")

    def parseJSON (self, jsonStr):
        #print "parsing" + jsonStr
        json1 = json.loads(jsonStr);

        # Get PortNumber
        self.__parseJSON_PortNumber(json1)
        self.__parseJSON_URLs(json1)

    def __parseJSON_PortNumber (self, json1): # Key is : PortNumber
        """
        Parses the JSON "PortNumber" assertion to populate change port number
        """
        try:
            x = int(json1['PortNumber'])
            self.changePort(int(json1['PortNumber']))

        except ValueError:
            self.logger.log(0, "PortNumber is not an integer: [" +  json1['PortNumber'] + "]")
            os._exit(1)
        except KeyError:
            self.logger.log(7, "PortNumber is not specified. Using default value: [" + str(self.portNumber) + "]")


    def __parseJSON_URLs (self, json1): # Key is Services
        """
        Parses the JSON "Services" block to populate URL list
        """
        try:
            x = json1['Services']
        except KeyError:
            self.logger.log(0, "Services array not found in JSON")
            os._exit(1)

        for vari in range(len(x)):
            varj = json.loads(json.dumps(x[vari]))
            try:
                varm = varj['method']
            except KeyError:
                self.logger.log(0, "Method is missing in JSON block. \n=== \n" + str(x[vari]) + "\n===\n")

            # Next depends on Method type
            if varm == "GET":
                self.__addURLGet(varj)
            elif varm == "POST":
                self.__addURLPost(varj)
            else:
                self.logger.log(0, "Method is not recognized: "+varm)
                os._exit(1)


    def registerNewService (self, json):
        self.logger.log(7, "registering")

    def __addURL(self, URL):
        self.logger.log(7, "ADDURL")

    def __addURLGet (self, blk):
        self.logger.log(7, "Registering a 'GET' URL")
        try:
            vart = blk['type']
            self.URLsPost[blk['url']] = '{"Init": "Init"}'
        except KeyError:
            self.logger.log(0, "Unable to add GET URL: Config is not complete" + str(blk))
            os._exit(1)
        if vart == "bash":
            try:
                tab = [vart, blk['command'], blk['options']]
            except KeyError:
                self.logger.log(0, "For type bash, you need to specify command and options (even if options is empty)")
        elif vart == "fetchurl":
            tab = [vart, blk['source']]
        elif vart == "push":
            tab = [vart]
        else:
            self.logger.log(0, "Method is not recognized " + str(blk))
            os._exit(1)
        self.URLsGET[blk['url']] = tab


    def __addURLPost (self, blk):
        self.logger.log(7, "Registering a 'POST' URL")
        try:
            self.URLsPost[blk['url']] = '{"Init": "Init"}'
        except KeyError:
            self.logger.log(0, "Unable to add POST URL: URL does not exist" + str(blk))
            os._exit(1)

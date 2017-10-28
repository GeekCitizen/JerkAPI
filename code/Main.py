from webserver.jerkWebServer import JerkWebServer
from utils.logs import Logger

logger = Logger()
logger.changeLogLevel(7) # 7 is default loglevel

obj = JerkWebServer(logger)
f = open('../examples/_example-001__TEST.json', 'r')

jblock = f.read()
f.close()
obj.parseJSON(jblock)
obj.run()

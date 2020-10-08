# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import logging
from nigelsautobot import NigelsAutoBot
from markdown import markdown

# The below imports are all local
from config import Config
from const import Const

hostName = '' #"192.168.2.4"
serverPort = 8008

class nigelHTTPBot(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.htmlBot = htmlBot()
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		
		print('requested has been %s' % self.path)
		self.wfile.write(bytes(markdown(self.htmlBot.handleCommand('covid')),'utf-8'))
		
	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)
		self.send_response(200)
		self.end_headers()
		response = BytesIO()
		response.write(b'This is POST request. ')
		response.write(b'Received: ')
		response.write(body)
		self.wfile.write(response.getvalue())

class htmlBot(NigelsAutoBot):
	
	def __init__(self):
		self.responseMessage = ''
		super().__init__()
	
	def reply_text(self, textMessage):	
		self.responseMessage += textMessage
		
	def reply_photo(self, photoLocation):
		self.responseMessage += '<IMG SRC="http://%s:8080/%s" >' % (self.config.WEBURL, photoLocation)

		# This function handles the commands given by the user.
	def handleCommand(self, messageCommand):
		logging.info('Executing command %s.' % messageCommand)

		if messageCommand == self.const.TELEGRAM_COMMAND_VERSION:
			self.reply_text(self.escapeString(self.generateVersionResponse()))
		elif messageCommand == self.const.TELEGRAM_COMMAND_INFO:
			self.reply_text(self.escapeString(self.const.BOT_INFO))
		elif messageCommand == self.const.TELEGRAM_COMMAND_COVID:
			self.covidHandler.getCovidData(self)
		elif messageCommand == self.const.TELEGRAM_COMMAND_TEMPERATURE:
			self.temperatureHandler.getTemperature(self)
			
		return self.responseMessage


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), nigelHTTPBot)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
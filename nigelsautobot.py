# Generic modules to import
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telegram
import locale
import logging

# The below imports are all local
from config import Config
from const import Const
from covidhandler import CovidHandler
from temperaturehandler import TemperatureHandler

class NigelsAutoBot:

	def __init__(self):
		# Config and setup
		self.const = Const()
		self.config = Config()
		locale.setlocale(locale.LC_TIME, self.config.LOCALE)
		# Set logging level and info
		logging.basicConfig(level=self.config.LOG_LEVEL,
												format=self.const.LOG_FORMAT)
		self.covidHandler = CovidHandler()
		self.temperatureHandler = TemperatureHandler()

	# generate version response, for testing purposes in separate function.
	def generateVersionResponse(self):
		return self.const.BOT_VERSION_TEXT % self.const.BOT_VERSION

	def escapeString(self, textMessage):
		specialChars = {} 
		specialChars['\\'] = '\\\\' 
		specialChars['`'] = '&#96;'
		specialChars['*'] = '\*'
		specialChars['_'] = '\_'
		specialChars['{'] = '\{'
		specialChars['}'] = '\}'
		specialChars['['] = '\['
		specialChars[']'] = '\]'
		specialChars['('] = '\('
		specialChars[')'] = '\)'
		specialChars['#'] = '\#'
		specialChars['+'] = '\+'
		specialChars['-'] = '\-'
		specialChars['.'] = '\.'
		specialChars['!'] = '\!'
		for specialKey in specialChars:
			textMessage = textMessage.replace(specialKey,specialChars[specialKey])
			print(textMessage)
		return textMessage

	def reply_text(self, textMessage):	
		self.update.message.reply_text(textMessage, quote=False, parse_mode=telegram.ParseMode.MARKDOWN_V2)
		
	def reply_photo(self, photoLocation):
		self.update.message.reply_photo(open(photoLocation,'rb'), quote=False)

	# This function handles the commands given by the user.
	def handleCommand(self,update,context):
		logging.info('Executing command %s received from %s.' % (update.message.text, update.message.from_user.name))
		messageCommand = update.message.text
		
		self.update = update
		self.context = context

		if messageCommand == self.const.TELEGRAM_COMMAND_PREFIX + self.const.TELEGRAM_COMMAND_VERSION:
			self.reply_text(self.generateVersionResponse())
		elif messageCommand == self.const.TELEGRAM_COMMAND_PREFIX + self.const.TELEGRAM_COMMAND_INFO:
			self.reply_text(self.const.BOT_INFO)
		elif messageCommand == self.const.TELEGRAM_COMMAND_PREFIX + self.const.TELEGRAM_COMMAND_COVID:
			self.covidHandler.getCovidData(self)
		elif messageCommand == self.const.TELEGRAM_COMMAND_PREFIX + self.const.TELEGRAM_COMMAND_TEMPERATURE:
			self.temperatureHandler.getTemperature(self)

	
	# Set up the listener
	def main(self):
		updater = Updater(self.config.BOT_KEY, use_context=True)
		dp = updater.dispatcher
		dp.add_handler(CommandHandler(self.const.TELEGRAM_COMMAND_COVID,self.handleCommand), True)
		dp.add_handler(CommandHandler(self.const.TELEGRAM_COMMAND_VERSION,self.handleCommand), True)
		dp.add_handler(CommandHandler(self.const.TELEGRAM_COMMAND_TEMPERATURE,self.handleCommand), True)	
		dp.add_handler(CommandHandler(self.const.TELEGRAM_COMMAND_INFO,self.handleCommand), True)	
		logging.info('Starting polling for commands')
		updater.start_polling()
		updater.idle()

if __name__ == '__main__':
	bot = NigelsAutoBot()
	bot.main()
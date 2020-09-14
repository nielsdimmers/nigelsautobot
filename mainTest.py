# Importing subprocess Library
import subprocess
import unittest
from covidhandler import CovidHandler
from refreshCovidData import CovidDataRefresher
import hashlib
import time

# checking output of the command
# scriptOutput = subprocess.check_output(['ls', '-a'])

#print('Script output is %s', scriptOutput)

class TestStringMethods(unittest.TestCase):
	
	def test_retrieveCovidData(self):
		refresher = CovidDataRefresher()
		covidData = refresher.retrieveData('TEST')
		covidString = str(covidData)
		self.assertEqual(len(covidString),79406,'Incorrect input testdata length')
		self.assertEqual(len(covidString.split('Amersfoort')),200,'Incorrect testdata city consistency')
		covidArray = refresher.addByDay(covidData);
		result = 0
		for covidDate in covidArray:
			result += covidArray[covidDate]
		self.assertEqual(result,465,'Incorrect testdata total infections')
		self.assertEqual(len(covidArray),199,'Incorrect testdata daily count')
		refresher.fillDB(covidArray)			
	
	def test_nigelsautobot(self):
		covidHandler = CovidHandler()
		infectedMessage = covidHandler.generateCovidResponseMessage().split('\n')[1]
		self.assertIn('Het aantal nieuwe corona zieken gisteren gemeld was:',infectedMessage)

if __name__ == '__main__':
    unittest.main()

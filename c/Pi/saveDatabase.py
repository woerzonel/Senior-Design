import serial
import time
from storedProcedures.Taps import Taps

class saveDatabase:
	port = serial.Serial("/dev/rfcomm0", baudrate=9600)
  	db_name = 'BeerTapSystem.db'
    db_loc = 'C:\sqlite\dbs\\'
	
	
	def __init__(self):
		#Find and open the sql data base		
		self.taps_procedures = Taps(db_name=self.db_name, db_loc=self.db_loc)
	
	def main():
	# reading and writing data from and to arduino serially.                                      
	# rfcomm0 -> this could be different
		while True:
			print "DIGITAL LOGIC -- > SENDING..."
			#string from hub "B33R 1 1000" 
			rcv = port.readline()
			
			#split the message
			wordList = rcv.split()
			
			#make sure its one of ours
			if wordList[0] == 'B33R':
				#save the count and ID
				count = wordList[2]
				sensorId = wordList[1]
				
				#go through and update the beer.
				get_beer(sensorId,count)

    def get_beer(self,sensor_id, count):
		#tapFound = self.taps_procedures.get_tap(sensor_id)
		
		#get list
		tapList = self.taps_procedures.get_taps()
		
		#search through the list for the matching tap
		for currentTap in tapList:
			if currentTap['sensorId'] == sensor_id:
				tapId == currentTap['id']
				beerId == currentTap['beerId']
				update_tap(tapId, beerId, count)


    def update_tap(self,tap_id, beer_id, count):
		#update the tap with the amount you want
		tapToUpdate = self.taps_procedures.set_tap(tap_id, beer_id, self.count)
		
	
	if __name__ == '__main__':
    main()



 

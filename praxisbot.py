from errbot import BotPlugin, botcmd
import time

class PraxisBot(BotPlugin):

	def activate(self):
		super().activate()
		# initial setup
		if 'counters' not in self:
			self['counters'] = {}

	@botcmd
	def pick(self, msg, args):
		return 

	@botcmd
	def alive(self, msg, args):
		with self.mutable('counters') as counters:
			alive_count = counters.get('alive',0)
			counters['alive'] = alive_count + 1
		return "PraxisBot alive and ready for action [" + str(alive_count) + "]"

	@botcmd
	def messagerooms(self, msg, args):
		yield "Starting"

		current_rooms = self.rooms()
		for current_room in current_rooms:
			yield "Found room [" + str(current_room) + "] with dir [ " + str(dir(current_room)) + "]"	

			current_occupants = current_room.occupants
			for current_occupant in current_occupants:
				yield "Found occupant [" + current_occupant.nick + "] with dir [ " + str(dir(current_occupant)) + "]"	
				self.send( current_occupant, "Allo [" + current_occupant.nick + "] in [" + current_room.name + "] with alive_count [" + str(self['counters']['alive']) + "]")

		yield "Done Rooms"

	@botcmd
	def talktott(self, msg, args):
		self.send( self.build_identifier("a5zt4eotibdpzkrxd67zs74xuh"), "Talking to you")


	@botcmd
	def listpeople(self, msg, args):
		yield "Starting listpeople"

		current_rooms = self.rooms()
		for current_room in current_rooms:
#			yield "Found room [" + str(current_room) + "] with dir [ " + str(dir(current_room)) + "]"	
			yield "Found room [" + str(current_room) + "]"	

			start = time.time()
			
			current_occupants = current_room.occupants
			response = []
			for current_occupant in current_occupants:
#				yield "Found occupant [" + current_occupant.nick + "] with dir [ " + str(dir(current_occupant)) + "]"	
# nick can be changed by the user
#				response.append(current_occupant.nick)
				response.append("[" + current_occupant.userid + "," + current_occupant.nick + "]")
			yield "Found [" + str(len(response)) + "] occupants [" + str(response) + "]"
			end = time.time()
			yield "Done room [" + str(current_room) + "] in [" +  str((end - start)) + "]"

		yield "Done listpeople"



class PlayerModel(object):
	'Represent a player information'

	playerID = ''
	playerName = ''
	playerEmail = ''
	playerTeam = ''
	playerRank = ''

	def __init__(self, id, name, email, team, rank):
		self.playerID = id
		self.playerName = name
		self.playerEmail = email
		self.playerTeam = team
		self.playerRank = rank

	def setID(self, id):
		self.playerID = id

	def setName(self, name):
		self.playerName = name

	def setEmail(self, email):
		self.playerEmail = email

	def setTeam(self, team):
		self.playerTeam = team

	def setRank(self, rank):
		self.playerRank = rank

	def getID(self):
		return self.playerID

	def getName(self):
		return self.playerName

	def getEmail(self):
		return self.playerEmail

	def getTeam(self):
		return self.playerTeam

	def getRank(self):
		return self.playerRank

	def hasTeam(self):
		return self.playerTeam != ''

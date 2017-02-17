
class TeamModel(object):
	'Represents a team'

	teamMembers = []
	teamID = ''
	teamName = ''
	teamLogo = ''
	teamRank = 0


	def __init__(self, id, name, logo, members, rank):
		self.teamID = id
		self.teamName = name
		self.teamLogo = logo
		self.teamMembers = members
		self.teamRank = rank

	def __cmp__(self, otherTeam):
		for curr, other in zip(self.__values(), otherTeam.__values()):
			check = cmp(curr, other)
			if check:
				return check
		return 0

	def __eq__(self, otherTeam):
		return cmp(self, otherTeam) == 0

	def __ne__(self, otherTeam):
		return cmp(self, otherTeam) != 0

	def __lt__(self, otherTeam):
		return self.teamRank < otherTeam.teamRank

	def __gt__(self, otherTeam):
		return self.teamRank > otherTeam.teamRank

	def setID(self, id):
		self.teamID = id

	def setName(self, name):
		self.teamName = name

	def setLogo(self, logo):
		self.teamLogo = logo

	def setMembers(self, members):
		self.teamMembers = members

	def setRank(self, rank):
		self.teamRank = rank

	def getID(self):
		return self.teamID

	def getName(self):
		return self.teamName

	def getLogo(self):
		return self.teamLogo

	def getMembers(self):
		return self.teamMembers

	def getRank(self):
		return self.teamRank

	def addMember(self, member):
		added = False
		if not member.hasTeam():
			member.setTeam(self.teamName)
			self.teamMembers.append(member)
			added = True
		return added

	def removeMember(self, member):
		removed = False
		if member in self.teamMembers:
			member.setTeam('') # could not work verify
			self.teamMembers.remove(member)
			removed = True
		return removed

	def removeMemberByEmail(self, memberEmail):
		member = self.searchMemberByEmail(memberEmail)
		return self.removeMember(member)

	def removeMemberById(self, memberId):
		member = self.searchMemberById(memberId)
		return self.removeMember(member)

	def searchMemberById(self, memberId):
		pos = self.getMemberPositionById(memberId)
		if pos >= 0:
			return self.teamMembers[pos]
		else:
			return pos

	def searchMemberByEmail(self, memberEmail):
		pos = self.getMemberPositionByEmail(memberEmail)
		return self.teamMembers[pos] if pos >= 0 else pos

	def searchMemberByName(self, memberName):
		members = []
		for member in self.teamMembers:
			if member.playerName == memberName:
				members.append(member)
		return members[0] if len(members) == 1 else members

	def getMemberPositionById(self, memberId):
		pos = -1
		for i in range(len(self.teamMembers)):
			if memberId == self.teamMembers[i].playerID:
				pos = i
				break
		return pos

	def getMemberPositionByEmail(self, memberEmail):
		pos = -1
		for i in range(len(self.teamMembers)):
			if memberEmail == self.teamMembers[i].playerEmail:
				pos = i
				break
		return pos

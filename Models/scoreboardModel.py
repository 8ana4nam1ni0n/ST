
class ScoreboardModel(object):
	'Represent the Scoreboard of an Event'

	sbTable = []

	def __init__(self, teamList):
		for i in range(len(teamList)):
			row = {'place': i + 1, 'team': teamList[i], 'points': 0, 'rankingPoints': 0.0}
			self.sbTable.append(row)

	def getTeamPositionByName(self, teamName):
		pos = -1
		for i in range(len(self.sbTable)):
			if self.sbTable[i]['team'] == teamName:
				pos = i
				break
		return pos

	def addTeamPoints(self, teamName, pointsToAdd):
		pointsAdded = False
		pos = self.getTeamPositionByName(teamName)
		if pos >= 0:
			self.sbTable[pos]['points'] += pointsToAdd
			pointsAdded = True
		return pointsAdded

	def removeTeamPoints(self, teamName, pointsToRemove):
		pointsRemoved = False
		pos = self.getTeamPositionByName(teamName)
		if pos >= 0:
			self.sbTable[pos]['points'] -= pointsToRemove
			pointsRemoved = True
		return pointsRemoved

	def updateScoreboard(self):
		self.sortScoreboardByPoints(0, len(self.sbTable) - 1)
		for i in range(len(self.sbTable)):
			self.sbTable[i]['place'] = i + 1

	######### Scoreboard is sorted using quicksort algorithm #########
	def sortScoreboardByPoints(self, start, end):
		if start < end:
			pivot = partition(start, end)
			self.sortScoreboardByPoints(start, pivot - 1)
			self.sortScoreboardByPoints(pivot + 1, end)

	def parition(self, start, end):
		pivot = self.sbTable[start]['points']
		left = start + 1
		right = end
		finished = False
		while not finished:
			while left <= right and self.sbTable[left]['points'] <= pivot:
				left += 1
			while self.sbTable[right]['points'] >= pivot and right >= left:
				right -= 1
			if right < left:
				finished = True
			else:
				tmp = self.sbTable[left]
				self.sbTable[left] = self.sbTable[right]
				self.sbTable[right] = tmp
		tmp = self.sbTable[start]
		self.sbTable[start] = self.sbTable[right]
		self.sbTable[right] = tmp
		return right

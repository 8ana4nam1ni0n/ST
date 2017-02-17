
class EventModel(object):
	'This will represent an Event'

	eventName = ''
	eventAvgWeight = 0.0
	eventTotalPoints = 0
	eventDate = ''
	eventType = ''
	eventTasks = []
	eventScoreboard = ''
	eventTeams = []

	def __init__(self, name, avgWeight, totalPoints, date, type, tasks, scoreboard, teams):
		self.eventName = name
		self.eventAvgWeight = avgWeight
		self.eventTotalPoints = totalPoints
		self.eventDate = date
		self.eventType = type
		self.eventTasks = tasks
		self.eventScoreboard = scoreboard
		self.eventTeams = teams

	def __cmp__(self, otherEvent):
		for curr, other in zip(self.__values(), otherEvent.__values()):
			check = cmp(curr, other)
			if check:
				return check
		return 0

	def setName(self, name):
		self.eventName = name

	def setAvgWeight(self, avgWeight):
		self.eventAvgWeight = avgWeight

	def setTotalPoints(self, totalPoints):
		self.eventTotalPoints = totalPoints

	def setDate(self, date):
		self.eventDate = date

	def setType(self, type):
		self.eventType = type

	def setTasks(self, tasks):
		self.eventTasks = tasks

	def setScoreboard(self, scoreboard):
		self.eventScoreboard = scoreboard

	def setTeams(self, teams):
		self.eventTeams = teams

	def getName(self):
		return self.eventName

	def getAvgWeight(self):
		return self.eventAvgWeight

	def getTotalPoints(self):
		return self.eventTotalPoints

	def getDate(self):
		return self.eventDate

	def getType(self):
		return self.eventType

	def getTasks(self):
		return self.eventTasks

	def getScoreboard(self):
		return self.eventScoreboard

	def getTeams(self):
		return self.eventTeams

	########### Team's Related Mehtods ###########
	def registerTeam(self, team):
		registered = False
		if team not in self.eventTeams:
			self.eventTeams.append(team)
			registered = True
		return registered

	########### Tasks's Related Mehtods ###########
	def insertTask(self, task):
		inserted = False
		if task not in self.eventTasks:
			self.eventTasks.append(task)
			inserted = True
		return inserted

	def insertTasks(self, tasksList):
		err = 0
		for task in tasksList:
			if self.insertTask(task):
				continue
			else:
				err += 1
		return err

	def removeTask(self, task):
		removed = False
		if task in self.eventTasks:
			self.eventTasks.remove(task)
			removed = True
		return removed

	def removeByName(self, taskName):
		task = self.searchTaskByName(taskName)
		return removeTask(task)

	def searchTaskByName(self, taskName):
		pos = getTaskPositionByName(taskName)
		return self.eventTasks[pos] if pos >= 0 else pos

	def searchTaskByCategory(self, category):
		tasks = []
		for task in self.eventTasks:
			if task.getCategory() == category:
				tasks.append(task)
		return tasks[0] if len(tasks) == 1 else tasks

	def searchTaskByPoints(self, points):
		tasks = []
		for task in self.eventTasks:
			if task.getPoints() == points:
				tasks.append(task)
		return tasks[0] if len(tasks) == 1 else tasks

	def getTaskPositionByName(self, taskName):
		pos = -1
		for i in range(len(self.eventTasks)):
			if taskName == self.eventTasks[i].getName():
				pos = i
				break
		return pos



	########### Scoreboard's Related Mehtods ###########

	def addTeamPoints(self, teamName, pointsToAdd):
		added = self.eventScoreboard.addTeamPoints(teamName, pointsToAdd)
		if added:
			self.eventScoreboard.updateScoreboard()
		return added

	def removeTeamPoints(self, teamName, pointsToRemove):
		removed = self.eventScoreboard.removeTeamPoints(teamName, pointsToRemove)
		if removed:
			self.eventScoreboard.updateScoreboard()
		return removed

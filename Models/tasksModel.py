
class TaskModel(object):
	'Represents tasks in an event'

	taskName = ''
	taskCategory = ''
	taskPoints = 0

	def __init__(self, name, category, points):
		self.taskName = name
		self.taskCategory = category
		self.taskPoints = points

	def __cmp__(self, otherTask):
		for curr, other in zip(self.__values(), otherTask.__values()):
			check = cmp(curr, other)
			if check:
				return check
		return 0

	def setName(self, name):
		self.taskName = name

	def setCategory(self, category):
		self.taskCategory = category

	def setPoints(self, points):
		self.taskPoints = points

	def getName(self):
		return self.taskName

	def getCategory(self):
		return self.taskCategory

	def getPoints(self):
		return self.taskPoints


class DBModel(object):
	'Represent Database Model'

	dbName = ''
	tables = []

	def __init__(self, name):
		self.dbName = name

	# read

	def setName(self, name):
		self.dbName = name

	def getName(self):
		return self.dbName

	############### Table operations ###############
	def createTable(self, tableName):
		newTable = {tableName: []}
		created = False
		if len(self.tables) == 0 or not self.tableExists(tableName):
			self.tables.append(newTable)
			created = True
		return created

	def tableExists(self, tableName):
		exists = False
		for table in self.tables:
			for tName in table:
				if tName == tableName:
					exists = True
					break
			if exists: break
		return exists

	def deleteTable(self, tableName):
		pos = self.getTablePosition(tableName)
		deleted = False
		if pos >= 0:
			del self.tables[pos]
			deleted = True
		return deleted

	def getTablePosition(self, tableName):
		pos = -1
		for i in range(len(self.tables)):
			if tableName in self.tables[i]:
				pos = i
				break
		return pos

	############### Insert Record Operations ###############
	def insertData(self, tableName, data):
		inserted = False
		pos = self.getTablePosition(tableName)
		if pos >= 0 and not self.recordExists(tableName, pos, data):
			self.tables[pos][tableName].append(data)
			inserted = True
		return inserted

	def recordExists(self, tableName, tablePosition, data):
		exists = False
		if data in self.tables[tablePosition][tableName]:
			exists = True
		return exists

	############### Update Record Operations ###############
	def updateRecordAll(self, tableName, id, data):
		updated = False
		rpos, tpos = self.recordPositionLookUp(tableName, id)
		if rpos >= 0 and data:
			if len(data) == len(self.tables[tpos][tableName][pos]):
				self.tables[tpos][tableName][pos] = data
				updated = True
		return updated

	############### Delete Record Operations ###############
	def removeRecord(self, tableName, id):
		removed = False
		rpos, tpos = self.recordPositionLookUp(tableName, id)
		if rpos >= 0:
			del self.tables[tpos][tableName][rpos]
			removed = True
		return removed

	############### Search Record Operations ###############
	def recordPositionLookUp(self, tableName, id):
		rpos = -1
		tpos = self.getTablePosition(tableName)
		if tpos >= 0:
			for i in range(len(self.tables[tpos][tableName])):
				if self.tables[tpos][tableName][i]['ID'] == id:
					rpos = i
					break
		return rpos, tpos

	def recordLookUp(self, tableName, id):
		record = {}
		pos = self.getTablePosition(tableName)
		if pos >= 0:
			for data in self.tables[pos][tableName]:
				if data['ID'] == id:
					record = data
					break
		return record

	############### Read Record Operations ###############
	def readRecord(self, tableName, id):
		record = self.recordLookUp(tableName, id)
		if record:
			print record
		else:
			print 'record with ID: %d not found!!' % id

	def readAll(self, tableName):
		table = []
		tpos = self.getTablePosition(tableName)
		if tpos >= 0:
			table = self.tables[tpos]
			print table
		else:
			print 'table: %s not found' % teamName

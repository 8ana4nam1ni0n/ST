import playerModel
import teamModel

if __name__ == '__main__':
	player = playerModel.PlayerModel(1, 'Yoshuam', 'yoshuam@mail.com', '1nc0gnito', 1)
	team = teamModel.TeamModel(1, 'name', 'logo', ['aliases'], [player], 50)

	if team.removeMemberByEmail('yoshuam@mail.com'):
		print 'Yeah'
		print team.getMembers()
	else:
		print 'Could not delete'
		print team.getMembers()

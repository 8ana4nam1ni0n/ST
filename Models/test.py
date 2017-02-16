import playerModel

if __name__ == '__main__':
	player = playerModel.PlayerModel(1, 'Yoshuam', 'yoshuam@mail.com', '1nc0gnito', 1)
	print str(player.hasTeam())

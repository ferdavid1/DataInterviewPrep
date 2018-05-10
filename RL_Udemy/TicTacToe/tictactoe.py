import numpy as np
# play_game(p1, p2, env)
class Bandit(object):
	def __init__(self):
		pass
class env():
	def __init__(self):
		pass
	def game_over(self):
		pass
	def draw_board(self):
		pass


def play_game(p1, p2, env, draw=False):
	current_player = None
	while not env.game_over():
		if current_player == p1:
			current_player = p2
		else:
			current_player = p1

		if draw:
			env.draw_board()

		current_player.take_action(env)

		state = env.get_state()
		p1.update_state_history(state)
		p2.update_state_history(state)

	if draw:
		env.draw_board()

	p1.update(env)
	p2.update(env)




if __name__ == '__main__':
	# p1 = Bandit(1)
	# p2 = Bandit(2)
	env = np.array([['-']*3, ['-']*3, ['-']*3])
	print(env)
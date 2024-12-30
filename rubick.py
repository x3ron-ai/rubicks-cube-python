colors = ['red', 'blue', 'white', 'green', 'yellow', 'orange']

class Fragment:
	color = 'default'
	def __init__(self,color):
		self.color = color

	def __str__(self):
		return self.color[0]

	def __repr__(self):
		return self.color[0]

class Site:
	fragments = []
	def __init__(self, fragments):
		self.fragments = fragments

	def get_site(self):
		resp = [self.fragments[i:i+3] for i in range(0, len(self.fragments), 3)]
		return resp

	def __str__(self):
		resp = ''
		for i in self.get_site():
			for y in range(3):
				resp+=i[y].color[0]
			resp+='\n'
		return resp[:-1]


	def transpose(self, revert):
		if revert:
			self.fragments = [self.fragments[i] for i in (6, 3, 0, 7, 4, 1, 8, 5, 2)]
		else:
			self.fragments = [self.fragments[i] for i in (2, 5, 8, 1, 4, 7, 0, 3, 6)]

	def select(self, *args):
		return [self.fragments[i] for i in args]

	def put(self, indexes, vals):
		for i in range(len(indexes)):
			self.fragments[indexes[i]] = vals[i]
		return self

	# получение вертикалей и горизонталей кубика
	def get_top_row(self):
		return self.fragments[:3]

	def get_mid_row(self):
		return self.fragments[3:6]

	def get_bot_row(self):
		return self.fragments[6:9]

	def get_left_column(self):
		return [self.fragments[i] for i in range(0,3,6)]

	def get_mid_column(self):
		return [self.fragments[i] for i in range(1,4,7)]

	def get_right_column(self):
		return [self.fragments[i] for i in range(2,5,8)]
		
def frag_str(frag_seq):
	return "".join(map(str, frag_seq))

class RCube:
	fragments = []
	sites = []
	def __init__(self):

		for i in colors:
			_fragments = []
			for _ in range(9):
				self.fragments.append(Fragment(i))
				_fragments.append(Fragment(i))
			self.sites.append(Site(_fragments))



	def get_sites(self):
		"""0 - up, 1 - front, 2 - right, 3 - back, 4 - left, 5 - down"""
		return self.sites

	def make_u_move(self, i=True):
		# Получаем грани
		up_side = self.sites[0]
		front_side = self.sites[1]
		right_side = self.sites[2]
		back_side = self.sites[3]
		left_side = self.sites[4]
		down_side = self.sites[5]

		up_side.transpose(i)

		if i:
			front_temp = front_side.select(0,1,2)
			front_side.put((0,1,2), (right_side.select(0,1,2)))
			right_side.put((0,1,2), (back_side.select(0,1,2)))
			back_side.put((0,1,2), (left_side.select(0,1,2)))
			left_side.put((0,1,2), (front_temp))
		else:
			front_temp = front_side.select(0,1,2)
			front_side.put((0,1,2), (left_side.select(0,1,2)))
			left_side.put((0,1,2), (back_side.select(0,1,2)))
			back_side.put((0,1,2), (right_side.select(0,1,2)))
			right_side.put((0,1,2), (front_temp))
		self.sites = [up_side, front_side, right_side, back_side, left_side, down_side]

	def make_f_move(self, i=True):
		up_side = self.sites[0]
		front_side = self.sites[1]
		right_side = self.sites[2]
		back_side = self.sites[3]
		left_side = self.sites[4]
		down_side = self.sites[5]

		front_side.transpose(i)

		if i:
			up_temp = up_side.select(6,7,8)
			up_side.put((6,7,8), left_side.select(8,5,2))
			left_side.put((8,5,2), down_side.select(8,5,2))
			down_side.put((8,5,2),  right_side.select(0,3,6))
			right_side.put((0,3,6), up_temp)
		else:
			up_temp = up_side.select(6,7,8)
			up_side.put((6,7,8), right_side.select(0,3,6))
			right_side.put((0,3,6), down_side.select(8,5,2))
			down_side.put((8,5,2),  left_side.select(8,5,2))
			left_side.put((8,5,2), up_temp)

		self.sites = [up_side, front_side, right_side, back_side, left_side, down_side]

	def make_r_move(self, i=True):
		up_side = self.sites[0]
		front_side = self.sites[1]
		right_side = self.sites[2]
		back_side = self.sites[3]
		left_side = self.sites[4]
		down_side = self.sites[5]

		right_side.transpose(i)
		if i:
			up_temp = up_side.select(8,5,2)
			up_side.put((8,5,2), front_side.select(8,5,2))
			front_side.put((8,5,2), down_side.select(6,7,8))
			down_side.put((6,7,8), back_side.select(0,3,6))
			back_side.put((0,3,6), up_temp)
		else:
			up_temp = up_side.select(8,5,2)
			up_side.put((8,5,2), back_side.select(0,3,6))
			back_side.put((0,3,6), down_side.select(6,7,8))
			down_side.put((6,7,8), front_side.select(8,5,2))
			front_side.put((8,5,2), up_temp)

		self.sites = [up_side, front_side, right_side, back_side, left_side, down_side]

	def make_b_move(self, i=True):
		up_side = self.sites[0]
		front_side = self.sites[1]
		right_side = self.sites[2]
		back_side = self.sites[3]
		left_side = self.sites[4]
		down_side = self.sites[5]

		back_side.transpose(i)
		if i:
			down_temp = down_side.select(0,3,6)
			down_side.put((0,3,6), left_side.select(0,3,6))
			left_side.put((0,3,6), up_side.select(2,1,0))
			up_side.put((2,1,0), right_side.select(8,5,2))
			right_side.put((8,5,2), down_temp)
		else:
			down_temp = down_side.select(0,3,6)
			down_side.put((0,3,6), right_side.select(8,5,2))
			right_side.put((8,5,2), up_side.select(2,1,0))
			up_side.put((2,1,0), left_side.select(0,3,6))
			left_side.put((0,3,6), down_temp)


		self.sites = [up_side, front_side, right_side, back_side, left_side, down_side]

	def make_l_move(self, i=True):
		up_side = self.sites[0]
		front_side = self.sites[1]
		right_side = self.sites[2]
		back_side = self.sites[3]
		left_side = self.sites[4]
		down_side = self.sites[5]

		left_side.transpose(i)

		if i:
			up_temp = up_side.select(0,3,6)
			up_side.put((0,3,6), back_side.select(8,5,2))
			back_side.put((8,5,2), down_side.select(2,1,0))
			down_side.put((2,1,0), front_side.select(0,3,6))
			front_side.put((0,3,6), up_temp)
		else:
			up_temp = up_side.select(0,3,6)
			up_side.put((0,3,6), front_side.select(0,3,6))
			front_side.put((0,3,6), down_side.select(2,1,0))
			down_side.put((2,1,0), back_side.select(8,5,2))
			back_side.put((8,5,2), up_temp)

		self.sites = [up_side, front_side, right_side, back_side, left_side, down_side]

	def make_d_move(self, i=True):
		up_side = self.sites[0]
		front_side = self.sites[1]
		right_side = self.sites[2]
		back_side = self.sites[3]
		left_side = self.sites[4]
		down_side = self.sites[5]

		down_side.transpose(i)

		if i:
			front_temp = front_side.select(6,7,8)
			front_side.put((6,7,8), left_side.select(6,7,8))
			left_side.put((6,7,8), back_side.select(6,7,8))
			back_side.put((6,7,8), right_side.select(6,7,8))
			right_side.put((6,7,8), front_temp)
		else:
			front_temp = front_side.select(6,7,8)
			front_side.put((6,7,8), right_side.select(6,7,8))
			right_side.put((6,7,8), back_side.select(6,7,8))
			back_side.put((6,7,8), left_side.select(6,7,8))
			left_side.put((6,7,8), front_temp)

		self.sites = [up_side, front_side, right_side, back_side, left_side, down_side]

	def cool_show(self):
		response = ''
		response += str(self.sites[0]) + '\n\n'
		response += frag_str(self.sites[1].get_top_row())+' '
		response += frag_str(self.sites[2].get_top_row())+' '
		response += frag_str(self.sites[3].get_top_row())+' '
		response += frag_str(self.sites[4].get_top_row())+'\n'

		response += frag_str(self.sites[1].get_mid_row())+' '
		response += frag_str(self.sites[2].get_mid_row())+' '
		response += frag_str(self.sites[3].get_mid_row())+' '
		response += frag_str(self.sites[4].get_mid_row())+'\n'
		
		response += frag_str(self.sites[1].get_bot_row())+' '
		response += frag_str(self.sites[2].get_bot_row())+' '
		response += frag_str(self.sites[3].get_bot_row())+' '
		response += frag_str(self.sites[4].get_bot_row())+'\n\n'

		response += 12*' ' + frag_str(self.sites[5].get_top_row()) + '\n'
		response += 12*' ' + frag_str(self.sites[5].get_mid_row()) + '\n'
		response += 12*' ' + frag_str(self.sites[5].get_bot_row()) + '\n'
		
		return response

if __name__ == "__main__":
	cube = RCube()

	while True:
		print(cube.cool_show())
		move = input("Moving ((u)p, (f)ront, (r)ight, (b)ack, (l)eft, (d)own): ")	
		match move:
			case 'u':
				cube.make_u_move()
			case 'f':
				cube.make_f_move()
			case 'r':
				cube.make_r_move()
			case 'b':
				cube.make_b_move()
			case 'l':
				cube.make_l_move()
			case 'd':
				cube.make_d_move()
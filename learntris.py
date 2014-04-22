def command_split(user_command):
	commands = list(user_command)
	i = 0
	while i < len(commands):
		if commands[i].isspace() is True:
			commands.pop(i)
		i = i + 1
	i = 0
	while i < len(commands):
		if commands[i] == '?':
			commands[i] += commands.pop(i+1)
		i = i + 1
	return commands
	
def initialize_grid():
	i = 0
	grid = []
	for i in range(22):
		grid.append(". "*10)
	return grid

def print_grid(grid):
	print '\n'.join(grid)

def spawn_tetra(grid, active_tetramino):
	i = 0
	if len(active_tetramino) < 4:
		while i < len(active_tetramino):
			s = list(grid[i])
			s_add = list(active_tetramino[i])
			tetra_len = len(s_add)+1
			x = 1
			while x < tetra_len:
				s[-8-x] = s_add[-x]
				x = x + 1
			s = ''.join(s)
			grid[i] = s.upper()
			i = i + 1
	else:
		while i < len(active_tetramino):
			s = list(grid[i])
			s_add = list(active_tetramino[i])
			tetra_len = len(s_add)+1
			x = 1
			while x < tetra_len:
				s[-6-x] = s_add[-x]
				x = x + 1
			s = ''.join(s)
			grid[i] = s.upper()
			i = i + 1	
	return grid, active_tetramino
	
def given():
	line_count = 0
	user_input = []
	while len(user_input) < 22:
		line = raw_input("")
		user_input.append(line)
	return user_input

def step(grid, score, clearedlines):
	i = 0
	for i in range(len(grid)):
		if '.' in grid[i]:
			pass
		else:
			grid[i] = ". "*10
			score = score + 100
			clearedlines = clearedlines + 1
	return grid, score, clearedlines

def set_tetramino(tetramino):
	active_tetramino = []
	if tetramino == 'I':
		active_tetramino = ['. . . . ', 'c c c c ', '. . . . ', '. . . . ']
	elif tetramino == 'O':
		active_tetramino = ['y y ', 'y y ']
	elif tetramino == 'Z':
		active_tetramino = ['r r . ', '. r r ', '. . . ']
	elif tetramino == 'S':
		active_tetramino = ['. g g ', 'g g . ', '. . . ']
	elif tetramino == 'J':
		active_tetramino = ['b . . ', 'b b b ', '. . . ']
	elif tetramino == 'L':
		active_tetramino = ['. . o ', 'o o o ', '. . . ']
	elif tetramino == 'T':
		active_tetramino = ['. m . ', 'm m m ', '. . . ']
	else:
		pass
	return active_tetramino
	
def display_tetramino(active_tetramino):
	print '\n'.join(active_tetramino)
	
def clear():	
	i = 0
	grid = []
	for i in range(22):
		grid.append(". "*10)
	return (grid)

def rotate_ccw(active_tetramino):
	tetra_rotate = []
	for i in range(len(active_tetramino)):
		tetra_rotate.append(active_tetramino[i].split())
	temp_tetramino = []
	#active_tetramino = []
	#for i in range(len(tetra_rotate)):
		#temp_tetramino.append(' ')
	last_col = len(tetra_rotate) - 1
	for i in range(len(tetra_rotate)):
		for j in range(len(tetra_rotate)):
			if j == 0:
			#temp_tetramino[j] = tetra_rotate[j][i]
				temp_tetramino.append(tetra_rotate[j][last_col-i] + ' ')
			else:
				temp_tetramino[i] = temp_tetramino[i] + (tetra_rotate[j][last_col-i] + ' ')
		#active_tetramino.append(temp_tetramino)
	return temp_tetramino

def rotate_cw(active_tetramino):
	tetra_rotate = []
	for i in range(len(active_tetramino)):
		tetra_rotate.append(active_tetramino[i].split())
	temp_tetramino = []
	#active_tetramino = []
	#for i in range(len(tetra_rotate)):
		#temp_tetramino.append(' ')
	last_col = len(tetra_rotate) - 1
	for i in range(len(tetra_rotate)):
		for j in range(len(tetra_rotate)):
			if j == 0:
			#temp_tetramino[j] = tetra_rotate[j][i]
				temp_tetramino.append(tetra_rotate[last_col-j][i] + ' ')
			else:
				temp_tetramino[i] = temp_tetramino[i] + (tetra_rotate[last_col-j][i] + ' ')
		#active_tetramino.append(temp_tetramino)
	return temp_tetramino

def nudge_left(grid, active_tetramino):
	row = 0
	if (
		grid[row][:len(active_tetramino[row])] != active_tetramino[row].upper() and 
		grid[row+1][:len(active_tetramino[row+1])] != active_tetramino[row+1].upper()
		):
		# Check that the 'spawning' area isn't equal to the active tetramino to
		# ensure you collide with the left wall
		while row < len(active_tetramino):

			i = 0
			s = list(grid[row])
			while i < len(s):
				if i == (len(s)-2):
					s[i] = '.'
					#s[i] = s[0]
				elif i == (len(s)-1):
					s[i] = ' '
					#s[i] = s[1]
				else:
					s[i] = s[i+2]
				i += 1
				# print ''.join(s)
				# raw_input()
			s = ''.join(s)
			grid[row] = s
			row += 1
			
	else:
		pass
	return grid
	
def nudge_right(grid, active_tetramino):
	row = 0
	if (
		(active_tetramino[row][len(active_tetramino[row])-2:] == '. ' and 
		active_tetramino[row+1][len(active_tetramino[row])-2:] == '. ')
		):
		# Check that the 'tetramino' isn't all '. ' on the right side, erroneously causing it to stop moving
		if (
		grid[row][-len(active_tetramino[row])+2:] != active_tetramino[row][:len(active_tetramino[row])-2].upper() 
		and 
		grid[row+1][-len(active_tetramino[row+1])+2:] != active_tetramino[row+1][:len(active_tetramino[row])-2].upper()
		):
			# Check that the 'spawning' area isn't equal to the active tetramino,
			# minus the row which is all '. ', to ensure you collide with the right wall
			while row < len(active_tetramino):
				s = list(grid[row])
				i = len(s)-1
				while i >= 0:
					if i == 0:
						s[i] = '.'
						# s[i] = s[len(s)-2]
					elif i == 1:
						s[i] = ' '
						# s[i] = s[len(s)-1]
					else:
						s[i] = s[i-2]
					i -= 1
				s = ''.join(s)
				grid[row] = s
				row += 1
		else:
			pass
	elif (
	grid[row][-len(active_tetramino[row]):] != active_tetramino[row].upper() 
	and grid[row+1][-len(active_tetramino[row+1]):] != active_tetramino[row+1].upper()
	):
		# Check that the 'spawning' area isn't equal to the active tetramino to
		# ensure you collide with the right wall
		while row < len(active_tetramino):
			s = list(grid[row])
			i = len(s)-1
			while i >= 0:
				if i == 0:
					s[i] = '.'
					# s[i] = s[len(s)-2]
				elif i == 1:
					s[i] = ' '
					# s[i] = s[len(s)-1]
				else:
					s[i] = s[i-2]
				i -= 1
			s = ''.join(s)
			grid[row] = s
			row += 1
	else:
		pass
	return grid	

def nudge_down(grid):
	row = 0
	s = []
	while row < 2:
		s.append(grid[row])
		row += 1
	row -= 1
	grid[row-1] = '. '*10
	i = 0
	while i < len(s):
		grid[row] = s[i]
		row += 1
		i += 1
	return grid

def quit():
	pass
	
def execute(grid, score, clearedlines, active_tetramino):

	i = 0
	user_command = raw_input("")
	commands = command_split(user_command)
	command_length = len(commands)
	index_length = command_length - 1
	
	while i < command_length:
		if commands[i] == 'p':
			print_grid(grid)
		elif commands[i] == 'g':
			grid = given()
		elif commands[i] == 'P':
			print_grid(grid)
		elif commands[i] == 'c':
			grid = clear()
		elif commands[i] == 's':
			grid, score, clearedlines = step(grid, score, clearedlines)
		elif commands[i] == '?s':
			print score
		elif commands[i] == '?n':
			print clearedlines
		elif commands[i] in {'I', 'O', 'Z', 'S', 'J', 'L', 'T'}:
			tetramino = commands[i]
			active_tetramino = set_tetramino(tetramino)
			grid, active_tetramino = spawn_tetra(grid, active_tetramino)
		elif commands[i] == ')':
			active_tetramino = rotate_cw(active_tetramino)
			grid, active_tetramino = spawn_tetra(grid, active_tetramino)
		elif commands[i] == '(':
			active_tetramino = rotate_ccw(active_tetramino)
			grid, active_tetramino = spawn_tetra(grid, active_tetramino)
		elif commands[i] == '<':
			grid = nudge_left(grid, active_tetramino)
		elif commands[i] == '>':
			grid = nudge_right(grid, active_tetramino)
		elif commands[i] == 'v':
			grid = nudge_down(grid)
		elif commands[i] == 't':
			display_tetramino(active_tetramino)
		elif commands[i] == 'q':
			quit()
		else:
			print ""
		i = i + 1
		
	if commands == []:
		execute(grid, score, clearedlines, active_tetramino)
	elif commands[index_length] != 'q':
		execute(grid, score, clearedlines, active_tetramino)
	else:
		quit()

grid = initialize_grid()
score = 0
clearedlines = 0
active_tetramino = ''

execute(grid, score, clearedlines, active_tetramino)
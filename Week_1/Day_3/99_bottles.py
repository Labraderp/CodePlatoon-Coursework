def bottle_song():
	for i in range(99,2,-1):
		print(f'{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i-1} bottles of beer on the wall.')
	
	print(f'1 more bottle of beer on the wall, 1 more bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.')
	print(f'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')

bottle_song()
import math,pyperclip

def decryptMessage(key, message):
	numofcol = math.ceil(len(message)/key)#列
	print(numofcol)
	numofrow = key#行
	shadow = (numofcol*numofrow)-len(message)
	
	plaintext = ['']*numofcol#密文
	col = 0
	row = 0
	for i in message:
		plaintext[col] += i
		col += 1
		if(col == numofcol) or (col == numofcol-1 and row >= numofrow-shadow):
			col = 0
			row += 1
			print(plaintext)
	return ''.join(plaintext)

mymessage = 'Cenoonommstmme oo snnio. s s c'
mykey = 8
plaintext = decryptMessage(mykey,mymessage)
print(plaintext+'|')
pyperclip.copy(plaintext)
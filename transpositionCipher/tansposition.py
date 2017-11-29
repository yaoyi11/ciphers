import pyperclip
 		
def encryptMessage(message, key):
	ctext = [''] * key
	for i in range(key):
		pointer = i
		while pointer < len(message):
			ctext[i] += message[pointer]
			pointer += key
	return ''.join(ctext)
	
Mymessage = 'Common sense is not so common.'
mykey = 8
cipertext = encryptMessage(Mymessage,mykey)
print(cipertext+'|')
	
pyperclip.copy(cipertext)
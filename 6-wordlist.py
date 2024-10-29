fin = open('words.txt')

for line in fin:
	word = line.strip()				#strip off newline character
	if word[0] == 'a' and word[-3:] == 'mie':	#words beginning with 'a' and ending with 'mie'
		print(word)

sent = open('sentences.txt')
for line in sent:
	#sentence = line.strip()
	print(line)

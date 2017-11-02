with open('in.txt', 'r') as f_in:
	input_text = f_in.read()
sentences = input_text.split('.')
output_text = ""
for index in range(0, 4):
	senten = sentences[index]
	words = senten.split(' ') 
	words.reverse()
	senten = ' '.join(words)
	output_text = output_text + senten
	print(senten)	
with open('out.txt', 'w') as f_out:
	f_out.write(output_text)
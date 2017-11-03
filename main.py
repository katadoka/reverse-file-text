with open('in.txt', 'r') as f_in:
	input_text = f_in.read()
sentences = input_text.split('.')
output_text = ''
point = '.'
for index in range(0, 4):
	sentence = sentences[index]
	words = sentence.split(' ') 
	words.reverse()
	sentence = ' '.join(words)	
	output_text = output_text + sentence + point
	print(sentence + point)	
with open('out.txt', 'w') as f_out:
	f_out.write(output_text)	
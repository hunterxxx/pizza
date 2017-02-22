from collections import Counter
from itertools import islice

cnt = Counter()
done=[]



text = 'medium.in'
def split_line(text):
	with open(text) as f:
		for line in islice(f, 1, 16):
		#lines = f.readlines()
			return line
	#print lines
	#for line in lines:
	#	words = line.split()
	#	return words

def count_ingredient(wordList):
	for words in wordList:
		for letters in set(words):
			cnt[letters]+=1
			done.append(words)
		if cnt[words] < 13:	
			if cnt['T'] > 3 and cnt['M'] > 3:		
				break

if __name__ == '__main__':			
	count_ingredient(split_line(text))
	print cnt['T']
	print cnt['M']
	print done



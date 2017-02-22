from collections import Counter


text = 'medium.in'
def split_line(text):
with open(text) as f:
	lines = f.readlines()
	#print lines
	for line in lines:
		words = line.split()

done=[]
wordList='TMMMTTTMMMMTTTTTTMM'
cnt = Counter()
for words in wordList:
	for letters in set(words):
		cnt[letters]+=1
		done.append(words)
	if cnt[words] < 13:	
		if cnt['T'] > 3 and cnt['M'] > 3:		
			break

print cnt['T']
print cnt['M']
print done

#split_line(pizza)

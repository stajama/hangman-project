import random
library = ['acres',
		   'adult',
		   'advice',
		   'arrangement',
		   'attempt',
		   'august',
		   'autumn',
		   'border',
		   'breeze',
		   'brick',
		   'calm',
		   'canal',
		   'casey',
		   'cast',
		   'chose',
		   'claws',
		   'coach',
		   'constantly',
		   'contrast',
		   'cookies',
		   'customs',
		   'damage',
		   'danny',
		   'deeply',
		   'depth',
		   'discussion',
		   'doll',
		   'donkey',
		   'egypt',
		   'ellen',
		   'essential',
		   'exchange',
		   'exist',
		   'explanation',
		   'facing',
		   'film',
		   'finest',
		   'fireplace',
		   'floating',
		   'folks',
		   'fort',
		   'garage',
		   'grabbed',
		   'grandmother',
		   'habit',
		   'happily',
		   'harry',
		   'heading',
		   'hunter',
		   'illinois',
		   'image',
		   'independent',
		   'instant',
		   'january',
		   'kids',
		   'label',
		   'lee',
		   'lungs',
		   'manufacturing',
		   'martin',
		   'mathematics',
		   'melted',
		   'memory',
		   'mill',
		   'mission',
		   'monkey',
		   'mount',
		   'mysterious',
		   'neighborhood',
		   'norway',
		   'nuts',
		   'occasionally',
		   'official',
		   'ourselves',
		   'palace',
		   'pennsylvania',
		   'philadelphia',
		   'plates',
		   'poetry',
		   'policeman',
		   'positive',
		   'possibly',
		   'practical',
		   'pride',
		   'promised',
		   'recall',
		   'relationship',
		   'remarkable',
		   'require',
		   'rhyme',
		   'rocky',
		   'rubbed',
		   'rush',
		   'sale',
		   'satellites',
		   'satisfied',
		   'scared',
		   'selection',
		   'shake',
		   'shaking',
		   'shallow',
		   'shout',
		   'silly',
		   'simplest',
		   'slight',
		   'slip',
		   'slope',
		   'soap',
		   'solar',
		   'species',
		   'spin',
		   'stiff',
		   'swung',
		   'tales',
		   'thumb',
		   'tobacco',
		   'toy',
		   'trap',
		   'treated',
		   'tune',
		   'university',
		   'vapor',
		   'vessels',
		   'wealth',
		   'wolf',
		   'zoo']


def displayer(word,guesslist,strikes):
	printlist = (' _'*len(word))+'  '
	for letter in range(len(word)):
		if word[letter] in guesslist:
			printlist = printlist[:(letter*2+1)]+word[letter]+printlist[(letter*2+2):]
	print(printlist)
	triedlist=''
	for alpha in "abcdefghijklmnopqrstuvwxyz":
		if alpha in guesslist:
			triedlist += alpha
		else:
			triedlist += ' '
	print(['',' =',' ==',' ==\n l',' ==\n l\n l',' ==\n l\n l\n 0',' ==\n l\n l\n 0\n\\',' ==\n l\n l\n 0\n\\!',' ==\n l\n l\n 0\n\\!/',' ==\n l\n l\n 0\n\\!/\n i',' ==\n l\n l\n 0\n\\!/\n i\n /',' ==\n l\n l\n 0\n\\!/\n i\n /\\'][strikes])
	return

def setup():
	pname = input("Enter your name")
	score = 0
	return pname,score
	
def lettercheck(word,letter):
	if letter in word:
		return True
	else:
		return False
		
def endgame(word,guesslist):
	for letter in word:
		if not letter in guesslist:
			return False
	return True
	
def game(word,pname):
	strikes =0
	guesslist = []
	while strikes <=11:
		displayer(word,guesslist,strikes)
		check = input("Take a guess.")
		if len(check)>1:
			print("One Letter Only")
			continue
		elif check in guesslist:
			print("Already tried, pick again.")
			continue
		guesslist.append(check)
		if lettercheck(word,check):
			print("CORRECT")
		else:
			strikes+=1
			print("FAIL")
		if endgame(word,guesslist)==True:			
			print("Congratulations, "+ pname +". You win")
			points = (len(word)*100)-(len(guesslist)*10)
			print("Gained "+str(points)+" points.")
			return points
		else:
			continue
	print("Better luck next time, "+ pname +".\n0 points")
	return 0

def hangman():
	pname,score=setup()
	while True:
		print('Score: '+str(score))
		keepplay=input("Ready?")
		if keepplay in ['no','No','n','N']:
			break
		word = library[random.randint(0,len(library)-1)]
		score+=game(word,pname)
	
if __name__ == "__main__":
  hangman()   	
	

import collections
import copy
#The women that the men favors
favor_of_men = {			
	'm1': 	['w1', 'w2', 'w3', 'w4'],  #w:women        #tuuples
	'm2': 	['w2', 'w1', 'w4', 'w3'], 
	'm3': 	['w2', 'w4', 'w3', 'w1'],
	'm4': 	['w1', 'w2', 'w3', 'w4']
}

#The men that the women favors
favor_of_women = {
	'w1': 	['m1', 'm3', 'm4', 'm2'],
	'w2': 	['m1', 'm3', 'm4', 'm2'],	#m:man  
	'w3':  	['m4', 'm2', 'm1', 'm3'],
	'w4':	['m1', 'm2', 'm4', 'm3'] 
}




#Not certain but this may end up as a couple
temporary_couples 	= [ ]

#Still does not have match
single_men = [ ]

def create_single_man():
	
	for man in iter(favor_of_men.keys()): #iteration function in python
		single_men.append(man)



def stable_matching_algorithm():
	while (len(single_men) > 0):
		for man in single_men:
			match(man)


def match(man):

	print("DEALING WITH %s"%(man))
	for woman in favor_of_men[man]: # in python is interpreter 

		
		bool_match = [couple for couple in temporary_couples if woman in couple]

		if (len(bool_match) == 0):
			
			temporary_couples.append([man, woman])
			single_men.remove(man)
			print('%s not single anymore he is couple with %s'%(man, woman))
			break

		elif (len(bool_match) > 0):
			print('%s has a bf, sorry dude'%(woman))

			woman_current_mate = favor_of_women[woman].index(bool_match[0][0])
			potential_guy = favor_of_women[woman].index(man)

			if (woman_current_mate < potential_guy):
				print("She has a better bf %s.."%(bool_match[0][0]))
			else: 
				print('Woman chooses %s over %s'%(man, bool_match[0][0]))
				print(' %s is single again.. and has potential %s and %s'%(bool_match[0][0], man, woman))
				
				
				single_men.remove(man)
				single_men.append(bool_match[0][0])
				bool_match[0][0] = man
				break

#### Main
print('Creation of single men:')
create_single_man()
print('Single men: %s'%(single_men))
stable_matching_algorithm()
print('Final Couples: %s'%(temporary_couples))

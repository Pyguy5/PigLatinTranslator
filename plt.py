pyg = 'ay'
o_sent = raw_input("What would you like to translate? No symbols please")
#User input
l_osent = o_sent.lower()
#Simplifies things
n_word = []
t_sent = []
#empty lists for later
n_word = l_osent.split(" ")
#splits the string into a list
for n in n_word:
	if n.isalpha():
		f_letter = n[0]
        #takes the first letter
		f_w = n[1:] + f_letter + pyg
        #concatenates the word minus the first letter, with the first letter and ay
		t_sent.append(f_w)
        #adds it to the list
        else:
            print "All numbers must be spelled out."
            #in case someone inputs numbers

f = " ".join(t_sent)
#reforms the string
print f

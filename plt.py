pyg = 'ay'
o_sent = raw_input("What would you like to translate? No symbols please")
l_osent = o_sent.lower()
sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(" , ")"]
n_word = []
t_sent = []
n_word = l_osent.split(" ")
for n in n_word:
	if n.isalpha():
		f_letter = n[0]
		f_w = n[1:] + f_letter + pyg
		t_sent.append(f_w)
        else:
            print "All numbers must be spelled out."
	

f = " ".join(t_sent)
print f

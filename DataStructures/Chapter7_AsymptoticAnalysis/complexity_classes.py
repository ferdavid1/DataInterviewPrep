# a complexity class is a set of problems with related complexity. 
	# a 'reduction' is a transformation of one problem into another that is at least as difficult as the original

# P 
# p is the complexity class of decision problems that can be solved on a deterministic Turing machine,
	# in polynomial time (at worst case).
# if we can turn a problem into a decision problem, it belongs in P

# NP
# np is the complexity class of decision problems that can be solved on a nondeterministic turing machine in polynomial time (in the worst case)
# a problem is called complete if all problems in the class are reduced to NP.
	# this is called NP-Complete
		# this subclass contains the hardest problems in NP
# any problem that is at least as hard (determined by polynomial time reduction) as any problem in NP,
	# but isn't necessarily by force in NP class, is called NP-hard
	# ex of NP-hard:
		# finding the shortest route through a graph (traveling salesman problem)

# P = NP???
# the class co-NP is the class of the complements of NP problems.
	# for every 'yes' answer, we have the 'no', and vice versa
	# if NP is truly assymetric, then these two classes are different
		# but because their intersection contains all of P, there is some overlap
# if we found a solution to a NP-Complete problem in Polynomial time, NP = Co-NP, and thus P = NP
	# we could solve any NP-hard problem in polynomial time


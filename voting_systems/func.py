import numpy as np



'''
combination: integer 
	A voting combination. Can be expressed in base 2 for num_candidates=2 or in base 3 for num_candidates=3 etc...
num_votes: integer
	Number of voters
num_candidates: integer
	Number of candidates
returns: list of integers
	Each element represents the vote of the i-th voter. 0 for candidate 1, 1 for candidate 2, ..., n for candidate n+1 etc...
''' 
def get_votes(combination, num_voters, num_candidates):
    votes = [0 for i in range(num_voters)]
    for i in range(num_voters):
        votes[num_voters - 1 - i] = combination % num_candidates 
        combination -= votes[num_voters - 1 - i]
        combination /= num_candidates
        combination = int(combination)
    return votes



'''
votes: list of integers
	The same as what get_votes returns.
returns: integer
	The candidate with the most votes.
	
'''
def get_winner(votes):
    return max(set(votes), key=votes.count)



'''
num_votes: integer
	Number of voters
num_candidates: integer
	Number of candidates
returns: list of lists of integers
	Channel matrix W representing the election process channel.
'''
def get_W(num_voters, num_candidates):
    return np.array([[1 if j == get_winner(get_votes(i, num_voters, num_candidates)) else 0 for j in range(num_candidates)]  for i in range(num_candidates ** num_voters)])

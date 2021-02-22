import numpy as np
import itertools
from collections import Counter
import unittest



'''
combination: integer 
	A voting combination. Can be expressed in base 2 for num_candidates=2 or in base 3 for num_candidates=3 etc...
num_votes: integer
	Number of voters.
num_candidates: integer
	Number of candidates.
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
	Number of voters.
num_candidates: integer
	Number of candidates.
returns: list of lists of integers
	Channel matrix W representing the election process channel,
    where only the winning candidate is announced.
'''
def get_W(num_voters, num_candidates):
    return np.array([[1 if j == get_winner(get_votes(i, num_voters, num_candidates)) else 0 for j in range(num_candidates)]  for i in range(num_candidates ** num_voters)])



'''
num_votes: integer
	Number of voters.
num_candidates: integer
	Number of candidates.
returns: list of c-ary tuples (c = num_candidates)
    List of all possible combinations (tuples)
    for the results of elections where they announce the tallies
    for each candidate.
'''
def C_results(num_voters, num_candidates):
    if num_candidates == 0:
        return []
    
    if num_candidates == 1:
        return [(num_voters,)]
    
    if (num_voters == 0):
        return [(0,)*num_candidates]
    
    ret = []
    for i in range(num_voters+1):   
        ret += [(num_voters - i,) + j for j in C_results(i, num_candidates-1)]
    return ret



'''
votes: list of integers
	The same as what get_votes returns.
returns: list num_candidates elements
    List containing the votes for each candidate.
'''
def get_result(votes, num_candidates):
    c = Counter(votes)
    return [c[i] for i in range(num_candidates)]



'''
num_votes: integer
	Number of voters.
num_candidates: integer
	Number of candidates.
returns: list of lists of integers
	Channel matrix C representing the election process channel
    where the tallies for each candidate are announced.
'''
def get_C(num_voters, num_candidates):
    results = C_results(num_voters, num_candidates)    
    return np.array([[1 if tuple(get_result(get_votes(i, num_voters, num_candidates), num_candidates)) == r else 0 for r in results] for i in range(num_candidates ** num_voters)])



def g1(vote, voting_combination, num_voters, num_candidates):
    return int(vote[0] == get_votes(voting_combination, num_voters, num_candidates)[vote[1]])



def get_G1(num_voters, num_candidates):
    return np.array([[g1((c, v), i, num_voters, num_candidates) for i in range(num_candidates ** num_voters)] for c,v in itertools.product(range(num_candidates), range(num_voters))])



def g0(vote, voting_combination, num_voters, num_candidates):
    return int(vote[0] != get_votes(voting_combination, num_voters, num_candidates)[vote[1]])



def get_G0(num_voters, num_candidates):
    return np.array([[g0((c, v), i, num_voters, num_candidates) for i in range(num_candidates ** num_voters)] for c,v in itertools.product(range(num_candidates), range(num_voters))])



class Test(unittest.TestCase):
    
    
    def test_get_W(self):
        correct1 = np.array([
            [1, 0],
            [1, 0],
            [1, 0],
            [0, 1],
            [1, 0],
            [0, 1],
            [0, 1],
            [0, 1],
        ])
        self.assertTrue((get_W(3, 2) == correct1).all())
        
        correct3 = np.array([
          [1],  
        ])
        self.assertTrue((get_W(1, 1) == correct3).all())
    
    
    def test_get_C_(self):
        correct1 = np.array([
            [1, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 1], 
        ])
        self.assertTrue((get_C(3, 2) == correct1).all())
        
        correct2 = np.array([
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
        ])
        self.assertTrue((get_C(2, 3) == correct2).all())
        
        correct3 = np.array([
          [1],  
        ])
        self.assertTrue((get_C(1, 1) == correct3).all())
        
    
    
if __name__ == "__main__":
    unittest.main()
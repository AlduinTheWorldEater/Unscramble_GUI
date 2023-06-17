#Rudimentary scrabbler

from sys import stdin
from itertools import combinations as comb
from utils import *
from collections import defaultdict as dd

# Global dictionary to store the vectorized dictionary just once, in the cache.
indic = dict()

with open("./dictio.txt", 'r') as dic:

    dicr = dic.readlines()
    dic.close()

    indic = dict_intify(dicr)

# Function to get all possible unscrambled words, as a dictionary of ordered lists
# are separated by their lengths as the dictionary keys

def get_unscrambled_words(wordle: str) -> "Dictioinary of sets of words \
keyed by number of letters":

    wordle = wordle.upper()
    ans_dict = dd(set)

    for l in range(3, len(wordle) + 1):
        
        for word in comb(wordle, l): #Creates mathematical combinations of letters. Used instead
                                     # of permuutations to ensure no recomputation

            invec = vector_intify(vectorize(word)) # Vectorize the word entered

            ans_dict[l].update(set(indic.get(invec, ""))) #Get all possible hits for the word vector

        ans_dict[l] = sorted(ans_dict[l]) # Separate the lists and sort them, based on word lengths     

    return ans_dict


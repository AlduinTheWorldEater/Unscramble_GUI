#Utilities file, used to store those functions that are called as subroutines of the main function.

# Converts a word to a list (of exactly 26 elements) of counts of letters.
def vectorize(word_list: "List/string of uppercase letters"):

    alpha = [chr(i) for i in range(65, 91)]
    vector = [0] * 26

    for i in range(len(word_list)):

        if word_list[i] not in alpha:
            raise ValueError(f"Paramater {i}: {word_list[i]} is not a list \
of uppercase letters!")

        vector[ord(word_list[i]) - 65] += 1

    return vector

# Function to convert such a count vector of a word to an integer based on a planned process
def vector_intify(vect: "List of 26 integers"):

    ans = 0

    for i in range(26):
        ans += vect[i] * (2 ** (4 * i)) ## 4^i is used here to indicate that
                                        ## the program can handle a maximum of three repeated letters.
                                        ## More thn three repeated letters leads to wrong answers.   
    return ans

# Function to vectorize a dictionary list of words in the same format as given above.
def dict_intify(input_dic: "Dictionary list of words"):

    return_dict = {}
    
    for i in range(len(input_dic)):

        input_dic[i] = input_dic[i].strip()
        
        int_word = vector_intify(vectorize(input_dic[i]))

        if int_word in return_dict:
            (return_dict.get(int_word)).append(input_dic[i])
            
        elif int_word not in return_dict:
            return_dict[int_word] = [input_dic[i]]
            
    return return_dict

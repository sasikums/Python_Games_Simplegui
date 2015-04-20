"""
Student code for Word Wrangler game
Direct Link 
http://www.codeskulptor.org/#user39_Kmqq0O70Vn_20.py
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"
codeskulptor.set_timeout(40)

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.
    Returns a new sorted list with the same elements in list1, but
    with no duplicates.
    This function can be iterative.
    """ 
    unique_list=[]
    count_dict={}
    
    for dum_elem in list1:
        #if count_dic has a count of 0 for elem add to
        #unique_list, else pass.
        if count_dict.get(dum_elem,0)==0:
            unique_list.append(dum_elem)
            count_dict[dum_elem]=1
     
    #keys of the dictionaries provides a unique list
    #but not sorted
    #return count_dict.keys() 
    return unique_list
    
        
#l=['a','a','a','b','b','c','d','a','e','b','b','b']
#print remove_duplicates(l)

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    #create dictionaries with elements of each list
    dict1={}
    for dum_elem in list1:
        if dict1.get(dum_elem,0)<2:
            dict1[dum_elem] = dict1.get(dum_elem,0)+1
     
    dict2={}
    for dum_elem in list2:
        if dict2.get(dum_elem,0)<2:
            dict2[dum_elem] = dict2.get(dum_elem,0)+1   
    #iterate over shorter dictionary to find
    #common elements
    common_list=[]

    if len(dict1)>len(dict2):
        for key in dict2.keys():
            if dict1.get(key,0)>0 and dict2.get(key,0)>0:
                common_list.append(key)
    else:
        for key in dict1.keys():
            if dict1.get(key,0)>0 and dict2.get(key,0)>0:
                common_list.append(key)
                
    return common_list
#x=[1,3,5,'a',6,'c']
#print intersect(l,x)
            

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """  
    big_list=list1+list2
    
    return merge_sort(big_list) 


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    #sets some initial variables for recursive sort
    sort=[]
    counter=len(list1)
    list_copy=list1[0:counter]
   
    def sort_core(list_copy):
        """
        Recursive portion of sort
    
        """
        if len(list_copy)>0:
            sort.append(min(list_copy))
        if len(sort)==counter:
            return sort
        else:
            list_copy.remove(min(list_copy))
            return sort_core(list_copy)
    
    return sort_core(list_copy)
#testlist=['v','x','a','b','f',1,3,-8]
#print merge_sort(testlist) 
#tlist1=[[3,4,5]]
#tlist2=[[3,4,5]]
#print merge(tlist1,tlist2)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function is recursive. A word, say 'abcd' is entered,
    it is split in to a and bcd and then bcd is run recursively
    though gen_all_strings again, breaking in in to
    b and cd and then in to c and d and then d and "" at which
    point it hits the if condition to return "" and then 
    starts working up the recursion tree.
    
    d then as a first is combined with rest_string '' to make rest_strings be 'd' and
    and ''. Then this version of rest_strings is combined
    with c as the first generate [c,cd,dc] which is combined
    with rest_strings. Then b takes on the role of first
    and is combined with ["",d,c,cd,dc] and so on to a.
    
    Essentially rest_string is built as all possible combinations
    of the last letter, then last 2 letter, then last 3 letters
    and so on. The possibility set is increased each time by inserting
    the next letter with all previous possible combos
    
    """
    if word=="":
        return [""]
    else:
        first, rest = word[0],word[1:]
       
        rest_strings = gen_all_strings(rest)
        
        results=list()
        for dum_string in rest_strings:
            
            for dum_pos in range(len(dum_string)+1):
                results.append(dum_string[:dum_pos]+\
                               first+dum_string[dum_pos:])
                
        return rest_strings+results
                               
   
#gen_all_strings("abcd")
# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    online_file = urllib2.urlopen(url)
    return [word[:-1] for word in online_file]

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    

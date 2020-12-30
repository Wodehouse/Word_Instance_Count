"""
word-frequency counts
Wodehouse
"""

import glob

def main():

    """ word frequencies for given file """
    #measures the frequency of the words
    txtfile = menu("/usr/local/doc") 
    lines = readFile(txtfile)

    words = clean(lines)
    # add word count to dictionary
    d = {}
    for i in range(len(words)):
        word = words[i]
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1   #first occurence of word

    # print the words with the highest counts
    highest = 0
    second = 0
    third = 0
    fourth = 0
    for key in d.keys():
        if d[key]>highest:
            highest = d[key]
            word = key
        elif d[key]<highest and d[key]>second:
            second = d[key]
            word2 = key
        elif d[key]<second and d[key]>third:
            third = d[key]
            word3 = key
        elif d[key]<third and d[key]>fourth:
            fourth = d[key]
            word4 = key

    print("%s has the highest word count with %d occurences" %(word, highest))
    print("%s has the second highest word count with %d occurences" %(word2, second))
    print("%s has the third highest word count with %d occurences" %(word3, third))
    print("%s has the fourth highest word count with %d occurences" %(word4, fourth))


def clean(lines):
      # now split each line into individual words
      # clean up each word (trailing punctuation)
    allwords = []
    for i in range(len(lines)):
        line = lines[i]
        words = line.split()
        #clean each word and add to allwords
        for j in range(len(words)):
            word = words[j].lower()
            cleaned = word.strip(".,'?:;!-'")
            allwords.append(cleaned)
    return allwords

def menu(dirname):
    """present menu of txt files, get choice"""
    # get all files that end in .txt
    files = glob.glob(dirname+"/*.txt")
    for i in range(len(files)):
        print("%d. %s" % (i+1,files[i]))
    index = getInt("Which file? ",1,len(files)) - 1
    return files[index]

def getInt(prompt,low,high):
    """get positive integer from user"""
    n = input(prompt)
    if n.isdigit():
        n = int(n)
        if n >= low and n <= high:
            return n
    print("Please enter a number from %d to %d..." % (low,high))
    return getInt(prompt,low,high)

def readFile(fname):
    """
    given file name, open file and read all lines into
    a list, then return the list
    """
    Lines = []
    infile = open(fname, "r")
    for line in infile:
        # skip the lines that start with a hash mark (comments)
        if line[0] != "#":
            # force everything to lowercase, take off trailing \n
            Lines.append(line.lower().strip())
    return Lines

main()

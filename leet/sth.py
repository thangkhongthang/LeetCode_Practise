# 781. Rabbits in Forest
# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
# Given the array answers, return the minimum number of rabbits that could be in the forest.

def numRabbits(answers):
    count = {}

    for item in answers:
        count[item] = count.get(item, 0) + 1
    min_rab = 0    
    for k in count:
        l = count[k]
        if l<= k+1:
            min_rab += k+1
        else:
            min_rab += (k+1)*((l+k)//(k+1))
    return min_rab

print(numRabbits([10,10,10]))
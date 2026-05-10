import random
#Odd number on dice
dice = [1,2,3,4,5,6]

favourable = 0
for i in dice:
    if i%2 !=0:
        favourable += 1
total_length = len(dice)
probability = favourable/total_length
print(probability)


#Number less than three
numbers = [1,2,3,4,5,6]
favourable = 0
for num in numbers:
    if num < 3:
        favourable += 1

total_len = len(numbers)
probability = favourable/total_len
print(probability)


#Coin toss
coin = ["H","T"]
favourable = 0
for type in coin:
    if type == "T":
        favourable += 1
total_len = len(coin)
probability = favourable/total_len
print(probability)


#Two coins tosses
two_coin = ["HH", "HT", "TH", "TT"]
favour = 0
for toss in two_coin:
    if toss.count("H") == 1:
        favour += 1
total_len = len(two_coin)
prob = favour/total_len
print(prob)


#Dice simulation
dice = [1,2,3,4,5,6]
def times(num):
    fav = 0
    for i in range(num):
        choices = random.choice(dice)
        if choices == 6:
            fav += 1
    probability = fav/num
    return probability

print(times(1000))


#Complement probability
dice = [1,2,3,4,5,6]

fav = 0
for i in dice:
    if i%2 == 0:
        fav += 1

total_len = len(dice)
prob = fav/total_len

com_prob = 1-prob
print(com_prob)


#Independent events
coin = ["H", "T"]
fav_coin = 0
for i in coin:
    if i == "H":
        fav_coin += 1

total_len_coin = len(coin)
probability_coin = fav_coin/total_len_coin

dice = [1,2,3,4,5,6]
fav_dice = 0
for i in dice:
    if i % 2 == 0:
        fav_dice += 1
total_len_dice = len(dice)
probability_dice = fav_dice/total_len_dice

ind_events = probability_coin * probability_dice
print(ind_events)
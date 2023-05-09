# number of players , power of enemy team
# we're given power of players we can select from 

# we can win if our team has striclty greater power than theirs

# sort players

# select best player, then select worst players until our score is greater
# add one to score, minimise size of our arr 

# enemy = 100

n, enemy_power = list(map(int, input().split()))
candidates = list(map(int, input().split()))

candidates.sort()
l = 0
r = n-1
count = 0
while l <= r:
    # select best player
    best_player_score = candidates[r]
    current_total = best_player_score
    r -= 1
    
    # while sum <= enemy_power, add worst player
    while current_total <= enemy_power and l <= r:
        current_total += best_player_score
        l += 1
     
    if current_total > enemy_power:
        count += 1 
print(count)
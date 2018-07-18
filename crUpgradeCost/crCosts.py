import math

# 1: common, 2: rare, 3: epic, 4: legendary
rarity_level = [1, 2, 3, 4]

# the array values correspond to the index from where the value in
# num_gold_required_upgrade_list best matches the cost of the 1st 
# upgrade (from level 1 to 2) of each rarity level.
# NOTE: one must add 1000 for the upgrade from level 1 to 2 for the legendary tier
gold_start_list = [0, 2, 4, 8]

# max level indices correspond to rarity levels from rarity_level
max_level_list = [13, 11, 8, 5]

#num_cards_required_upgrade_list = [2, 4, 10, 20, 50, 100, 200, 
#																		400, 800, 1000, 2000, 5000]
#num_gold_required_upgrade_list = [5, 20, 50, 150, 400, 1000, 2000, 4000,
#																	8000, 20000, 50000, 100000]

# Calculates total cost to upgrade all cards to the highest level possible
# with the quantity at hand.
def calculateUpgradeCosts(rarity_list, quantity_list, level_list):
	num_items = min(len(rarity_list), len(quantity_list), len(level_list))
	cost = 0
	
	num_cards_required_upgrade_list = [2, 4, 10, 20, 50, 100, 200, 
																			400, 800, 1000, 2000, 5000]
	num_gold_required_upgrade_list = [5, 20, 50, 150, 400, 1000, 2000, 4000,
																		8000, 20000, 50000, 100000]
	
	for i in range(num_items):
		rarity = rarity_list[i]
		quantity = quantity_list[i]
		level = level_list[i]
		
		while (quantity >= num_cards_required_upgrade_list[level - 1] and level < max_level_list[rarity - 1]):
			if (level == 1 and rarity == 4):
				cost += 5000
			else:
				gold_start_index = gold_start_list[rarity - 1]
				cost += num_gold_required_upgrade_list[gold_start_index + level - 1]
			quantity -= num_cards_required_upgrade_list[level - 1]
			level += 1
			
	return cost

def testCalculateUpgradeCosts():
	# answer should be 346,150
	rarity_list = [2, 4, 4, 4, 2, 3, 1]
	quantity_list = [1043, 3, 6, 36, 745, 72, 6742]
	level_list = [1, 1, 1, 1, 5, 3, 4]
	
	print (calculateUpgradeCosts(rarity_list, quantity_list, level_list))
	
def customCalculate():
	rarity_list = [3, 2, 2, 3, 3, 3, 1, 1, 1, 3, 3, 2, 3]
	quantity_list = [73, 905, 858, 67, 115, 89, 4075, 3803, 5532, 70, 74, 874, 111]
	level_list = [5, 7, 7, 5, 1, 1, 11, 11, 9, 4, 1, 9, 4]
	
	return calculateUpgradeCosts(rarity_list, quantity_list, level_list)


# Open "playerCards.txt" to retrieve card info
card_file = open("playerCards.txt", "r")

name_list = []
rarity_list = []
card_quantity_list = []
current_level_list = []

for line in card_file:
	name, rarity, card_ratio, level = line.split(',')
	name_list.append(name)
	rarity_list.append(int(rarity) // 100)
	card_quantity, cost_next_upgrade = card_ratio.split('/')
	card_quantity_list.append(int(card_quantity.strip()))
	level = int(level.strip('\n'))
	current_level_list.append(level)

print (calculateUpgradeCosts(rarity_list, card_quantity_list, current_level_list))
#testCalculateUpgradeCosts()
#print (customCalculate())

card_file.close()		
		
		
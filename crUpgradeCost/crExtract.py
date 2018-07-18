from lxml import html
import requests
import re
import sys
import argparse

# parse user input (should be a valid player id from the mobile game "Clash Royale")
text_description = 'Obtain Clash Royale card information for a given player ID. Results stored in files.'
parser = argparse.ArgumentParser(description=text_description)
parser.add_argument("id", help='Player ID')
args = parser.parse_args()
player_id = args.id

# get html content page for a given user
id = player_id;
page = requests.get('https://statsroyale.com/profile/' + id + '/cards')
tree = html.fromstring(page.content)

user_exists = tree.xpath('//div[@class="ui__headerMedium"]/text()')

if (len(user_exists) > 0):
	print ("No valid user with such ID.")
	sys.exit()

print ("Valid user found! Retrieving card name list...")

# obtain the name of every card a player currently has and store in list
card_name_list = tree.xpath('//div[@class="ui__tooltip ui__tooltipTop ui__tooltipMiddle cards__tooltip"]/text()')
card_name_list = list(map(str.strip, card_name_list))

print ("Retrieving card quantity list...")

# obtain the number of each such card a player currently has and quantity needed for next upgrade
card_quantity_list = tree.xpath('//div[@class="profileCards__meter__numbers"]/text()')
card_quantity_list = list(map(str.strip, card_quantity_list))

print ("Retrieving card level list...")

# obtain the current level of each card a player currently has and store in list
card_level_list = tree.xpath('//span[@class="profileCards__level"]/text()')
pattern = '[^0-9]'
card_level_list = [ re.sub(pattern, '', item) for item in card_level_list]

#card_elixir_cost_list = tree.xpath('//@data-elixir')
card_rarity_list = tree.xpath('//@data-rarity')

print ("Writing data to file...")

# begin writing card info to a file 
card_file = open("playerCards.txt", "w")
num_cards_list = len(card_name_list)
num_quantity_list = len(card_quantity_list)
num_level_list = len(card_level_list)

num_items = min(num_cards_list, num_quantity_list, num_level_list)

for i in range(num_items):
	if (card_name_list[i] != "" and card_rarity_list[i] != "" and card_quantity_list[i] != "" and card_level_list[i] != ""):
		card_file.write("{0}, {1}, {2}, {3}\n".format(card_name_list[i], card_rarity_list[i], card_quantity_list[i], card_level_list[i]))


card_file.close()

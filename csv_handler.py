import csv

player_dict = {}

with open('Player_Attributes.csv', mode='r') as fp:
	line_count = 0
	csv_reader = csv.DictReader(fp)
	for row in csv_reader:
		if(line_count) == 0:
			line_count += 1
		player_api = row["player_api_id"]
		if(player_api in player_dict):
			if(row["date"] > player_dict[player_api][0]):
				player_dict[player_api] = row["date"], row["overall_rating"]
		else:
			player_dict[player_api] = row["date"], row["overall_rating"]



with open('Organized_Players.csv', mode='w') as fp:
	for tracker in range(len(player_dict.keys())):
		key = list(player_dict.keys())[tracker]
		temp_dict = {"player_api_id": key, "date": player_dict[key][0], "overall_rating": player_dict[key][1]}
		
		if(tracker == 0):
			w = csv.DictWriter(fp, temp_dict.keys())
			w.writeheader()
		w = csv.DictWriter(fp, temp_dict.keys())
		w.writerow(temp_dict)

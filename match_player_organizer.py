import csv

matches = []

with open('Match.csv', mode='r') as fp:
    line_count = 0
    csv_reader = csv.DictReader(fp)
    for row in csv_reader:
        if(line_count) == 0:
            line_count += 1
        season = row["season"]
        if(season == "2015/2016"):
            matches.append(row)


with open("2015,2016_Matches.csv", mode='w') as fp:
    tracker = 0
    for match in matches:
        w = csv.DictWriter(fp, match.keys())
        if(tracker == 0):
            w.writeheader()
            tracker += 1
        w.writerow(match)

for match in matches:
    keys = match.keys()

    for num in range(1, 12):
        match.pop("home_player_X{}".format(num), None)
        match.pop("away_player_X{}".format(num), None)
        match.pop("home_player_Y{}".format(num), None)
        match.pop("away_player_Y{}".format(num), None)
    match.pop("date", None)
    match.pop("league_id", None)
    match.pop("season", None)

with open("Matches_With_Players.csv", mode='w') as fp:
    tracker = 0
    for match in matches:
        w = csv.DictWriter(fp, match.keys())
        if(tracker == 0):
            w.writeheader()
            tracker += 1
        w.writerow(match)

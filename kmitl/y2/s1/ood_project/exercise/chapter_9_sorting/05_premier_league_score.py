def parse_input(input_str):
    teams = input_str.split('/')
    data = []
    for team in teams:
        name, wins, loss, draws, scored, conceded = team.split(',')
        wins, loss, draws, scored, conceded = int(wins), int(loss), int(draws), int(scored), int(conceded)
        points = wins * 3 + draws
        goal_difference = scored - conceded
        data.append((name, points, goal_difference))
    return data

def custom_sort(data):
    range_i = range(len(data))

    # for i in range(len(data)):
    for i in range_i:
        range_j = range(0, len(data) - i - 1)

        # for j in range(0, len(data) - i - 1):
        for j in range_j:

            j_team_gd = data[j][2]
            j_team_points = data[j][1]

            k = j + 1
            k_team_gd = data[k][2]
            k_team_point = data[k][1]
            
            if (j_team_points < k_team_point) or (j_team_points == k_team_point and j_team_gd < k_team_gd):
                data[j], data[j + 1] = data[j + 1], data[j]

def generate_results(data):
    results = []
    for name, points, goal_difference in data:
        results.append([name, {'points': points}, {'gd': goal_difference}])
    return results

def process_football_data(input_str):
    data = parse_input(input_str)
    custom_sort(data)
    return generate_results(data)

input_str = input('Enter Input : ')
output = process_football_data(input_str)
print("== results ==")
for line in output:
    print(line)

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

team_size = len(list_players) // 2
#print(f"{team_size=}")

print(list_players[:team_size])
print(list_players[team_size:])

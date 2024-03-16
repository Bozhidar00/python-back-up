cards = input("ЗАПИШИ СЕРИЯ ОТ КАРТИ: ").split()

team_a_players = set(range(1, 12))
team_b_players = set(range(1, 12))

for card in cards:
    team, player = card.split('-')
    player = int(player)

    if team == 'A' and player in team_a_players:
        team_a_players.remove(player)
    elif team == 'B' and player in team_b_players:
        team_b_players.remove(player)

    if len(team_a_players) < 7 or len(team_b_players) < 7:
        print("ИГРАТА БЕШЕ ПРЕКРАТЕНА")
        break

if len(team_a_players) >= 7 and len(team_b_players) >= 7:
    print(f"ОТБОР A - {len(team_a_players)}; ОТБОР B - {len(team_b_players)}")


if __name__ == "__main__":
    players = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]
    players_dict = {player: i for i, player in enumerate(players)}

    for call in callings:
        idx = players_dict[call]

        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        players_dict[players[idx]] = idx
        players_dict[players[idx - 1]] = idx - 1

    a = 1
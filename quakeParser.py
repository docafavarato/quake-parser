import json
import os

if not os.path.exists(os.getcwd()+'\output'):
    os.mkdir(os.getcwd()+'\output')

def quakeParser(filename):
    with open(filename, "r") as r:
        data = r.read()
        games = []
        index = 0
        for game in data.split("ShutdownGame"):
            total_kills = 0
            players_info = {}
            for line in game.split("\n"):
                if "Kill" and "killed" in line:
                    total_kills += 1
                    if "<world>" not in line:
                        player_name = line.split("killed")[0].split(":")[3].strip()
                        killed_player = line.split("killed")[1].split("by")[0].strip()
                        if player_name != killed_player:
                            players_info[player_name] = players_info[player_name] + 1
                        elif player_name == killed_player:
                            players_info[player_name] = players_info[player_name] - 1
                    elif "<world>" in line:
                        player_name = line.split("killed")[1].split("by")[0].strip()
                        players_info[player_name] = players_info[player_name] - 1
                        
                elif "ClientUserinfoChanged" in line: 
                    player_name = line.split('n\\')[1].split("\\")[0]
                    if not players_info.get(player_name):
                        players_info[player_name] = 0  
                        
            newObj = []
            for player in players_info:
                newObj.append({"name": player, "kills": players_info[player]})
            
            games.append({
                "game": index+1,
                "status": {
                    "total_kills": total_kills,
                    "players": newObj
                }
            })
            index += 1    

    with open("output/data.json", "w", encoding="utf-8") as output:
        games.pop()
        json.dump(games, output, indent=4, ensure_ascii=False)
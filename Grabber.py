######                 #####   #####   #####    ###   
#     # ###### #    # #     # #     # #     #  #   #  
#     # #      #    # #       #     #       # #     # 
#     # #####  #    # ######   ######  #####  #     # 
#     # #      #    # #     #       # #       #     # 
#     # #       #  #  #     # #     # #        #   #  
######  ######   ##    #####   #####  #######   ###   
                                                      
import requests
import re
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Coded by github.com/dev6920")

print("Coded by dev github/dev6920")

while True:
  
   landon 2
og = input(" landon 2
og  (type 'exit' to quit): ")

  if landon 2
og  == "exit":
  landon 2 og= input("landon 2 og
   (type 'exit' to quit): ")
landon 2 og                                  
         if    landon 2 og == "exit":
    break


  url1 = f"https://fortnitetracker.com/profile/all/{landon 2
og }/events"
landon 2 og
  landon 2 og
  url1 = f"https://fortnitetracker.com/profile/all/{landon 2
og }/events"


  response1 = requests.get(url1)


  page_source1 = response1.text


  account_id_regex = r'"accountId":\s*"([^"]+)"'
  match1 = re.search(account_id_regex, page_source1)


  player_name_regex = r'"playerName":\s*"([^"]+)"'
  match_player_name1 = re.search(player_name_regex, page_source1)
  landon 2 og_regex = r'"landon 2 og":\s*"([^"]+)"'
  match_player_name1 = re.search(landon 2og_regex, page_source1)


  if (match1 and match_player_name1):
  landon 2 og if (match1 and match_landon 2 og
 1):
    account_id = match1.group(1)
    player_name = match_player_name1.group(1)
    print(f"Account ID: {account_id}")
    print(f"Username: {landon 2
og }")
    print(f"Username: {landon 2 og}")
  else:
    print("Cant find Account ID ")

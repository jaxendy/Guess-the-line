import pandas as pd
df = pd.DataFrame()
# Initialize variables to None firstx
week_dfs = {}  # Dictionary to store week dataframes
weekDf = []    # List of loaded week keys

for week in range(15):
    try:
        file_path = f'/filepath/weeks/week{week}gtl.csv'
        df = pd.read_csv(file_path)
        week_key = f'week{week}'
        week_dfs[week_key] = df
        weekDf.append(week_key)
    except (ValueError, FileNotFoundError):
        continue

# Function to get a player's guess with input validation
def playerGuess(player, homeTeam, awayTeam):
    back = False
    print(f'Type "i" for information about past games\n')
    while True:
      guess = input(f"Enter {player}\'s guess (Home team perspective): ").strip()
      if not guess:
          print("Please enter a guess.")
          continue
      if guess.lower() == 'back':
        return None
        break
      if guess.lower() == 'i':
         displayInfo(homeTeam.lower(), awayTeam.lower())
         print(f'\n')
      elif guess in ['pick', 'Pick', 'pk', '0', '0.0']:
         guessUpdate = 0.0
         break
      elif guess[0] in ['-', '+']:
        try:
          number = float(guess[1:])
          guessUpdate = -number if guess[0] == '-' else +number
          break 
        except ValueError:
             print("Invalid number after the sign.")
      else:
        print("Guess must start with '+' or '-'.")
      if back == True:
        continue
    return guessUpdate

# Function to compare two players' distances
def comparePlayers(p1, p2):
  if distance[p1] < distance[p2]:
    return 1
  elif distance[p1] > distance[p2]:
    return -1
  else:
    return 0

# Function to display past games for two teams
def displayInfo(team1, team2):
    def helper(team):
        print(f'\nPast games for {team.title()}')
        for key in weekDf:
            df = week_dfs[key]

            # All games where team is home or away
            home_games = df[df['Home Team'] == team]
            away_games = df[df['Away Team'] == team]

            # Home games: keep line as-is
            for _, row in home_games.iterrows():
                line = row['Actual Line']
                try:
                    line_val = float(line)
                    formatted = f"+{line_val}" if line_val > 0 else str(line_val)
                except ValueError:  # e.g., "pick"
                    formatted = str(line)
                print(f"Week {row['Week']}: {formatted} vs. {row['Away Team'].title()}")

            # Away games: flip line sign
            for _, row in away_games.iterrows():
                line = row['Actual Line']
                try:
                    line_val = float(line)
                    flipped = -line_val
                    formatted = f"+{flipped}" if flipped > 0 else str(flipped)
                except ValueError:  # e.g., "pick"
                    formatted = str(line)
                print(f"Week {row['Week']}: {formatted} @ {row['Home Team'].title()}")

    helper(team1)
    helper(team2)
        
# Create the teams DataFrame with all teams
teams = pd.DataFrame(
    data=[
        ['Air Force', 'Mountain West'],
        ['Akron', 'MAC'],
        ['Alabama', 'SEC'],
        ['Appalachian State', 'Sun Belt'], # app state
        ['Arizona', 'Big 12'],
        ['Arizona State', 'Big 12'],
        ['Arkansas', 'SEC'],
        ['Arkansas State', 'Sun Belt'],
        ['Army', 'American'],
        ['Auburn', 'SEC'],
        ['Ball State', 'MAC'],
        ['Baylor', 'Big 12'],
        ['Boise State', 'Mountain West'], # boise
        ['Boston College', 'ACC'], # bc
        ['Bowling Green', 'MAC'], # bg
        ['Buffalo', 'MAC'],
        ['BYU', 'Big 12'],
        ['California', 'ACC'], # cal
        ['Central Michigan', 'MAC'], # central, cmu
        ['Charlotte', 'American'], 
        ['Cincinnati', 'Big 12'], # cinci, cincy
        ['Clemson', 'ACC'],
        ['Coastal Carolina', 'Sun Belt'], # coastal
        ['Colorado', 'Big 12'], #cu
        ['Colorado State', 'Mountain West'], # csu
        ['Duke', 'ACC'],
        ['East Carolina', 'American'], # ecu
        ['Eastern Michigan', 'MAC'], # eastern, emu
        ['FIU', 'Conference USA'],
        ['Florida', 'SEC'],
        ['Florida Atlantic', 'American'], # fau
        ['Florida State', 'ACC'], # fsu
        ['Fresno State', 'Mountain West'], # fresno
        ['Georgia', 'SEC'], # uga
        ['Georgia Southern', 'Sun Belt'],
        ['Georgia State', 'Sun Belt'],
        ['Georgia Tech', 'ACC'], # gt
        ['Hawaii', 'Mountain West'],
        ['Houston', 'Big 12'],
        ['Illinois', 'Big Ten'],
        ['Indiana', 'Big Ten'],
        ['Iowa', 'Big Ten'],
        ['Iowa State', 'Big 12'],
        ['Jacksonville State', 'Conference USA'], # jax, jax state
        ['James Madison', 'Sun Belt'], # jmu
        ['Kansas', 'Big 12'], # ku
        ['Kansas State', 'Big 12'], #kstate, k-state
        ['Kennesaw State', 'Conference USA'], # kennesaw
        ['Kent State', 'MAC'], # kent
        ['Kentucky', 'SEC'], # uk
        ['Liberty', 'Conference USA'],
        ['Louisiana', 'Sun Belt'], # ull
        ['Louisiana-Monroe', 'Sun Belt'], # ukm
        ['Louisiana Tech', 'Conference USA'], # la tech
        ['Louisville', 'ACC'],
        ['LSU', 'SEC'],
        ['Marshall', 'Sun Belt'],
        ['Maryland', 'Big Ten'],
        ['Memphis', 'American'],
        ['Miami (FL)', 'ACC'], # miami fl
        ['Miami (OH)', 'MAC'], # miami oh, miami
        ['Michigan', 'Big Ten'], # um
        ['Michigan State', 'Big Ten'], # msu
        ['Middle Tennessee', 'Conference USA'], # mtsu
        ['Minnesota', 'Big Ten'], # minn
        ['Mississippi State', 'SEC'], # miss state, miss st
        ['Missouri', 'SEC'], # mizzou
        ['Navy', 'American'],
        ['NC State', 'ACC'],
        ['Nebraska', 'Big Ten'],
        ['Nevada', 'Mountain West'],
        ['New Mexico', 'Mountain West'], # unm
        ['New Mexico State', 'Conference USA'], # nmst
        ['North Carolina', 'ACC'], # unc
        ['North Texas', 'American'], # unt
        ['Northern Illinois', 'MAC'], # niu
        ['Northwestern', 'Big Ten'], 
        ['Notre Dame', 'Independent'],
        ['Ohio', 'MAC'],
        ['Ohio State', 'Big Ten'],
        ['Oklahoma', 'SEC'], # ou
        ['Oklahoma State', 'Big 12'], #okie
        ['Old Dominion', 'Sun Belt'], # odu
        ['Ole Miss', 'SEC'], # mississippi
        ['Oregon', 'Big Ten'], 
        ['Oregon State', 'Pac-2'],
        ['Penn State', 'Big Ten'], # psu
        ['Pittsburgh', 'ACC'], # pitt
        ['Purdue', 'Big Ten'],
        ['Rice', 'American'],
        ['Rutgers', 'Big Ten'],
        ['Sam Houston', 'Conference USA'], # shst, sam houston st, sam houston state
        ['San Diego State', 'Mountain West'], # sdsu
        ['San Jose State', 'Mountain West'], # sjst, sjsu, san jose
        ['SMU', 'ACC'], 
        ['South Alabama', 'Sun Belt'], #usa
        ['South Carolina', 'SEC'], # sc
        ['South Florida', 'American'], # usf
        ['Southern Miss', 'Sun Belt'], # usm
        ['Stanford', 'ACC'],
        ['Syracuse', 'ACC'],
        ['TCU', 'Big 12'],
        ['Temple', 'American'],
        ['Tennessee', 'SEC'], # tenn
        ['Texas', 'SEC'], # ut
        ['Texas A&M', 'SEC'], # a&m
        ['Texas State', 'Sun Belt'], 
        ['Texas Tech', 'Big 12'], # ttu, tech
        ['Toledo', 'MAC'],
        ['Troy', 'Sun Belt'],
        ['Tulane', 'American'],
        ['Tulsa', 'American'],
        ['UAB', 'American'],
        ['UCF', 'Big 12'],
        ['UCLA', 'Big Ten'],
        ['UConn', 'Independent'],
        ['UMass', 'Independent'],
        ['UNLV', 'Mountain West'],
        ['USC', 'Big Ten'],
        ['UTEP', 'Conference USA'],
        ['UTSA', 'American'],
        ['Utah', 'Big 12'],
        ['Utah State', 'Mountain West'], # usu
        ['Vanderbilt', 'SEC'], # vandy
        ['Virginia', 'ACC'], # uva
        ['Virginia Tech', 'ACC'], # vt
        ['Wake Forest', 'ACC'], # wake
        ['Washington', 'Big Ten'], # uw
        ['Washington State', 'Pac-2'], # wazzu, wsu
        ['West Virginia', 'Big 12'], # wvu
        ['Western Kentucky', 'Conference USA'], # wku
        ['Western Michigan', 'MAC'], # western, wmu
        ['Wisconsin', 'Big Ten'], # sconnie
        ['Wyoming', 'Mountain West'],
        ['Delaware', 'Conference USA'],
        ['Missouri State', 'Conference USA']
    ],
    columns=['Team', 'Conference']
)

# Convert the 'Team' column to lowercase
teams['Team'] = teams['Team'].str.lower()

alt_names = {
    # 'alternate name': 'official team name'
    'app state': 'appalachian state',
    'boise': 'boise state',
    'bc': 'boston college',
    'bg': 'bowling green',
    'cal': 'california',
    'central': 'central michigan',
    'cmu': 'central michigan',
    'cinci': 'cincinnati',
    'cincy': 'cincinnati',
    'coastal': 'coastal carolina',
    'cu': 'colorado',
    'csu': 'colorado state',
    'ecu': 'east carolina',
    'eastern': 'eastern michigan',
    'emu': 'eastern michigan',
    'fau': 'florida atlantic',
    'fsu': 'florida state',
    'fresno': 'fresno state',
    'uga': 'georgia',
    'gt': 'georgia tech',
    'jax': 'jacksonville state',
    'jax state': 'jacksonville state',
    'jmu': 'james madison',
    'ku': 'kansas',
    'kstate': 'kansas state',
    'k-state': 'kansas state',
    'kennesaw': 'kennesaw state',
    'kent': 'kent state',
    'uk': 'kentucky',
    'ull': 'louisiana',
    'ulm': 'louisiana-monroe',
    'la tech': 'louisiana tech',
    'miami fl': 'miami (fl)',
    'miami oh': 'miami (oh)',
    'miami': 'miami (oh)',  # could go either way
    'um': 'michigan',
    'msu': 'michigan state',
    'mtsu': 'middle tennessee',
    'minn': 'minnesota',
    'miss state': 'mississippi state',
    'miss st': 'mississippi state',
    'mizzou': 'missouri',
    'unm': 'new mexico',
    'nmst': 'new mexico state',
    'unc': 'north carolina',
    'unt': 'north texas',
    'niu': 'northern illinois',
    'ou': 'oklahoma',
    'okie': 'oklahoma state',
    'odu': 'old dominion',
    'mississippi': 'ole miss',
    'psu': 'penn state',
    'pitt': 'pittsburgh',
    'shst': 'sam houston',
    'sam houston st': 'sam houston',
    'sam houston state': 'sam houston',
    'sdsu': 'san diego state',
    'sjst': 'san jose state',
    'sjsu': 'san jose state',
    'san jose': 'san jose state',
    'usa': 'south alabama',
    'sc': 'south carolina',
    'usf': 'south florida',
    'usm': 'southern miss',
    'tenn': 'tennessee',
    'ut': 'texas',
    'a&m': 'texas a&m',
    'ttu': 'texas tech',
    'tech': 'texas tech',
    'usu': 'utah state',
    'vandy': 'vanderbilt',
    'uva': 'virginia',
    'vt': 'virginia tech',
    'wake': 'wake forest',
    'uw': 'washington',
    'wazzu': 'washington state',
    'wsu': 'washington state',
    'wvu': 'west virginia',
    'wku': 'western kentucky',
    'western': 'western michigan',
    'wmu': 'western michigan',
    'sconnie': 'wisconsin',
    'mo state': 'missouri state',
    'missouri st': 'missouri state'
}
# Load your teams DataFrame and make names lowercase
teams['Team'] = teams['Team'].str.lower()

# Create set of valid team names
valid_teams = set(teams['Team'])

# Add canonical teams to aliases map (identity map)
for team in valid_teams:
    alt_names[team] = team

teamsDict = dict(zip(teams['Team'], teams['Conference']))

# Normalizer function
def normalize_team(name):
    return alt_names.get(name.strip().lower(), None)

done = False
iteration = 0
score = 0
print(f'Enter "back" at anytime to restart game\n')
week = input(f'What week is it: ')
playerCount = int(input(f'How many players (6 max): '))
while playerCount not in [2,3,4,5,6]:
    playerCount = int(input(f'How many players (6 max): '))
playerList = []
for i in range(playerCount):
  player = input(f"Enter Player {i+1}'s name: ").strip()
  playerList.append(player)

# User selects scoring style
scoreType = input("\n\nChoose a scoring style —\n\npoints (closest guess earns a point)\nrelative (each player has a score against each other)\nboth points and relative\n\n(p/r/b): ").strip().lower()
if scoreType not in ['p', 'r', 'b']:
  scoreType = input("Choose a scoring style —\npoints (closest guess earns a point)\nrelative (each player has a score against each other)\nboth points and relative\n\n(p/r/b): ").strip().lower()
count = {player: 0 for player in playerList}


# Create a list to track possible matchups
matchups = [f'{player1} vs {player2}' for i, player1 in enumerate(playerList) for player2 in playerList[i+1:]]
# Keep dictionary of matchups to keep track of score
relativeTrack = {m: 0 for m in matchups}

# Create the dataframe based on scoreType
if scoreType == 'p':
  columns = (
    ['Week', 'Home Team', 'Away Team', 'Conference Game'] +
    [f'{player} Guess' for player in playerList] +
    ['Actual Line'] +
    [f'{player} Distance' for player in playerList] +
    [f'{player} Score' for player in playerList]
)
if scoreType == 'r':
  columns = (
    ['Week', 'Home Team', 'Away Team', 'Conference Game'] +
    [f'{player} Guess' for player in playerList] +
    ['Actual Line'] +
    [f'{player} Distance' for player in playerList] +
    matchups
)
   
if scoreType == 'b':
  columns = (
    ['Week', 'Home Team', 'Away Team', 'Conference Game'] +
    [f'{player} Guess' for player in playerList] +
    ['Actual Line'] +
    [f'{player} Distance' for player in playerList] +
    [f'{player} Score' for player in playerList] +
    matchups
)
weeklyDf = pd.DataFrame(columns=columns)


print("\n\n THE GAME BEGINS!\n")
# Main loop
while not done:
    print('\n')
    # Input home and away teams
    homeTeam = input("Enter Home Team: ").lower().strip()
    if homeTeam.lower() == 'back':
      continue
    homeTeam = normalize_team(homeTeam)
    while homeTeam is None:
        print(f'Not in list, try again:\n')
        homeTeam = normalize_team(input("Enter Home Team: "))

    awayTeam = input("Enter Away Team: ").lower().strip()
    if awayTeam.lower() == 'back':
        continue
    awayTeam = normalize_team(awayTeam)
    while awayTeam is None:
        print(f'Not in list, try again:\n')
        awayTeam = normalize_team(input("Enter Away Team: "))

    # See if confrence game
    if teamsDict[homeTeam] == teamsDict[awayTeam]:
       conferenceGame = teamsDict[homeTeam]
    else:
       conferenceGame = None

    guesses = {}
    actualBack = False
    for player in playerList:
      guess = playerGuess(player, homeTeam, awayTeam)
      if guess is None:
        actualBack = True
        break
      guesses[player] = guess


    # ACTUAL LINE
    while True:
      actualLine = input("\nEnter the Actual Line (Home team perspective): ").strip()
      if not actualLine:
        print("Please enter a guess.")
        continue
      if actualLine.lower() == 'back':
        actualBack = True
        break
      if actualLine in ['pick', 'Pick', 'pk', '0', '0.0']:
         actualLineUpdate = 0.0
         break
      if actualLine[0] in ['-', '+']:
        try:
          number = float(actualLine[1:])  # this might raise ValueError
          actualLineUpdate = -number if actualLine[0] == '-' else number
          break
        except ValueError:
             print("Invalid number after the sign.")
      else:
        print("Guess must start with '+' or '-'.")
    if actualBack == True:
        continue
    # CALCULATE DISTANCE
    distance = {}
    for player in playerList:
      distance[player] = abs(guesses[player] - actualLineUpdate)
    
    # Keep going
    keepGoing = input(f'Add another game? (y/n): ')
    if keepGoing == 'back':
        continue
    while keepGoing not in ['y', 'n']:
      keepGoing = input(f'Add another game? (y/n): ')
    # Score update for point and both systems
    if scoreType in ['p', 'b']:
      lowest = min(distance.values())
      winners = [player for player, dist in distance.items() if dist == lowest]
      # get number of winners to split point if necessary
      numWinners = len(winners)
      # If one winner full point
      if numWinners == 1:
        count[winners[0]] += 1
      # if two or more winners split point
      if numWinners > 1:
        for player in winners:
          count[player] += 1 / numWinners
        
    
    if scoreType in ['r', 'b']:
    # Score update for relative and both systems
      for i in range (len(playerList)):
         for j in range (i + 1, len(playerList)):
            p1 = playerList[i]
            p2 = playerList[j]
            result = comparePlayers(p1, p2)
            # RESULT ALWAYS IN TERMS OF HIGHERER INDEX PLAYER
            if result == 1:
              relativeTrack[f'{p1} vs {p2}'] += 1
            elif result == -1:
              relativeTrack[f'{p1} vs {p2}'] -= 1
            else:
              continue

    # Print results
    # Add to dataframe based on scoreType
       
    # If scoretype is points
    if scoreType == 'p':
      weeklyDf.at[iteration, 'Week'] = week
      weeklyDf.at[iteration, 'Home Team'] = homeTeam
      weeklyDf.at[iteration, 'Away Team'] = awayTeam
      weeklyDf.at[iteration, 'Conference Game'] = conferenceGame
      weeklyDf.at[iteration, 'Actual Line'] = actualLineUpdate
      for player in playerList:
        weeklyDf.at[iteration, f'{player} Guess'] = guesses[player]
        weeklyDf.at[iteration, f'{player} Distance'] = distance[player]
        weeklyDf.at[iteration, f'{player} Score'] = count[player]
      print("Distance:")
      for player in playerList:
        print(f'{player} was off by {distance[player]}')
      print('\n')
      print("Score:")
      for player in playerList:
        print(f'{player} has {count[player]} points')

    # If scoretype is relative
    if scoreType == 'r':
      weeklyDf.at[iteration, 'Week'] = week
      weeklyDf.at[iteration, 'Home Team'] = homeTeam
      weeklyDf.at[iteration, 'Away Team'] = awayTeam
      weeklyDf.at[iteration, 'Conference Game'] = conferenceGame
      weeklyDf.at[iteration, 'Actual Line'] = actualLineUpdate

      for player in playerList:
        weeklyDf.at[iteration, f'{player} Guess'] = guesses[player]
        weeklyDf.at[iteration, f'{player} Distance'] = distance[player]
      for matchup in matchups:
        weeklyDf.at[iteration, matchup] = relativeTrack[matchup]
      print("Distance:")
      for player in playerList:
        print(f'{player} was off by {distance[player]}')
      print('\n')
      print("Relative Score (First team is +):")
      for matchup in matchups:
        print(f'{matchup}: {relativeTrack[matchup]}')
         

    # If scoretype is both
    if scoreType == 'b':
      weeklyDf.at[iteration, 'Week'] = week
      weeklyDf.at[iteration, 'Home Team'] = homeTeam
      weeklyDf.at[iteration, 'Away Team'] = awayTeam
      weeklyDf.at[iteration, 'Conference Game'] = conferenceGame
      weeklyDf.at[iteration, 'Actual Line'] = actualLineUpdate

      for player in playerList:
        weeklyDf.at[iteration, f'{player} Guess'] = guesses[player]
        weeklyDf.at[iteration, f'{player} Distance'] = distance[player]
        weeklyDf.at[iteration, f'{player} Score'] = count[player]
      for matchup in matchups:
        weeklyDf.at[iteration, matchup] = relativeTrack[matchup]
      print("Distance:")
      for player in playerList:
        print(f'{player} was off by {distance[player]}')
      print('\n')
      print("Relative Score (First team is +):")
      for matchup in matchups:
        print(f'{matchup}: {relativeTrack[matchup]}')
      print('\n')
      print("Score:")
      for player in playerList:
        print(f'{player} has {count[player]} points')
    
    # Add one to the index
    iteration += 1

    if keepGoing == 'y':
      weeklyDf.to_csv(f'/filepath/weeks/week{week}gtl.csv', index = False, mode = 'w')
      continue
    if keepGoing == 'n':
      weeklyDf.to_csv(f'/filepath/week{week}gtl.csv', index = False, mode = 'w')
      done = True
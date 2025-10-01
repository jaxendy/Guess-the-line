import pandas as pd
df = pd.DataFrame()
# Initialize variables to None firstx
week_dfs = {}  # Dictionary to store week dataframes
weekDf = []    # List of loaded week keys

for week in range(15):
    try:
        file_path = f'/Users/jaxen1/Shared/C/Guess the Line/weeks/week{week}gtl.csv'
        df = pd.read_csv(file_path)
        week_key = f'week{week}'
        week_dfs[week_key] = df
        weekDf.append(week_key)
    except (ValueError, FileNotFoundError):
        continue
# def displayInfo(team1, team2):
#     def helper(team):
#       print(f'\nPast games for {team.title()}')
#       for key in weekDf:
#           try:
#               df = week_dfs[key]
#               homeTeam = (df['Home Team'] == team)
#               awayTeam = (df['Away Team'] == team)
        
#               if homeTeam.any():
#                     for _, row in df[homeTeam].iterrows():
#                         # Format the line for home team - use the line as is
#                         line = str(row['Actual Line'])
#                         if line != 'pick':
#                            floatLine = float(row['Actual Line'])
#                         else:
#                            floatLine = 'pick'
#                         formatted_line = '+' + floatLine if floatLine > 0 else floatLine
#                         print(f"Week {row['Week']}: {formatted_line} vs. {row['Away Team'].title()}")
                
#               if awayTeam.any():
#                 for _, row in df[awayTeam].iterrows():
#                         # For away team, flip the sign of the line
#                         try:
#                             # Convert to float to perform math operation
#                             num_line = float(row['Actual Line'])
#                             # Flip the sign
#                             flipped_line = -1 * num_line
#                             # Format with appropriate sign
#                             if flipped_line > 0:
#                                 formatted_line = f"+{flipped_line}"
#                             else:
#                                 formatted_line = str(flipped_line)
#                             print(f"Week {row['Week']}: {float(formatted_line)} @ {row['Home Team'].title()}")
#                         except ValueError:
#                             # If conversion to float fails, just use the line as is
#                             print(f"Week {row['Week']}: {row['Actual Line']} @ {row['Home Team'].title()}")
#           except (TypeError, KeyError):
#               continue
#     helper(team1)
#     helper(team2)

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

weeklyDf = pd.DataFrame(columns = ['Week', 'Home Team', 'Away Team', 'Conference Game', 'Jackson Guess', 'Jameson Guess', 'Actual Line', 'Jackson Distance', 'Jameson Distance', 'Score'])
done = False
iteration = 0
score = 0
print(f'Enter "back" at anytime to restart game\n')
week = input(f'What week is it: ')
while not done:
    print('\n')
    jacksonBack = False
    jamesonBack = False
    actualBack = False
    
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

    
    # Add guesses
        
        ## JACKSON
    print(f'Type "i" for information about past games\n')
    while True:
      jacksonGuess = input("Enter Jackson\'s guess (Home team perspective): ").strip()
      if jacksonGuess.lower() == 'back':
        jacksonBack = True
        break
      if jacksonGuess.lower() == 'i':
         displayInfo(homeTeam.lower(), awayTeam.lower())
         print(f'\n')
      elif jacksonGuess in ['pick', 'Pick', 'pk', '0', '0.0']:
         jacksonGuessUpdate = 0.0
         break
      elif jacksonGuess[0] in ['-', '+']:
        try:
          number = float(jacksonGuess[1:])
          jacksonGuessUpdate = number if jacksonGuess[0] == '-' else -number
          break 
        except ValueError:
             print("Invalid number after the sign.")
      else:
        print("Guess must start with '+' or '-'.")
    if jacksonBack == True:
        continue
    # JAMESON
    while True:
      jamesonGuess = input("Enter Jameson\'s guess (Home team perspective): ").strip()
      if jamesonGuess.lower() == 'back':
        jamesonBack = True
        break
      elif jamesonGuess in ['pick', 'Pick', 'pk', '0', '0.0']:
         jamesonGuessUpdate = 0.0
         break
      elif jamesonGuess[0] in ['-', '+']:
        try:
          number = float(jamesonGuess[1:])
          jamesonGuessUpdate = number if jamesonGuess[0] == '-' else -number
          break
        except ValueError:
             print("Invalid number after the sign.")
      else:
          print("Guess must start with '+' or '-'.")
    if jamesonBack == True:
        continue
    # ACTUAL LINE

    while True:
      actualLine = input("Enter the Actual Line (Home team perspective): ").strip()
      if actualLine.lower() == 'back':
        actualBack = True
        break
      if actualLine in ['pick', 'Pick', 'pk', '0', '0.0']:
         actualLineUpdate = 0.0
         break
      if actualLine[0] in ['-', '+']:
        try:
          number = float(actualLine[1:])  # this might raise ValueError
          actualLineUpdate = number if actualLine[0] == '-' else -number
          break
        except ValueError:
             print("Invalid number after the sign.")
      else:
        print("Guess must start with '+' or '-'.")
    if actualBack == True:
        continue
    # CALCULATE DISTANCE

    jacksonDistance = abs(jacksonGuessUpdate - actualLineUpdate)
    jamesonDistance = abs(jamesonGuessUpdate - actualLineUpdate)
    
    # Break loop if done
    keepGoing = input(f'Add another game? (y/n): ')
    if keepGoing == 'back':
        continue
    while keepGoing not in ['y', 'n']:
      keepGoing = input(f'Add another game? (y/n): ')
    if jamesonDistance < jacksonDistance:
       score += 1
    if jamesonDistance > jacksonDistance:
       score -= 1

    # Print off interesting stuff
    print(f'\nJackson was off by {jacksonDistance}\nJameson was off by {jamesonDistance}')
    if score < 0:
       print(f'Jackson is winning by {abs(score)}')
    elif score > 0:
       print(f'Jameson is winning by {score}')  
    else:
       print(f'The game is tied')

    # Add to dataframe
    weeklyDf.at[iteration, 'Week'] = week
    weeklyDf.at[iteration, 'Home Team'] = homeTeam
    weeklyDf.at[iteration, 'Away Team'] = awayTeam
    weeklyDf.at[iteration, 'Conference Game'] = conferenceGame
    weeklyDf.at[iteration, 'Jackson Guess'] = jacksonGuess
    weeklyDf.at[iteration, 'Jameson Guess'] = jamesonGuess
    weeklyDf.at[iteration, 'Actual Line'] = actualLine
    weeklyDf.at[iteration, 'Jackson Distance'] = jacksonDistance
    weeklyDf.at[iteration, 'Jameson Distance'] = jamesonDistance
    weeklyDf.at[iteration, 'Score'] = score
    
    # Add one to the index
    iteration += 1

    if keepGoing == 'y':
      weeklyDf.to_csv(f'/Users/jaxen1/Shared/C/Guess the Line/weeks/week{week}gtl.csv')
      continue
    if keepGoing == 'n':
      done = True
ifCsv = input(f'Would you like to print to a .csv? (y/n): ')
while ifCsv not in ['y', 'n']:
    ifCsv = input(f'Would you like to print to a .csv? (y/n): ')
if ifCsv == 'y':
    print(f'Printing to csv as week{week}gtl.csv')
    weeklyDf.to_csv(f'/Users/jaxen1/Shared/C/Guess the Line/weeks/week{week}gtl.csv')

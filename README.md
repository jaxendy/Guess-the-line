#####       Guess the Line       #####

A simple Python game where players try to predict the betting lines for upcoming college football matchups.

Overview:

Each week, the script:
1. Pulls the schedule of college football games.
2. Displays each matchup (home vs. away).
3. Lets each player enter their guessed spread for every game.
4. After the real betting lines are revealed, it compares everyone’s guesses to the actual lines.

Points or scores are then awarded based on how close each player’s predictions were — or through head-to-head “relative” matchups where players compete directly against each other.

Scoring Modes:

The game supports three styles of scoring:
- Point System (p) – Players earn points for being the closest to the actual line each game.
- Relative Matchups (r) – Each player is matched up against every other player. Whoever’s guess is closer earns a win for that matchup.
- Both (b) - Keeps track of score with both the point system and relative matchups system

Files:

- week#.csv – Weekly schedules and results (auto-generated). Used to pull games from past weeks and append to the current week
- guess_the_line.py – Main script that runs the game.

How to Play:

1. Pull the betting lines for games for an upcoming week (preferably from Circa Sports via https://x.com/CircaSports for example https://x.com/CircaSports/status/1974900025529672163). Try to do earlier in the week so lines are sharper
2. Either:
       (Preferred) Use a drawing app to draw over all the lines on the sheet and erase them as you go
       Find a third party that can read the games to you where you can then enter the data into the laptop (so you can not see the lines on the sheet).
4. Run the script:       NOTE: MAKE SURE YOU UPDATE THE FILEPATHS ON LINE ,  AND  TO SAVE WHERE DESIRED. I RECOMMEND MAKING A NEW FOLDER CALLED "Guess the Line" WITH A FOLDER INSIDE CALLED WEEKS
   python guess_the_line.py
6. Choose your scoring system (p (point), r (relative) or b (both).
7. Enter each player’s name.
8. Input your guesses for each matchup.
9. Once the actual lines are available, the script will calculate distances and scores.
10. Do as many games as you want, the csv updates iteratively so you can quit any time.


# Wheel of Fortune
## DEV10 M06 Python Assessment

### 'playGame.py' generates a 3-player, turn-based Wheel of Fortune game
+ 4000-most-common-english-words-csv.csv was taken from: http://www.rupert.id.au/resources/1000-words.php/4000-most-common-english-words-csv.csv and in the game file, I remove all strings w/ length < 10 to ensure longer + more challenging word puzzles
+ simply download the file + word-list, run the file on your computer, and play along with the terminal prompt
+ there are 2 main rounds + a final bonus round where the player with the highest accumulative score can play for an additional prize
+ at the start of each turn, players will spin the wheel and if they land on a money value, they are able to guess one consonant and then are given the option to buy a vowel for $250 + try and solve the whole world puzzle
+ if a player lands on 'Lose a Turn' then the next player in rotation spins the wheel and begins their turn
+ if a player lands on 'Bankrupt' then they lose their turn AND all their earnings in the current round go to 0
+ in the case of a tie in the final bonus round, the program randomly selects one of the players with the highest earnings to proceed

### The goal of this project was to test my basic python skills and measure my proficiency with:
+ variables
+ string manipulation
+ flow control
+ collections (lists,types,sets,dictionaries)
+ functions
+ file I/O
+ and more!

### Thank you for playing + hope you enjoy my Wheel of Fortune game!

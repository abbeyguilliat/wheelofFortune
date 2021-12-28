## WHEEL OF FORTUNE - M06 ASSESSMENT
import random;
import csv;

## import csv
file = open('4000-most-common-english-words-csv.csv','r');
read_file = csv.reader(file);

puzzle_list = [];

for line in read_file:
    puzzle_list.append(line[0]);
    for word in puzzle_list:
        if len(word) < 10: #removes words less than 10 letters
            puzzle_list.remove(word);

## defining collections + variables
wheel = ('Bankrupt', 'Bankrupt', 'Lose a Turn', '100', '150', '200', '250', '300', '300', '350', '400', '450', '500', '500', '550', '600', '650', '700', '750', '800', '850', '900');
#practice_puzzles = ['go hang a salami i a lasagna hog','a beautiful bouquet of red roses for you','a leopard cannot change its spots'];
vowel_dict = {'a','e','i','o','u'};
consonant_dict = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'];
final_round_list = {'r','s','t','l','n','e'};
order_list = [0,1,2]; # used to determine player order at start of round

players = ['Player 1', 'Player 2', 'Player 3'];
winnings = [0,0,0];   # players' total game earnings, does not reset
banks = [0,0,0];      # players' round earnings, resets between rounds

in_play = 0;
turn = in_play % 3;   # gives index for current player in_play
already_guessed = []; 

def determine_order(order_list):
    first_turn = random.choices(order_list);
    first_turn = first_turn[0];
    #print(first_turn, order_list);
    return(first_turn);

def generate_puzzle(puzzle_list):
    word_puzzle = random.choices(puzzle_list);
    word_puzzle = word_puzzle[0];
    puzzle_list.remove(word_puzzle);
    word_puzzle = list(word_puzzle);
    global puzzle_to_solve;
    puzzle_to_solve = [];
    for i in range(0,len(word_puzzle)):
        if word_puzzle[i] == ' ':
            puzzle_to_solve.append(' ');
        else:
            puzzle_to_solve.append('_');
    return(word_puzzle);

def spin_wheel():
    in_spin = True;
    while in_spin == True:
        spin = input("\n%s, press 'Enter' to spin the wheel!" % (players[turn]));
        if spin == "":
            spin_value = random.choices(wheel);
            spin_value = ''.join(spin_value);
            if spin_value == 'Lose a Turn':
                print("\nUh oh! You've land on 'Lose a Turn'. We'll move on to the next player.");
                #in_play += 1;
                return(0)
        
            elif spin_value == 'Bankrupt':
                print("\nOh no! You've landed on 'Bankrupt'. Your current earnings will go to 0 and we'll move on to the next player.");
                banks[turn] = 0;
                #in_play += 1;
                return(0)
            else:
                spin_value = int(spin_value);
                print("\nYou've landed on $%i! If you successfully guess a letter in the word puzzle, $%i will be added to your round earnings for each occurence of the letter.\n" % (spin_value,spin_value));
                return(spin_value);
        else:
            print("Please press 'Enter' to spin the wheel.");

def print_puzzle(puzzle_to_solve):
    temp = "";
    for i in puzzle_to_solve:
        temp += i;
        temp += ' ';
    print(temp);
    return;

def check_guess(guess,word_puzzle,puzzle_to_solve,spin_value):
    prize_multiplier = 0;
    if (guess.lower() in word_puzzle) == False:
        print("\nNo. There are no %ss in the word puzzle." % (guess.upper()));
        #in_play += 1;
    else:
        for i in range(0,len(word_puzzle)):
            if guess == word_puzzle[i]:
                puzzle_to_solve[i] = word_puzzle[i];
                prize_multiplier += 1;
        print("Yes!\n"); 
        print_puzzle(puzzle_to_solve);
        banks[turn] += spin_value * prize_multiplier; 
    print("\n==============\nRound Earnings\n==============\n%s: %i, %s: %i, %s: %i" % (players[0],banks[0],players[1],banks[1],players[2],banks[2]));
    if puzzle_to_solve == word_puzzle:
        print("\nCongrats, %s! You've guessed the final letter in the word puzzle: '%s'. We'll move on to the next round." % (players[turn],' '.join(word_puzzle)));
        max_bank = max(banks);
        if banks.count(max_bank) > 1:
            max_bank_index = [];
            for i in range(0,len(banks)):
                if banks[i] == max_bank:
                    winnings[i] += max_bank;
        else:
            max_bank_index = banks.index(max_bank);
            winnings[max_bank_index] += max_bank;
        print("\n==============\nTotal Earnings\n==============\n%s: %i, %s: %i, %s: %i" % (players[0],winnings[0],players[1],winnings[1],players[2],winnings[2]));
        prize_multiplier = -1;
    return(prize_multiplier);

def buy_vowel(word_puzzle,puzzle_to_solve):
    for vowel in vowel_dict:
        if (vowel in already_guessed) == False:
            in_vowel = True;
            if banks[turn] >= 250:
                while in_vowel == True:
                    buy_vowel = input("\n%s, would you like to buy a vowel? [y/n]: " % (players[turn]));
                    if buy_vowel.lower() == 'y':
                        banks[turn] -= 250;
                        in_guess = True;
                        while in_guess == True:
                            vowel_guess = input("\n%s, please enter a vowel: " % (players[turn]));
                            if (vowel_guess.lower() in vowel_dict) == True:
                                if (vowel_guess.lower() in already_guessed) == False:
                                    already_guessed.append(vowel_guess.lower());
                                    print("\nAre there any %ss?" % (vowel_guess.upper()));
                                    continue_turn = check_guess(vowel_guess,word_puzzle,puzzle_to_solve,0);
                                    return(continue_turn);
                                else:
                                    print("That vowel has already been guessed.")
                            else:
                                print("Invalid input. Please guess a vowel.")
                    elif buy_vowel.lower() == 'n':
                        continue_turn = 1;
                        in_vowel = False;
                    else:
                        print("Invalid input. Please respond with 'y' or 'n'.");
            else:
                continue_turn = 1;
            return(continue_turn);
    print("All vowels have already been bought.");
    return(1);
    
def solve_word(word_puzzle):
    global in_round;
    in_solve = True;
    while in_solve == True:
        solve_word = input("\n%s, would you like to try and solve the word? [y/n]: " % (players[turn]));
        if solve_word.lower() == 'y':
            word_guess = input("\n%s, please enter your guess: " % (players[turn]));
            if word_guess.lower() == ''.join(word_puzzle):
                print("\nCongrats, %s! You've successfully guessed the word puzzle: '%s'. We'll move on to the next round." % (players[turn],word_guess.lower()));
                max_bank = max(banks);
                if banks.count(max_bank) > 1:
                    max_bank_index = [];
                    for i in range(0,len(banks)):
                        if banks[i] == max_bank:
                            winnings[i] += max_bank;
                else:
                    max_bank_index = banks.index(max_bank);
                    winnings[max_bank_index] += max_bank;
                print("\n==============\nTotal Earnings\n==============\n%s: %i, %s: %i, %s: %i" % (players[0],winnings[0],players[1],winnings[1],players[2],winnings[2]));
                continue_turn = -1;
                in_solve = False;
            else:
                print("\nSorry %s, '%s' is incorrect. We'll move on to the next player." % (players[turn],word_guess));
                continue_turn = 0;
                in_solve = False;
        elif solve_word.lower() == 'n':
            continue_turn = 1;
            in_solve = False;
        else:
            print("Invalid input. Please respond with 'y' or 'n'.");
    return(continue_turn);

def get_guess(word_puzzle,puzzle_to_solve,spin_value):
    valid_guess = False;
    print_puzzle(puzzle_to_solve);
    for consonant in consonant_dict:
        if (consonant in already_guessed) == False:
            while valid_guess == False:        
                player_guess = input("\n%s, please guess a letter: " % (players[turn]));
                if len(player_guess) == 1 and player_guess.isalpha() == True:
                    if player_guess.lower() in vowel_dict:
                        print("Invalid guess. Letter must be a consonant.");
                    elif player_guess.lower() in already_guessed:
                        print("That letter has already been guessed.");
                    else:
                        player_guess = player_guess.lower();
                        already_guessed.append(player_guess);
                        print("\nAre there any %ss?" % (player_guess.upper()));
                        valid_guess = True;
                else:
                    print("Invalid guess. Please guess a letter.");
            continue_turn = check_guess(player_guess,word_puzzle,puzzle_to_solve,spin_value);
            if continue_turn == -1:
                return(continue_turn);
            elif continue_turn != 0:
                continue_turn = buy_vowel(word_puzzle,puzzle_to_solve);
                if continue_turn == -1:
                    return(continue_turn);
                elif continue_turn != 0:
                    continue_turn = solve_word(word_puzzle);
            return(continue_turn);
    
    print("\nAll consonants have already been guessed.");
    continue_turn = buy_vowel(word_puzzle,puzzle_to_solve);
    if continue_turn == -1:
        return(continue_turn);
    elif continue_turn != 0:
        continue_turn = solve_word(word_puzzle);
    return(continue_turn);

def guess_final_consonant():
    in_final_guess = True;
    while in_final_guess == True:
        guess = input("\nGuess a consonant: ");
        if len(guess) == 1 and guess.isalpha() == True and (guess.lower() not in vowel_dict) == True and (guess.lower() not in already_guessed) == True and (guess.lower() not in final_round_list) == True:
            already_guessed.append(guess.lower());
            in_final_guess = False;
        elif (guess.lower() in vowel_dict) == True:
            print("\nInvalid input. Please guess a consonant.")
        elif (guess.lower() in already_guessed) == True:
            print("\nYou've already guessed that letter.");
        elif (guess.lower() in final_round_list) == True:
            print("\nWe've already provided you with that letter.")
        else:
            print("\nInvalid input. Please guess a letter.");
    return(guess);

def guess_final_vowel():
    in_final_guess = True;
    while in_final_guess == True:
        guess = input("\nGuess a vowel: ");
        if (guess.lower() in vowel_dict) == True and guess.lower() != 'e':
            already_guessed.append(guess.lower());
            in_final_guess = False;
        elif guess.lower() == 'e':
            print("\nWe've already provided you with that letter.");
        else:
            print("\nInvalid input. Please guess a vowel.");
    return(guess);

start_game = True;
print("\n============================\nWelcome to Wheel of Fortune!\n============================")
while start_game == True:
    play_game = input("\nThis game requires 3 players.\nWould you like to play a game? [y/n]: ")
    if play_game.lower() == 'n':
        print("\nOK. Bye for now!");
        start_game = False;
    elif play_game.lower() == 'y':
        in_game = True;
        round_counter = 0;
        round1 = determine_order(order_list);
        round2 = determine_order(order_list);
        while round2 == round1:
            round2 = determine_order(order_list);
        print("\nGreat, let's begin!");
        while in_game == True:
            round_counter += 1;
            word_puzzle = generate_puzzle(puzzle_list); ## change puzzle list
            already_guessed = [];
            banks = [0,0,0];
            in_round = True;
            if round_counter < 3:
                if round_counter == 1:
                    in_play = round1;
                else:
                    in_play = round2;
                turn = in_play % 3;
                second_turn = (in_play + 1) % 3;
                third_turn = (in_play + 2) % 3;
                print("\nThe order for this round is as follows: %s, %s, %s." % (players[turn],players[second_turn],players[third_turn]));
                while in_round == True:
                    turn = in_play % 3;
                    print("\n%s, you're up!" % (players[turn]));
                    keep_guessing = True;
                    while keep_guessing == True:
                        spin_value = spin_wheel();
                        if spin_value == 0:
                            in_play += 1;
                            keep_guessing = False;
                        else:
                            continue_turn = get_guess(word_puzzle,puzzle_to_solve,spin_value);
                            if continue_turn == 0:
                                in_play += 1;
                                keep_guessing = False;
                            elif continue_turn == -1:
                                keep_guessing = False;
                                in_round = False;
            elif round_counter == 3:
                max_winnings = max(winnings);
                if winnings.count(max_winnings) > 1:
                    print(winnings.count(max_winnings));
                    max_winning_index = [];
                    for i in range(0,len(winnings)):
                        if winnings[i] == max_winnings:
                            max_winning_index.append(i);
                    print(max_winning_index);
                    max_winnings_index = random.choices(max_winning_index)[0];
                    print("\nTwo or more players have earned the highest amount. We have randomly chosen a player to proceed to the final bonus round.")
                else:
                    max_winnings_index = winnings.index(max_winnings);
                final_player = players[max_winnings_index];
                total_winnings = winnings[max_winnings_index];
                print("\nCongrats %s! You earned the highest total winnings and have made it to the final round." % (final_player));
                print("\nFor this round, you will guess 3 consonants and 1 vowel. Then, you may attempt to solve the word puzzle. If you guess correctly, you will earn a $1,000,000 bonus prize!\n");
                print("\nHere is your final word puzzle:");
                for i in range(0,len(word_puzzle)):
                    if (word_puzzle[i] in final_round_list) == True:
                        puzzle_to_solve[i] = word_puzzle[i];
                print_puzzle(puzzle_to_solve);
                print("\nWe have provided you with letters: 'R','S','T','L','N', and 'E'.\n");
                consonant1 = guess_final_consonant();
                consonant2 = guess_final_consonant();
                consonant3 = guess_final_consonant();
                vowel = guess_final_vowel();
                print("\nGreat!\n%s, here are your guesses: %s, %s, %s, and %s." % (final_player,consonant1.lower(),consonant2.lower(),consonant3.lower(),vowel.lower()));
                for i in range(0,len(word_puzzle)):
                    if (word_puzzle[i] in already_guessed) == True:
                        puzzle_to_solve[i] = word_puzzle[i];
                print_puzzle(puzzle_to_solve);
                print("\n%s, you only have one chance to solve the puzzle." % (final_player))
                final_guess = input("Make your guess: ");
                if ''.join(final_guess).lower() == ''.join(word_puzzle):
                    print("\nCongrats %s! The puzzle was '%s'. You've guessed correctly and will receive the $1,000,000 bonus!" % (final_player,' '.join(word_puzzle)));
                    total_winnings += 1000000;
                    print("\nYou've won a grand prize total of $%i!" % (total_winnings));
                else:
                    print("\nSorry, %s. You did not guess correctly. The word puzzle was: '%s'." % (final_player,' '.join(word_puzzle)));
                    print("\nYou will not receive the $1,000,000 bonus but will still take home your earnings from the previous rounds.");
                    print("\nYou've won a total of $%i." % (total_winnings));
                print("\nThank you for playing Wheel of Fortune!\nGAME OVER");
                in_round = False;
                in_game = False;
                start_game = False;       
    else:
        print("Invalid input. Please respond with 'y' or 'n'.");
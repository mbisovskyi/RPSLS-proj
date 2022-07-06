from human import Human
from ai import Ai

class SinglePlayer:
    def __init__(self):
        self.human = Human()
        self.ai = Ai()
        self.human_gesture = None
        self.ai_gesture = None
        self.human_score_counter = 0
        self.ai_score_counter = 0
        self.round_counter = 0

    def run_singleplayer(self):
         while self.human_score_counter != 2 and self.ai_score_counter != 2:
            self.players_picked_gestures()
            print(self.ai_gesture)
            self.compare_gestures()
            print(self.ai_score_counter, self.human_score_counter)
            self.round_counter += 1
            self.score_comparison()

    def players_picked_gestures(self):
        self.human_gesture = self.human.picked_gesture()
        self.ai_gesture = self.ai.picked_gesture()

    def compare_gestures(self):
            if self.human_gesture == self.ai_gesture:
                self.tie_result()
            elif self.human_gesture == 'Rock':
                self.rock_wins()
            elif self.human_gesture == 'Paper':
                self.paper_wins()
            elif self.human_gesture == 'Scissors':
                self.scissors_wins()
            elif self.human_gesture == 'Lizard':
                self.lizard_wins()
            elif self.human_gesture == 'Spock':
                self.spock_wins()    

    def tie_result(self):
        if self.human_gesture == self.ai_gesture:
            print(f'No one wins. Player picked {self.human_gesture} and Ai picked {self.ai_gesture}!')

    def rock_wins(self):
        if self.ai_gesture == 'Lizard' or self.ai_gesture == 'Scissors':
            print(f'Player wins!')
            print(f'Rock crushes {self.ai_gesture}')
            player_wins = True 
        elif self.ai_gesture == 'Paper':
            print(f'Ai wins. {self.ai_gesture} covers rock!')
            player_wins = False 
        elif self.ai_gesture == 'Spock':
            print(f'Ai wins. {self.ai_gesture} vaporizes rock!')
            player_wins = False 
        self.round_winner(player_wins)
            
    def paper_wins(self):
        if self.ai_gesture == 'Rock':
            print(f'Player wins!')
            print(f'Paper covers Rock!')
            player_wins = True
        elif self.ai_gesture == 'Spock':
            print(f'Player wins!')
            print(f'Paper disproves Spock!')
            player_wins = True
        elif self.ai_gesture == 'Scissors':
            print(f'Ai wins. {self.ai_gesture} cuts paper!')
            player_wins = False
        elif self.ai_gesture == 'Lizard':
            print(f'Ai wins. {self.ai_gesture} eats paper!')
            player_wins = False
        self.round_winner(player_wins)

    def scissors_wins(self):
        if self.ai_gesture == 'Paper':
            print(f'Player wins!')
            print(f'Scissors cuts paper!')
            player_wins = True
        elif self.ai_gesture == 'Lizard':
            print(f'Player wins!')
            print(f'Scissors decapitates Lizard!')
            player_wins = True
        elif self.ai_gesture == 'Rock':
            print(f'Ai wins. {self.ai_gesture} crushes scissors!')
            player_wins = False
        elif self.ai_gesture == 'Spock':
            print(f'Ai wins. {self.ai_gesture} smashes scissors!')
            player_wins = False
        self.round_winner(player_wins)

    def lizard_wins(self):
        if self.ai_gesture == 'Spock':
            print(f'Player wins!')
            print(f'Lizard poisons spock!')
            player_wins = True
        elif self.ai_gesture == 'Paper':
            print(f'Player wins!')
            print(f'Lizard eats paper')
            player_wins = True
        elif self.ai_gesture == 'Rock':
            print(f'Ai wins. {self.ai_gesture} crushes lizard!')
            player_wins = False
        elif self.ai_gesture == 'Scissors':
            print(f'Ai wins. {self.ai_gesture} decapitates lizard!')
            player_wins = False
        self.round_winner(player_wins)

    def spock_wins(self):
        if self.ai_gesture == 'Scissors':
            print(f'Player wins!')
            print(f'Spock smashes scissors!')
            player_wins = True
        if self.ai_gesture == 'Rock':
            print(f'Player wins!')
            print(f'Spock vaporizes rock!')
            player_wins = True
        elif self.ai_gesture == 'Lizard':
            print(f'Ai wins. {self.ai_gesture} poisons spock!')
            player_wins = False
        elif self.ai_gesture == 'Paper':
            print(f'Ai wins. {self.ai_gesture} disproves spock!')
            player_wins = False
        self.round_winner(player_wins)

    def round_winner(self, player_wins):
        if player_wins == True:
            self.human_score_counter += 1
        else:
            self.ai_score_counter += 1

    def score_comparison(self):
        if self.human_score_counter == 2:
            print('Player won this game!')
        elif self.ai_score_counter == 2:
            print('Ai won this game')
    



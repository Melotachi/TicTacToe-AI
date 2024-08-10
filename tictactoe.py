

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use a single list to represent 3x3 board
        self.current_winner = None
        self.played = 0
        self.is_playable = True
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def is_game_over(self, board):
        # check rows
        for row in [board[i*3:(i+1)*3] for i in range(3)]:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                self.current_winner = row[0]
                return True
        
        # check columns
        for col in [board[i::3] for i in range(3)]:
            if col[0] == col[1] == col[2] and col[0] != ' ':
                self.current_winner = col[0]
                return True
        
        # check diagonals
        if board[0] == board[4] == board[8] and board[0] != ' ':
            self.current_winner = board[0]
            return True
        
        if board[2] == board[4] == board[6] and board[2] != ' ':
            self.current_winner = board[2]
            return True
        
        if all(cell != ' ' for cell in board):
            return True
        
        return False


    
    def play(self):
        while self.is_playable:
            self.print_board()
            try:
                move = int(input('Enter your move (0-8): '))
                if self.board[move] == ' ':
                    self.board[move] = 'X'
                    self.played += 1
                    if self.is_game_over(self.board):
                        self.print_board()
                        if self.current_winner:
                            print(f'{self.current_winner} wins!')
                        else:
                            print('It\'s a tie!')
                        self.is_playable = False
                    else:
                        self.print_board()
                        print('Computer\'s turn...')
                        self.computer_move(self.board)
                        if self.is_game_over(self.board):
                            self.print_board()
                            if self.current_winner:
                                print(f'{self.current_winner} wins!')
                            else:
                                print('It\'s a tie!')
                            self.is_playable = False
                else:
                    print('Invalid move! Try again.')
            except ValueError:
                print('Invalid input! Try again.')
                
                
    def minimax(self, board, is_maximizing):
        if self.is_game_over(board):
            if self.current_winner == 'X':
                self.current_winner = None # reset current_winner because the game might not be over, we are just checking possible moves
                return -1 
            elif self.current_winner == 'O':
                self.current_winner = None # reset current_winner because the game might not be over, we are just checking possible moves
                return 1 
            else:
                return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    
    
    def computer_move(self,board):
        best_score = -float('inf')
        best_move = None

        for i in range(9):
            if self.board[i] == ' ':
                board[i] = 'O'
                score = self.minimax(board, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        
        # we do not need to check if best_move is None because we are sure that there is an empty cell since we are checking for it in the loop in the play function
        self.board[best_move] = 'O'
        self.played += 1

                
            
        
    
    
        





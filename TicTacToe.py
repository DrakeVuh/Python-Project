import random
import os
import time
from typing import List, Tuple, Optional
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

class TicTacToe:
    """A colorful and professional Tic Tac Toe game implementation."""
    
    def __init__(self):
        """Initialize the game with an empty board."""
        self.board = self._create_board()
        self.player_symbol = ''
        self.computer_symbol = ''
        
    def _create_board(self) -> List[List[str]]:
        """Create an empty 3x3 game board."""
        return [[' ' for _ in range(3)] for _ in range(3)]
        
    def display_board(self):
        """Display the game board with colors and styling."""
        # Clear screen for better presentation
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Display game header
        print(f"\n{Fore.CYAN}{Style.BRIGHT}==========================================")
        print(f"{Fore.YELLOW}{Style.BRIGHT}          T I C  T A C  T O E           ")
        print(f"{Fore.CYAN}{Style.BRIGHT}==========================================\n")
        
        # Show position legend
        print(f"{Fore.WHITE}Positions:")
        print(f"{Fore.BLUE} 1 | 2 | 3 ")
        print(f"{Fore.BLUE}---+---+---")
        print(f"{Fore.BLUE} 4 | 5 | 6 ")
        print(f"{Fore.BLUE}---+---+---")
        print(f"{Fore.BLUE} 7 | 8 | 9 \n")
        
        # Print current board state
        print(f"{Fore.WHITE}Current Board:")
        print(f"{Fore.MAGENTA}┌───┬───┬───┐")
        for i, row in enumerate(self.board):
            colored_cells = []
            for cell in row:
                if cell == 'X':
                    colored_cells.append(f"{Fore.RED}{Style.BRIGHT}X{Style.RESET_ALL}")
                elif cell == 'O':
                    colored_cells.append(f"{Fore.GREEN}{Style.BRIGHT}O{Style.RESET_ALL}")
                else:
                    colored_cells.append(" ")
            print(f"{Fore.MAGENTA}│ {colored_cells[0]} │ {colored_cells[1]} │ {colored_cells[2]} │")
            if i < 2:
                print(f"{Fore.MAGENTA}├───┼───┼───┤")
        print(f"{Fore.MAGENTA}└───┴───┴───┘\n")
    
    def choose_player_symbol(self) -> None:
        """Let the player choose their symbol (X or O)."""
        while self.player_symbol not in ['X', 'O']:
            choice = input(f"{Fore.YELLOW}Do you want to be {Fore.RED}X{Fore.YELLOW} or {Fore.GREEN}O{Fore.YELLOW}? ").upper()
            if choice in ['X', 'O']:
                self.player_symbol = choice
                self.computer_symbol = 'O' if choice == 'X' else 'X'
                print(f"{Fore.CYAN}You chose: {Fore.WHITE}{self.player_symbol}")
                time.sleep(1)
            else:
                print(f"{Fore.RED}Invalid choice. Please select X or O.")
    
    def is_space_free(self, row: int, col: int) -> bool:
        """Check if a position on the board is free."""
        return self.board[row][col] == ' '
    
    def player_move(self) -> None:
        """Handle the player's move with input validation."""
        print(f"{Fore.YELLOW}Your turn ({Fore.WHITE}{self.player_symbol}{Fore.YELLOW}).")
        while True:
            try:
                move = int(input(f"{Fore.WHITE}Enter your move (1-9): "))
                row, col = (move - 1) // 3, (move - 1) % 3
                
                if move < 1 or move > 9:
                    print(f"{Fore.RED}Please enter a number from 1 to 9.")
                elif not self.is_space_free(row, col):
                    print(f"{Fore.RED}That space is already taken.")
                else:
                    self.board[row][col] = self.player_symbol
                    break
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.")
    
    def computer_move(self) -> None:
        """Handle the computer's move with some simple AI."""
        print(f"{Fore.YELLOW}Computer's turn ({Fore.WHITE}{self.computer_symbol}{Fore.YELLOW}).")
        time.sleep(0.5)  # Add a small delay to simulate thinking
        
        # Try to win
        winning_move = self._find_winning_move(self.computer_symbol)
        if winning_move:
            row, col = winning_move
            self.board[row][col] = self.computer_symbol
            return
            
        # Block player's winning move
        blocking_move = self._find_winning_move(self.player_symbol)
        if blocking_move:
            row, col = blocking_move
            self.board[row][col] = self.computer_symbol
            return
            
        # Take center if available
        if self.is_space_free(1, 1):
            self.board[1][1] = self.computer_symbol
            return
            
        # Take a corner
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [corner for corner in corners if self.is_space_free(corner[0], corner[1])]
        if available_corners:
            row, col = random.choice(available_corners)
            self.board[row][col] = self.computer_symbol
            return
            
        # Take any available edge
        edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
        available_edges = [edge for edge in edges if self.is_space_free(edge[0], edge[1])]
        if available_edges:
            row, col = random.choice(available_edges)
            self.board[row][col] = self.computer_symbol
            return
            
        # Fallback to random move (should rarely happen)
        possible_moves = [(r, c) for r in range(3) for c in range(3) if self.is_space_free(r, c)]
        if possible_moves:
            row, col = random.choice(possible_moves)
            self.board[row][col] = self.computer_symbol
    
    def _find_winning_move(self, symbol: str) -> Optional[Tuple[int, int]]:
        """Find a winning move for the given symbol."""
        # Check rows and columns
        for i in range(3):
            # Check rows
            if self.board[i].count(symbol) == 2 and ' ' in self.board[i]:
                col = self.board[i].index(' ')
                return i, col
                
            # Check columns
            col_values = [self.board[j][i] for j in range(3)]
            if col_values.count(symbol) == 2 and ' ' in col_values:
                row = col_values.index(' ')
                return row, i
                
        # Check diagonals
        diag1 = [self.board[i][i] for i in range(3)]
        if diag1.count(symbol) == 2 and ' ' in diag1:
            i = diag1.index(' ')
            return i, i
            
        diag2 = [self.board[i][2-i] for i in range(3)]
        if diag2.count(symbol) == 2 and ' ' in diag2:
            i = diag2.index(' ')
            return i, 2-i
            
        return None
    
    def check_win(self, symbol: str) -> bool:
        """Check if the given symbol has won the game."""
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or all(self.board[j][i] == symbol for j in range(3)):
                return True
                
        # Check diagonals
        if all(self.board[i][i] == symbol for i in range(3)) or all(self.board[i][2-i] == symbol for i in range(3)):
            return True
            
        return False
    
    def is_board_full(self) -> bool:
        """Check if the board is full (tie game)."""
        return all(self.board[r][c] != ' ' for r in range(3) for c in range(3))
    
    def display_result(self, result: str) -> None:
        """Display the game result with colorful formatting."""
        self.display_board()
        
        print(f"{Fore.CYAN}{Style.BRIGHT}==========================================")
        if result == "player_win":
            print(f"{Fore.GREEN}{Style.BRIGHT}          🎉  YOU WIN!  🎉           ")
        elif result == "computer_win":
            print(f"{Fore.RED}{Style.BRIGHT}        😞  COMPUTER WINS  😞         ")
        else:  # Tie
            print(f"{Fore.YELLOW}{Style.BRIGHT}         🤝  IT'S A TIE!  🤝          ")
        print(f"{Fore.CYAN}{Style.BRIGHT}==========================================\n")
    
    def play_again(self) -> bool:
        """Ask if the player wants to play again."""
        while True:
            choice = input(f"{Fore.YELLOW}Play again? (y/n): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print(f"{Fore.RED}Invalid choice. Please enter 'y' or 'n'.")
    
    def play(self) -> None:
        """Main game loop."""
        while True:
            # Reset game
            self.board = self._create_board()
            self.choose_player_symbol()
            
            # Randomly decide who goes first
            current_turn = 'player' if random.choice([True, False]) else 'computer'
            if current_turn == 'player':
                print(f"{Fore.CYAN}You go first!")
            else:
                print(f"{Fore.CYAN}Computer goes first!")
            time.sleep(1)
            
            # Game loop
            while True:
                self.display_board()
                
                if current_turn == 'player':
                    self.player_move()
                    if self.check_win(self.player_symbol):
                        self.display_result("player_win")
                        break
                    current_turn = 'computer'
                else:
                    self.computer_move()
                    if self.check_win(self.computer_symbol):
                        self.display_result("computer_win")
                        break
                    current_turn = 'player'
                
                if self.is_board_full():
                    self.display_result("tie")
                    break
            
            if not self.play_again():
                print(f"{Fore.CYAN}Thanks for playing! Goodbye!")
                break

def main():
    """Main function to start the game."""
    # Check if colorama is installed
    try:
        import colorama
    except ImportError:
        print("Colorama is not installed. Installing now...")
        try:
            os.system('pip install colorama')
            print("Colorama installed successfully!")
            time.sleep(1)
            # Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print("Failed to install colorama. The game will run with limited styling.")
    
    # Start the game
    game = TicTacToe()
    game.play()

if __name__ == "__main__":
    main()
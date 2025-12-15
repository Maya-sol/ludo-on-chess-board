import pygame
import sys
from ludoconst import *
from ludogame import *

class GUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        pygame.display.set_caption("Ludo on chess board")
        self.clock = pygame.time.Clock()
        self.selected = False
        self.game = Ludo()

    def draw_board(self):
        self.screen.fill(BROWN)
        for row in range(8):
            for col in range(8):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                cell_rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
           
                if ((row + col)%2 == 0):
                    pygame.draw.rect(self.screen, LIGHT_BROWN, cell_rect)
            
                pygame.draw.rect(self.screen, BLACK, cell_rect, 1)
        
        cell_rect = pygame.Rect(WIDTH, 0, HEIGHT - WIDTH, WIDTH)
        pygame.draw.rect(self.screen, SIDE, cell_rect)
        pygame.draw.rect(self.screen, BLACK, cell_rect,1)

        font = pygame.font.Font(None, 50)
        text = str(self.game.dice)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = ((HEIGHT + WIDTH) // 2, (2*WIDTH - SQUARE_SIZE) // 4)
        background_rect = pygame.Rect((HEIGHT + WIDTH) // 2 - SQUARE_SIZE//2 , WIDTH // 2 - SQUARE_SIZE//2 , SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(self.screen, WHITE, background_rect)
        self.screen.blit(text_surface, text_rect)
        
        text = str(self.game.turn)
        text_surface = font.render(text, True, BLACK)
        text_rect.center = ((HEIGHT + WIDTH) // 2, (2*WIDTH + SQUARE_SIZE) // 4)
        self.screen.blit(text_surface, text_rect)
        
    def draw_pieces(self):
        grid = self.game.board.grid
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if grid[i][j] != '.':
                    x = j * SQUARE_SIZE + SQUARE_SIZE // 2
                    y = i* SQUARE_SIZE + SQUARE_SIZE // 2
    
                    if grid[i][j] == 'B':
                        color = BLUE
                    else:  
                        color = RED

                    pygame.draw.circle(self.screen, color, (x, y), 30)
                    pygame.draw.circle(self.screen, BLACK, (x, y), 30, 2)
        

    def draw_start(self):
        if self.game.check_start():
            font = pygame.font.Font(None, 50)
            text = 'start'
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = ((HEIGHT + WIDTH) // 2, WIDTH // 2 + SQUARE_SIZE *1.25)
            background_rect = pygame.Rect((HEIGHT + WIDTH) // 2 - SQUARE_SIZE//2 , WIDTH // 2 + SQUARE_SIZE , SQUARE_SIZE, SQUARE_SIZE//2)
            pygame.draw.rect(self.screen, WHITE, background_rect)
            self.screen.blit(text_surface, text_rect)
        
    def draw_moves(self):
        for i in self.game.moves:
            if i != 'start':
                row, col = i
                x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = row * SQUARE_SIZE + SQUARE_SIZE // 2 
                color = WHITE
    
                pygame.draw.circle(self.screen, color, (x, y), 10)


    def start(self):
        self.game.start()

    def handle_click(self, pos):
        if ((HEIGHT + WIDTH) // 2 - SQUARE_SIZE//2 <=pos[0]<= (HEIGHT + WIDTH) // 2 + SQUARE_SIZE//2) and (WIDTH // 2 + SQUARE_SIZE <= pos[1] <= WIDTH // 2 + SQUARE_SIZE*1.5):
            self.start()
            return -1
        x = pos[1]// SQUARE_SIZE
        y = pos[0] // SQUARE_SIZE

        
        for i in range (len(gui.game.moves)):
            if (x,y) == gui.game.moves[i]:
                return i
    
    def show_winner(self):
        font = pygame.font.Font(None, 100)
        text_surface = font.render(self.game.winner + " Wins!", True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH // 2, WIDTH // 2)
        background_rect = pygame.Rect(0, WIDTH//2 - SQUARE_SIZE, WIDTH, 2*SQUARE_SIZE)
        pygame.draw.rect(self.screen, (30,30,30), background_rect)
        self.screen.blit(text_surface, text_rect)

    def show_choose_mood(self):
        self.screen.fill(BROWN)
        cell_rect = pygame.Rect( HEIGHT//2 - SQUARE_SIZE*2, WIDTH//2 - SQUARE_SIZE*2, SQUARE_SIZE*4, SQUARE_SIZE*4)
        pygame.draw.rect(self.screen, SIDE, cell_rect)
        pygame.draw.rect(self.screen, WHITE, cell_rect,1)
        pygame.draw.line(self.screen, WHITE, (HEIGHT//2 - SQUARE_SIZE*2, WIDTH//2), (HEIGHT//2 + SQUARE_SIZE*2 -1,WIDTH//2), 1)
        font = pygame.font.Font(None, 70)
        text_surface = font.render("VS. BOT", True, WHITE)
        self.screen.blit(text_surface, text_surface.get_rect(center=(HEIGHT//2, WIDTH//2 - SQUARE_SIZE)))
        text_surface = font.render("VS. Friend", True, WHITE)
        self.screen.blit(text_surface, text_surface.get_rect(center=(HEIGHT//2, WIDTH//2 + SQUARE_SIZE)))

    def choose_mood(self, pos):
        if HEIGHT//2 - SQUARE_SIZE*2 <= pos[0] <=  HEIGHT//2 + SQUARE_SIZE*2 :
            if WIDTH//2 - 2*SQUARE_SIZE <= pos[1] <= WIDTH//2:
                return 0
            elif  WIDTH//2 <= pos[1] <= WIDTH//2 + 2*SQUARE_SIZE:
                return 1
            return





if __name__ == "__main__":
    pygame.init()
    gui = GUI()
    game = gui.game
    mood = None
    running = True
    while mood is None and running:
        gui.show_choose_mood()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mood = gui.choose_mood(event.pos)
                    
    if mood is not None:
        running = True
        if mood == 0:
            bot = Bot(game.board)
    while running:
        i = None
        gui.draw_board()
        gui.draw_pieces()
        gui.draw_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if game.moves:
            gui.draw_moves()
            pygame.display.update()
            if (mood == 0 and game.turn == 'B'):
                pygame.time.delay(600)
                i = bot.choose_move(game.moves)
                if game.moves[i] == 'start':
                    gui.start()
                    i = -1
            while i is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            i = gui.handle_click(event.pos)
                if not running:
                    break
            if not running:
                break
            if i != -1:
                removed = game.board.get_piece_at(game.moves[i][0], game.moves[i][1])
                if removed is not None:
                    removed.move((-1 , -1))
                game.board.update_piece_position(game.ids[i].position, game.moves[i])
                if game.check_arrive(game.moves[i]):
                    removed = game.arrive()
                    if game.turn == 'B':
                        game.board.update_piece_position((0,0), removed)
                    else:
                        game.board.update_piece_position((7,7), removed)
                    game.remove(removed)
                    if game.check_win():
                        running = False
                else: 
                    game.ids[i].move(game.moves[i])
            game.moves =[]
            game.ids =[]   
        game.change_turn()
        game.roll()
        game.get_valid_moves()


        pygame.display.update()
        gui.clock.tick(FRAMES_PER_SECOND)
    if (game.winner is not None):
        running = True
        while running: 
            gui.draw_board()
            gui.draw_pieces()
            gui.show_winner()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            gui.clock.tick(FRAMES_PER_SECOND)
        print(game.winner + ' wins!')
    
    pygame.quit()
    sys.exit()

import pygame
import sys
from tkinter import filedialog

from createbeats import beatarray

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

POSITION_A = 187
POSITION_B = 258
POSITION_C = 329
POSITION_D = 400
POSITION_E = 471
POSITION_F = 542

SPEED = 3
VISUAL_LATENCY = 80

STRUM_POSITION = 500

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

strum = pygame.image.load('assets/notestrum.png')

pressed = pygame.image.load('assets/pressed.png')

pygame.display.set_caption('Rhythm Game')

class Button():
	def __init__(self, pos, text_input, font, base_color, hover_color):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hover_color = base_color, hover_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hover_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def main_menu():
    while True:
        screen.fill(BLACK)

        pos = pygame.mouse.get_pos()

        menu_text = pygame.font.SysFont("Roboto", 100).render("Rhythm Game", True, "#ff5c5c")
        menu_rect = menu_text.get_rect(center=(400, 100))

        play_button = Button(pos=(400, 250), text_input="Play", font=pygame.font.SysFont("Roboto", 80), base_color="#60d4fc", hover_color="White")
        quit_button = Button(pos=(400, 400), text_input="Quit", font=pygame.font.SysFont("Roboto", 80), base_color="#60d4fc", hover_color="White")

        screen.blit(menu_text, menu_rect)

        play_button.changeColor(pos)
        play_button.update(screen)
    
        quit_button.changeColor(pos)
        quit_button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(pos):
                    choose_song()
                if quit_button.checkForInput(pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def choose_song():
    while True:
        screen.fill(BLACK)

        pos = pygame.mouse.get_pos()

        menu_text = pygame.font.SysFont("Roboto", 100).render("Choose Difficulty", True, "#ff5c5c")
        menu_rect = menu_text.get_rect(center=(400, 100))

        easy_button = Button(pos=(400, 250), text_input="Easy", font=pygame.font.SysFont("Roboto", 80), base_color="#60d4fc", hover_color="White")
        hard_button = Button(pos=(400, 400), text_input="Hard", font=pygame.font.SysFont("Roboto", 80), base_color="#60d4fc", hover_color="White")
        back_button = Button(pos=(100, 550), text_input="Back", font=pygame.font.SysFont("Roboto", 40), base_color="#60d4fc", hover_color="White")

        screen.blit(menu_text, menu_rect)

        easy_button.changeColor(pos)
        easy_button.update(screen)
    
        hard_button.changeColor(pos)
        hard_button.update(screen)

        back_button.changeColor(pos)
        back_button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.checkForInput(pos):
                    initialize('easy')
                if hard_button.checkForInput(pos):
                    initialize('hard')
                if back_button.checkForInput(pos):
                    main_menu()

        pygame.display.update()

class Note(pygame.sprite.Sprite):
    def __init__(self, identity, strumTime, position):
        pygame.sprite.Sprite.__init__(self)
        self.idnum = identity
        self.strum = strumTime
        self.miss = False
        self.hit = False
        self.difference = -2000000
        if position == 1:
            self.image = pygame.image.load('assets/noteA.png')
            self.rect = self.image.get_rect()
            self.rect.move_ip(POSITION_A, -100)
        if position == 2:
            self.image = pygame.image.load('assets/noteB.png')
            self.rect = self.image.get_rect()
            self.rect.move_ip(POSITION_B, -100)
        if position == 3:
            self.image = pygame.image.load('assets/noteC.png')
            self.rect = self.image.get_rect()
            self.rect.move_ip(POSITION_C, -100)
        if position == 4:
            self.image = pygame.image.load('assets/noteC.png')
            self.rect = self.image.get_rect()
            self.rect.move_ip(POSITION_D, -100)
        if position == 5:
            self.image = pygame.image.load('assets/noteB.png')
            self.rect = self.image.get_rect()
            self.rect.move_ip(POSITION_E, -100)
        if position == 6:
            self.image = pygame.image.load('assets/noteA.png')
            self.rect = self.image.get_rect()
            self.rect.move_ip(POSITION_F, -100)

    def update(self, pressed, time):

        if self.hit or self.miss:
            self.kill()

        if not self.hit and not self.miss and self.rect.centery > 520:
            self.miss = True
            self.difference = -1000000

        if self.rect.centery > 480 and not self.miss and pressed:
            if not self.hit:
                pressed = False
                self.difference = self.strum - time

            self.hit = True

    def move(self, shift):
        if shift > 0:
            self.rect.centery = shift

def combo_count(amount):
    font = pygame.font.SysFont("Roboto", 40)
    text = font.render( f"Combo: {amount}", True, WHITE)
    screen.blit(text, (20, 20))

def multiplier_count(amount):
    font = pygame.font.SysFont("Roboto", 40)
    text = font.render( f"{amount}x", True, WHITE)
    screen.blit(text, (20, 50))

def score_count(score_amount):
    font = pygame.font.SysFont("Roboto", 40)
    text = font.render(f"{score_amount}", True, WHITE)
    screen.blit(text, (630, 20))

def initialize(difficulty):
    audio_file_name = ''
    audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".flac .mp3"), ("All Files", "*.*")))

    if audio_file_name == '':
        choose_song()

    print('Loading...')

    try:
        beatmap, ending_time = beatarray(audio_file_name, difficulty)
    except:
        print('Unable to read audio file')
        main_menu()

    game_loop(audio_file_name, beatmap, ending_time)

def game_loop(file_name, beatmap, ending_time):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.set_volume(0.1)

    combo = 0
    score = 0
    multipier = 1

    keypressS = False
    keypressD = False
    keypressF = False
    keypressJ = False
    keypressK = False
    keypressL = False

    notesA = pygame.sprite.Group()
    notesB = pygame.sprite.Group()
    notesC = pygame.sprite.Group()
    notesD = pygame.sprite.Group()
    notesE = pygame.sprite.Group()
    notesF = pygame.sprite.Group()

    note_dict = {
        1: notesA.add,
        2: notesB.add,
        3: notesC.add,
        4: notesD.add,
        5: notesE.add,
        6: notesF.add,
    }

    for idx, beat in enumerate(beatmap):
        timing = beat['time']
        position = beat['position']
        note_dict[position](Note(idx, timing, position))

    print('Loading Done!')

    current = 0
    previousframetime = 0
    lastplayheadposition = 0
    mostaccurate = 0

    pygame.mixer.music.play()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    keypressS = True
                if event.key == pygame.K_d:
                    keypressD = True
                if event.key == pygame.K_f:
                    keypressF = True
                if event.key == pygame.K_j:
                    keypressJ = True
                if event.key == pygame.K_k:
                    keypressK = True
                if event.key == pygame.K_l:
                    keypressL = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    keypressS = False
                if event.key == pygame.K_d:
                    keypressD = False
                if event.key == pygame.K_f:
                    keypressF = False
                if event.key == pygame.K_j:
                    keypressJ = False
                if event.key == pygame.K_k:
                    keypressK = False
                if event.key == pygame.K_l:
                    keypressL = False

        current += clock.get_time()

        if current >= ending_time:
            pygame.mixer.music.unload()
            main_menu()

        mostaccurate += current - previousframetime
        previousframetime = current
        songtime = pygame.mixer.music.get_pos()
        if songtime != lastplayheadposition:
            mostaccurate = (mostaccurate + songtime)/2
            lastplayheadposition = songtime
    
        if combo < 10:
            multipier = 1
        if 10 <= combo < 20:
            multipier = 2
        elif 20 <= combo < 30:
            multipier = 3
        elif 30 <= combo:
            multipier = 4

        screen.fill(BLACK)
        combo_count(combo)
        multiplier_count(multipier)
        score_count(score)

        if keypressS:
            screen.blit(pressed, (POSITION_A, 494))
        if keypressD:
            screen.blit(pressed, (POSITION_B, 494))
        if keypressF:
            screen.blit(pressed, (POSITION_C, 494))
        if keypressJ:
            screen.blit(pressed, (POSITION_D, 494))
        if keypressK:
            screen.blit(pressed, (POSITION_E, 494))
        if keypressL:
            screen.blit(pressed, (POSITION_F, 494))

        notesA.draw(screen)
        notesB.draw(screen)
        notesC.draw(screen)
        notesD.draw(screen)
        notesE.draw(screen)
        notesF.draw(screen)

        screen.blit(strum, (0, 0))

        for note in notesA:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusa = note.difference
            if -500 <= statusa <= 500:
                combo += 1
                score += 1000 * multipier
            elif statusa == -1000000:
                combo = 0

        for note in notesB:
            distances = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distances)
            statusb = note.difference
            if -500 <= statusb <= 500:
                combo += 1
                score += 1000 * multipier
            elif statusb == -1000000:
                combo = 0

        for note in notesC:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusc = note.difference
            if -500 <= statusc <= 500:
                combo += 1
                score += 1000 * multipier
            elif statusc == -1000000:
                combo = 0

        for note in notesD:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusd = note.difference
            if -500 <= statusd <= 500:
                combo += 1
                score += 1000 * multipier
            elif statusd == -1000000:
                combo = 0

        for note in notesE:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statuse = note.difference
            if -500 <= statuse <= 500:
                combo += 1
                score += 1000 * multipier
            elif statuse == -1000000:
                combo = 0

        for note in notesF:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusf = note.difference
            if -500 <= statusf <= 500:
                combo += 1
                score += 1000 * multipier
            elif statusf == -1000000:
                combo = 0

        notesA.update(keypressS, mostaccurate)
        notesB.update(keypressD, mostaccurate)
        notesC.update(keypressF, mostaccurate)
        notesD.update(keypressJ, mostaccurate)
        notesE.update(keypressK, mostaccurate)
        notesF.update(keypressL, mostaccurate)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main_menu()

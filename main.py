import pygame
import json
import sys

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

NOTE_TIMES = []
NOTE_POSITIONS = []

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

strum = pygame.image.load('assets/notestrum.png')

pressed = pygame.image.load('assets/pressed.png')

pygame.display.set_caption('Rhythm Game')

clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text('Main Menu', pygame.font.SysFont("comicsansms", 30), WHITE, screen, 330, 40)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 100, 200, 50)
        button_2 = pygame.Rect(300, 180, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game_loop()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        draw_text('Play', pygame.font.SysFont("comicsansms", 30), WHITE, screen, 370, 110)
        draw_text('Quit', pygame.font.SysFont("comicsansms", 30), WHITE, screen, 355, 190)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(FPS)

class Note(pygame.sprite.Sprite):
    def __init__(self, screen, identity, strumTime, position):
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

def initialize(song_name):
    f = open(song_name + '.json')
    data = json.load(f)
    for i in data['notes']:
        NOTE_TIMES.append(i['time'])
        NOTE_POSITIONS.append(i['position'])
    f.close()
    pygame.mixer.music.load(song_name + '.mp3')

def combo_count(amount):
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render("Combo: " + str(amount), True, WHITE)
    screen.blit(text, (20, 20))

def score_count(score_amount):
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render("Score: " + str(score_amount), True, WHITE)
    screen.blit(text, (620, 20))

def debug_time(current, mostaccurate, previousframetime, songtime):
    font = pygame.font.SysFont("comicsansms", 15)
    text = font.render("current: " + str(current), True, WHITE)
    screen.blit(text, (620, 300))
    text = font.render("mostaccurate: " + str(mostaccurate), True, WHITE)
    screen.blit(text, (620, 315))
    text = font.render("previousframetime: " + str(previousframetime), True, WHITE)
    screen.blit(text, (620, 330))
    text = font.render("songtime: " + str(songtime), True, WHITE)
    screen.blit(text, (620, 345))

def debug_key(debugkey, mostaccurate):
    keyspressed = ""
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render("time pressed: " + str(mostaccurate), True, WHITE)
    screen.blit(text, (620, 370))
    for key in debugkey:
        keyspressed = keyspressed + " " + key
    text = font.render("keys pressed: " + str(keyspressed), True, WHITE)
    screen.blit(text, (620, 390))

def game_loop():
    initialize('test/example')
    current = 0
    combo = 0
    score = 0

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

    for note in range(len(NOTE_TIMES)):
        timing = int(NOTE_TIMES[note])
        position = int(NOTE_POSITIONS[note])
        if position == 1:
            notesA.add(Note(screen, note, timing, position))
        elif position == 2:
            notesB.add(Note(screen, note, timing, position))
        elif position == 3:
            notesC.add(Note(screen, note, timing, position))
        elif position == 4:
            notesD.add(Note(screen, note, timing, position))
        elif position == 5:
            notesE.add(Note(screen, note, timing, position))
        elif position == 6:
            notesF.add(Note(screen, note, timing, position))

    previousframetime = clock.get_time()
    lastplayheadposition = 0
    mostaccurate = 0

    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play()

    while True:
        current += clock.get_time()
        mostaccurate += current - previousframetime
        previousframetime = current
        songtime = pygame.mixer.music.get_pos()
        if songtime != lastplayheadposition:
            mostaccurate = (mostaccurate + songtime)/2
            lastplayheadposition = songtime

        screen.fill(BLACK)
        combo_count(combo)
        score_count(score)
        #debug_time(current, mostaccurate, previousframetime, songtime)
        #debug_key(debugkey, mostaccurate)

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

        notesA.update(keypressS, mostaccurate)
        notesB.update(keypressD, mostaccurate)
        notesC.update(keypressF, mostaccurate)
        notesD.update(keypressJ, mostaccurate)
        notesE.update(keypressK, mostaccurate)
        notesF.update(keypressL, mostaccurate)

        for note in notesA:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusa = note.difference
            if -500 <= statusa <= 500:
                combo += 1
                score += 1000
            elif statusa == -1000000:
                combo = 0

        for note in notesB:
            distances = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distances)
            statusb = note.difference
            if -500 <= statusb <= 500:
                combo += 1
                score += 1000
            elif statusb == -1000000:
                combo = 0

        for note in notesC:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusc = note.difference
            if -500 <= statusc <= 500:
                combo += 1
                score += 1000
            elif statusc == -1000000:
                combo = 0

        for note in notesD:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusd = note.difference
            if -500 <= statusd <= 500:
                combo += 1
                score += 1000
            elif statusd == -1000000:
                combo = 0

        for note in notesE:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statuse = note.difference
            if -500 <= statuse <= 500:
                combo += 1
                score += 1000
            elif statuse == -1000000:
                combo = 0

        for note in notesF:
            distance = STRUM_POSITION - (note.strum/SPEED - mostaccurate/SPEED) + VISUAL_LATENCY
            note.move(distance)
            statusf = note.difference
            if -500 <= statusf <= 500:
                combo += 1
                score += 1000
            elif statusf == -1000000:
                combo = 0

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main_menu()

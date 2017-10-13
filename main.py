import csv
import pygame

pygame.init()

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

STRUM = pygame.image.load('assets/notestrum.png')

STRUM_POSITION = 500

NOTE_TIMES = []
NOTE_POSITIONS = []

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Rhythm Game')

clock = pygame.time.Clock()
menu_clock = pygame.time.Clock()

class NoteA(pygame.sprite.Sprite):
    def __init__(self, screen, identity, strumTime):
        pygame.sprite.Sprite.__init__(self)
        self.idnum = identity
        self.strum = strumTime
        self.miss = False
        self.hit = False
        self.difference = -2000000
        self.image = pygame.image.load('assets/noteA.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(POSITION_A, -100)

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

class NoteB(pygame.sprite.Sprite):
    def __init__(self, screen, identity, strumTime):
        pygame.sprite.Sprite.__init__(self)
        self.idnum = identity
        self.strum = strumTime
        self.miss = False
        self.hit = False
        self.difference = -2000000
        self.image = pygame.image.load('assets/noteB.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(POSITION_B, -100)

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

class NoteC(pygame.sprite.Sprite):
    def __init__(self, screen, identity, strumTime):
        pygame.sprite.Sprite.__init__(self)
        self.idnum = identity
        self.strum = strumTime
        self.miss = False
        self.hit = False
        self.difference = -2000000
        self.image = pygame.image.load('assets/noteC.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(POSITION_C, -100)

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

class NoteD(pygame.sprite.Sprite):
    def __init__(self, screen, identity, strumTime):
        pygame.sprite.Sprite.__init__(self)
        self.idnum = identity
        self.strum = strumTime
        self.miss = False
        self.hit = False
        self.difference = -2000000
        self.image = pygame.image.load('assets/noteC.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(POSITION_D, -100)

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

class NoteE(pygame.sprite.Sprite):
    def __init__(self, screen, identity, strumTime):
        pygame.sprite.Sprite.__init__(self)
        self.idnum = identity
        self.strum = strumTime
        self.miss = False
        self.hit = False
        self.difference = -2000000
        self.image = pygame.image.load('assets/noteB.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(POSITION_E, -100)

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

class NoteF(pygame.sprite.Sprite):
    def __init__(self, screen, identity, strumTime):
        pygame.sprite.Sprite.__init__(self)
        self.idnum = identity
        self.strum = strumTime
        self.miss = False
        self.hit = False
        self.difference = -2000000
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
    with open(song_name + '.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            NOTE_TIMES.append(row[0])
            NOTE_POSITIONS.append(row[1])
    pygame.mixer.music.load(song_name + '.mp3')
    pygame.mixer.music.play()

def combo_count(amount):
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render(str(amount), True, WHITE)
    screen.blit(text, (20, 20))

def score_count(score_amount):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Score: " + str(score_amount), True, WHITE)
    screen.blit(text, (620, 20))

def game_loop():
    previousframetime = clock.get_time()
    lastplayheadposition = 0
    mostaccurate = 0

    initialize('miamihorror')
    current = 0
    combo = 0
    score = 0

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
            notesA.add(NoteA(screen, note, timing))
        elif position == 2:
            notesB.add(NoteB(screen, note, timing))
        elif position == 3:
            notesC.add(NoteC(screen, note, timing))
        elif position == 4:
            notesD.add(NoteD(screen, note, timing))
        elif position == 5:
            notesE.add(NoteE(screen, note, timing))
        elif position == 6:
            notesF.add(NoteF(screen, note, timing))

    while True:
        keypressS = False
        keypressD = False
        keypressF = False
        keypressJ = False
        keypressK = False
        keypressL = False

        current += clock.get_time()
        mostaccurate += current - previousframetime
        previousframetime = current
        songtime = pygame.mixer.music.get_pos()
        if songtime != lastplayheadposition:
            mostaccurate = (mostaccurate + songtime)/2
            lastplayheadposition = songtime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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

        screen.fill(BLACK)
        combo_count(combo)
        score_count(score)

        notesA.draw(screen)
        notesB.draw(screen)
        notesC.draw(screen)
        notesD.draw(screen)
        notesE.draw(screen)
        notesF.draw(screen)

        screen.blit(STRUM, (0, 0))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    game_loop()

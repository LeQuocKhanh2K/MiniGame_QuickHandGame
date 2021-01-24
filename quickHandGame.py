import pgzrun
import random

FONT_COLOR = (255, 255, 255) #màu RGB
WIDTH = 540
HEIGHT = 933
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)

START_SPEED = 10
COLORS = ["chung","bom"]
current_level = 1
final_level = 5

game_over = False
game_complete = False

subjects=[]
animations=[]

def draw():
    global subjects, game_over, game_complete, current_level
    screen.clear()
    screen.blit("bg1",(0,0))
    if game_over:
        display_message("Game Over","Press Space to play again!")
    elif game_complete:
        display_message("You Won","Press Space to play again!")
    else:
        for im in subjects:
            im.draw()

def update():
    global subjects, game_over, game_complete, current_level
    if len(subjects) == 0:
        subjects=make_subjects(current_level)
    if (game_over or game_complete) and keyboard.Space:
        subjects = []
        current_level = 1
        game_complete = False
        game_over = False

def make_subjects(number_of_subjects):
    colors_to_create=get_colors_to_create(number_of_subjects)
    new_subjects=create_subjects(colors_to_create)
    layout_subjects(new_subjects)
    animate_subjects(new_subjects)
    return new_subjects

def get_colors_to_create(number_of_subjects):
    colors_to_create=["lixi"]
    for i in range(0,number_of_subjects):
        random_color=random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_subjects(colors_to_create):
    new_subjects=[]
    for color in colors_to_create:
        subject=Actor(color + "-im")
        new_subjects.append(subject)
    return new_subjects

def layout_subjects(subjects_to_layout):
    number_of_gaps=len(subjects_to_layout) +0.1
    gap_size = WIDTH /number_of_gaps
    random.shuffle(subjects_to_layout)
    for index, subject in enumerate(subjects_to_layout):
        new_x_pos = (index+1)*gap_size
        subject.x=new_x_pos

def animate_subjects(subjects_to_animate):
    for subject in subjects_to_animate:
        duration = START_SPEED - current_level
        subject.anchor = ("center","bottom")
        animation=animate(subject, duration=duration, on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global subjects, current_level
    for subject in subjects:
        if subject.collidepoint(pos):
            if "lixi" in subject.image:
                red_subject_click()
            else:
                handle_game_over()

def red_subject_click():
    global current_level, subjects, animations, game_complete
    stop_animations(animations)
    if current_level == final_level:
        game_complete=True
    else:
        current_level=current_level+1
        subjects=[]
        animations=[]

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text,
    fontsize=30,
    center=(CENTER_X, CENTER_Y +30),
    color=FONT_COLOR)
pgzrun.go()
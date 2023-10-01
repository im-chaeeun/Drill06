from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

def handle_events():
    global running
    global mouse_x, mouse_y, mouse_num, click_mouse_x, click_mouse_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mouse_num += 1
                click_mouse_x, click_mouse_y = event.x, TUK_HEIGHT - 1 - event.y
                character_move()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def character_move():
    global frame, mouse_x, mouse_y, mouse_num, click_mouse_x, click_mouse_y, x, y, x1, y1

    if click_mouse_x == x and click_mouse_y == y:
        clear_canvas()
        # fill

    x1, y1 = x, y
    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * x1 + t * click_mouse_x
        y = (1 - t) * y1 + t * click_mouse_y

        # 이전 위치에 그려진 캐릭터를 지우기
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        mouse.clip_draw(0, 0, 50, 52, click_mouse_x, click_mouse_y)
        frame = (frame + 1) % 8
        # 캐릭터를 현재 위치에 그리기
        if click_mouse_x - x1 >= 0:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif click_mouse_x - x1 < 0:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        delay(0.01)
        update_canvas()

running = True
mouse_x, mouse_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
click_mouse_x, click_mouse_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y, x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2, TUK_WIDTH // 2, TUK_HEIGHT // 2  # 캐릭터의 좌표
frame = 0
mouse_num = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    mouse.clip_draw(0, 0, 50, 52, mouse_x, mouse_y)
    if mouse_num > 0:
        mouse.clip_draw(0, 0, 50, 52, click_mouse_x, click_mouse_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




from controller import *

pygame.init()

window = pygame.display.set_mode(SCREEN)

clock = pygame.time.Clock()

run = True
snake_pos = [WIDTH/2, HEIGHT/2]
change_pos = [0, 0]
apple = [round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK, 
            round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK]

snake_list = []
len_snake_list = 1
curr_state = STATE.MENU

start_btn = Button(100, 200, "Button\StartButton", 0.3)

while run:

    if curr_state == STATE.MENU:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill("#0B031E")
        start_btn.draw(window)
        pygame.display.update()
    
        if (start_btn.on_click()):
            curr_state = STATE.PLAYING

    elif curr_state == STATE.PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    change_pos[0] -= SNAKE_BLOCK
                    change_pos[1] = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    change_pos[0] += SNAKE_BLOCK
                    change_pos[1] = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    change_pos[0] = 0
                    change_pos[1] -= SNAKE_BLOCK
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    change_pos[0] = 0
                    change_pos[1] += SNAKE_BLOCK
                if event.key == pygame.K_q:
                    print("QUIT")
                    run = False
        
        snake_pos[0] = snake_pos[0] + change_pos[0]
        snake_pos[1] = snake_pos[1] + change_pos[1]
        
        snake_head = []
        snake_head.append(snake_pos[0])
        snake_head.append(snake_pos[1])
        snake_list.append(snake_head)

        if len(snake_list) > len_snake_list:
            del snake_list[0]
        window.fill("#0B031E")
        pygame.draw.rect(window, "Red", [apple[0], apple[1], SNAKE_BLOCK, SNAKE_BLOCK])
        draw_snake(SNAKE_BLOCK, snake_list, window)

        if snake_pos[0] == apple[0] and snake_pos[1] == apple[1]:
            apple = [round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK,
                    round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK]
            len_snake_list += 1
        
        pygame.display.update()

    clock.tick(SNAKE_SPEED)

pygame.quit()
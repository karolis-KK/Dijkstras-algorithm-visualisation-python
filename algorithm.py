import pygame
import customtkinter as ctk
import heapq
import time

# input
app = ctk.CTk()
app.geometry("325x250")
app.title("Input")
app.grid_columnconfigure((0), weight=1)

entry_start_x = ctk.CTkEntry(app, placeholder_text="Start X")
entry_start_x.grid(row=0, column=0, padx=10, pady=(20, 20), sticky="ew")

entry_start_y = ctk.CTkEntry(app, placeholder_text="Start Y")
entry_start_y.grid(row=0, column=1, padx=10, pady=(20, 20), sticky="ew")

entry_end_x = ctk.CTkEntry(app, placeholder_text="End X")
entry_end_x.grid(row=1, column=0, padx=10, pady=(20, 20), sticky="ew")

entry_end_y = ctk.CTkEntry(app, placeholder_text="End Y")
entry_end_y.grid(row=1, column=1, padx=10, pady=(20, 20), sticky="ew")

def button_event():
    global start_x, start_y, end_x, end_y

    start_x = entry_start_x.get()
    start_y = entry_start_y.get()
    end_x = entry_end_x.get()
    end_y = entry_end_y.get()

    print(f"Start X: {start_x}")
    print(f"Start Y: {start_y}")
    print(f"End X: {end_x}")
    print(f"End Y: {end_y}")

button = ctk.CTkButton(app, text="Enter", command=button_event)
button.place(relx=0.5, rely=0.8, anchor='center')

def checkbox_event():
    print(check_var.get())

check_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(app, text="Show search", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox.place(relx=0.5, rely=0.6, anchor='center')

app.mainloop()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (52, 235, 100)
CYAN = (70, 232, 235)
DARK_CYAN = (60, 149, 150)
VISITED_COLOR = (55, 76, 99)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visualiser")

fill = False
drawing = True
pygame.font.init()

def algo(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    min_heap = [(0, start, [])]
    explored = set()

    while min_heap:
        cost, current_node, path = heapq.heappop(min_heap)

        if current_node == end:
            return path + [current_node]

        if current_node in explored:
            continue

        explored.add(current_node)

        x, y = current_node
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1 and neighbor not in explored:
                new_cost = cost + 1
                new_path = path + [current_node]
                heapq.heappush(min_heap, (new_cost, neighbor, new_path))

        if check_var.get() == "on":
            time.sleep(0.1)  # delay                       --------------------------------INCREASE DELAY IF THE PROGRAM CRASHES--------------------------------
            screen.fill(BLACK)

            # grid
            for x in range(0, SCREEN_WIDTH, 25):
                pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT), 2)
            for y in range(0, SCREEN_HEIGHT, 25):
                pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y), 2)

            # coords
            for x in range(0, 600, 25):
                for y in range(0, 600, 25):
                    if x == 0 or y == 0:
                        number = (y // 25 + 1) if x == 0 else (x // 25 + 1)
                        font = pygame.font.SysFont("Arial", 18)
                        text = font.render(str(number), True, WHITE)
                        screen.blit(text, (x + 5, y + 5))

            # filled cells
            for x in range(0, SCREEN_WIDTH, 25):
                for y in range(0, SCREEN_HEIGHT, 25):
                    if grid[x // 25][y // 25] == 1:
                        pygame.draw.rect(screen, WHITE, (x, y, 25, 25))

            # explored cells
            for node in explored:
                x, y = node
                pygame.draw.rect(screen, VISITED_COLOR, (x * 25, y * 25, 25, 25))

            pygame.display.update()

    return []

grid = [[0] * 24 for w in range(24)]

shortest_path_nodes = []

# game loop
running = True

while running:
    starting_x = int(start_x) - 1
    starting_y = int(start_y) - 1
    ending_x = int(end_x) - 1
    ending_y = int(end_y) - 1
    actual_start_x = starting_x * 25
    actual_start_y = starting_y * 25
    actual_end_x = ending_x * 25
    actual_end_y = ending_y * 25

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if drawing:
                    fill = True
        elif event.type == pygame.MOUSEMOTION:
            if fill:
                x, y = event.pos
                grid[x // 25][y // 25] = 1
                pygame.draw.rect(screen, WHITE, (x // 25 * 25, y // 25 * 25, 25, 25))
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                fill = False
                drawing = False

    screen.fill(BLACK)

    # grid
    for x in range(0, SCREEN_WIDTH, 25):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT), 2)
    for y in range(0, SCREEN_HEIGHT, 25):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y), 2)

    # coords
    for x in range(0, 600, 25):
        for y in range(0, 600, 25):
            if x == 0 or y == 0:
                number = (y // 25 + 1) if x == 0 else (x // 25 + 1)
                font = pygame.font.SysFont("Arial", 18)
                text = font.render(str(number), True, WHITE)
                screen.blit(text, (x + 5, y + 5))

    # filled cells
    for x in range(0, SCREEN_WIDTH, 25):
        for y in range(0, SCREEN_HEIGHT, 25):
            if grid[x // 25][y // 25] == 1:
                pygame.draw.rect(screen, WHITE, (x, y, 25, 25))

    # shortest path
    for node in shortest_path_nodes:
        x, y = node
        pygame.draw.rect(screen, CYAN, (x * 25, y * 25, 25, 25))
        
    pygame.draw.rect(screen, GREEN, (actual_start_x, actual_start_y, 25, 25))  # start
    pygame.draw.rect(screen, DARK_CYAN, (actual_end_x, actual_end_y, 25, 25))  # end

    pygame.display.update()

    if not drawing:
        start_time = time.time()
        shortest_path_nodes = algo(grid, (starting_x, starting_y), (ending_x, ending_y))
        end_time = time.time()
        run_time = end_time - start_time
        print(run_time)
        drawing = True

pygame.quit()
import pygame

pygame.init()

WIDTH, HEIGHT = 900, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

current_color = BLUE
tool = "brush"
radius = 10
drawing = False
start_pos = None

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)


def draw_text(text, x, y):
    """Function to display text on the screen."""
    font = pygame.font.SysFont("Arial", 18)
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))


def draw_square(start, end, color):
    """Draw a square based on two corner points."""
    side_length = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], side_length, side_length)
    pygame.draw.rect(canvas, color, rect, 2)


def draw_right_triangle(start, end, color):
    """Draw a right triangle using two points (forming the base and height)."""
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x2, y1), (x1, y2)]  # right-angle triangle
    pygame.draw.polygon(canvas, color, points, 2)


def draw_equilateral_triangle(start, end, color):
    """Draw an equilateral triangle."""
    x1, y1 = start
    x2, y2 = end
    side_length = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    
    # Calculate the height of the equilateral triangle
    height = (side_length * (3 ** 0.5)) / 2

    # Points of the equilateral triangle
    points = [
        (x1, y1),
        (x2, y2),
        (x1 + side_length // 2, y1 - height)
    ]
    pygame.draw.polygon(canvas, color, points, 2)


def draw_rhombus(start, end, color):
    """Draw a rhombus using two diagonal points."""
    x1, y1 = start
    x2, y2 = end
    
    # Calculate the mid-point of the diagonal and define the rhombus' points
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    points = [
        (x1, center_y),  # top left
        (center_x, y1),  # top right
        (x2, center_y),  # bottom right
        (center_x, y2)   # bottom left
    ]
    pygame.draw.polygon(canvas, color, points, 2)


running = True

while running:
    screen.blit(canvas, (0, 0))

    # Display instructions
    draw_text("Keys: B Brush | R Rectangle | C Circle | E Eraser | S Square | T Triangle | Q Equilateral | H Rhombus", 10, 10)
    draw_text("Colors: 1 Red | 2 Green | 3 Blue | 4 Black", 10, 35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Tools
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_s:  # New: Square tool
                tool = "square"
            elif event.key == pygame.K_t:  # New: Right triangle tool
                tool = "right_triangle"
            elif event.key == pygame.K_q:  # New: Equilateral triangle tool
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:  # New: Rhombus tool
                tool = "rhombus"

            # Colors
            elif event.key == pygame.K_1:
                current_color = RED
            elif event.key == pygame.K_2:
                current_color = GREEN
            elif event.key == pygame.K_3:
                current_color = BLUE
            elif event.key == pygame.K_4:
                current_color = BLACK

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos

            elif event.button == 4:
                radius += 1

            elif event.button == 5:
                radius = max(1, radius - 1)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                # Tool-based drawing
                if tool == "rectangle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(
                        min(x1, x2),
                        min(y1, y2),
                        abs(x2 - x1),
                        abs(y2 - y1)
                    )
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    circle_radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, circle_radius, 2)

                elif tool == "square":
                    draw_square(start_pos, end_pos, current_color)  # Draw square

                elif tool == "right_triangle":
                    draw_right_triangle(start_pos, end_pos, current_color)  # Draw right triangle

                elif tool == "equilateral_triangle":
                    draw_equilateral_triangle(start_pos, end_pos, current_color)  # Draw equilateral triangle

                elif tool == "rhombus":
                    draw_rhombus(start_pos, end_pos, current_color)  # Draw rhombus

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "brush":
                    pygame.draw.circle(canvas, current_color, event.pos, radius)

                elif tool == "eraser":
                    pygame.draw.circle(canvas, WHITE, event.pos, radius)

    # Preview shape while dragging (only for specific shapes)
    if drawing and tool in ["rectangle", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"]:
        mouse_pos = pygame.mouse.get_pos()

        if tool == "rectangle":
            x1, y1 = start_pos
            x2, y2 = mouse_pos
            rect = pygame.Rect(
                min(x1, x2),
                min(y1, y2),
                abs(x2 - x1),
                abs(y2 - y1)
            )
            pygame.draw.rect(screen, current_color, rect, 2)

        elif tool == "circle":
            x1, y1 = start_pos
            x2, y2 = mouse_pos
            circle_radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
            pygame.draw.circle(screen, current_color, start_pos, circle_radius, 2)

        elif tool == "square":
            draw_square(start_pos, mouse_pos, current_color)  # Preview square

        elif tool == "right_triangle":
            draw_right_triangle(start_pos, mouse_pos, current_color)  # Preview right triangle

        elif tool == "equilateral_triangle":
            draw_equilateral_triangle(start_pos, mouse_pos, current_color)  # Preview equilateral triangle

        elif tool == "rhombus":
            draw_rhombus(start_pos, mouse_pos, current_color)  # Preview rhombus

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import sys
import pygame as pg

pg.init()
clock = pg.time.Clock()
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)

# Initialize background
screen     = pg.display.set_mode((640, 480))
BACKGROUND = pg.Color(127, 127, 127)
screen.fill(BACKGROUND)

# Initialize FPS stuff
fps_font    = pg.font.SysFont((), 64)
fps_surface = pg.Surface((0,0))
FPS_EVENT   = pg.event.custom_type()
pg.time.set_timer(pg.event.Event(FPS_EVENT, {}), 256)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == FPS_EVENT:

            # Erase fps counter
            screen.fill(BACKGROUND, fps_surface.get_rect())

            # Render fps counter
            fps_surface = fps_font.render(clock.get_fps().__int__().__str__(),
                                          False,
                                          WHITE,
                                          BLACK)

            screen.blit(fps_surface, (0,0))
            
    clock.tick(60)
    pg.display.update()

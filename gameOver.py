import pygame_gui
import pygame
import pygame_gui
import pygame_widgets as pw

class GameOverLogic:
    def __init__(self, manager, on_restart, on_quit):
        pygame.init()
        self.manager = manager
        self.on_restart = on_restart
        self.on_quit = on_quit
        self.display_game_over = False
        self.create_game_over_window()

    def create_game_over_window(self):
        self.game_over_window = pygame_gui.elements.UIWindow(
            pygame.Rect((100, 100), (400, 200)),
            self.manager,
            window_display_title="Game Over",
            object_id="#game_over_window"
        )

        restart_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 100), (100, 50)),
            text="Restart",
            manager=self.manager,
            container=self.game_over_window
        )

        quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((250, 100), (100, 50)),
            text="Quit",
            manager=self.manager,
            container=self.game_over_window
        )

        # restart_button.subscribe(self.handle_restart_button)
        # quit_button.subscribe(self.handle_quit_button)

    def handle_restart_button(self, event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            self.on_restart()

    def handle_quit_button(self, event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            self.on_quit()

def restart():
    print("erestart")
def quit():
    print("quit")
GameOverLogic(restart, quit)
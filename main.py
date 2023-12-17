# import pygame
import sys
from scenes.scene2 import *
from cripto import MessageEncryptionApp
from scenes.scene1 import *
from app import App
from scenes.halfscene import InterScene
from scenes.homescreen import HomeScreen
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.hardness = 1
        self.username = "martin"
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager("homescreen")
        self.intro = IntroScene(self.screen, self.gameStateManager)
        self.homescreen = HomeScreen(self.screen, self.gameStateManager)
        self.scene2 = EncryptionScene(self.screen, self.gameStateManager)
        self.halfscene = InterScene(self.screen, self.gameStateManager)
        self.states = {
            "intro": self.intro,
            "scene2": self.scene2,
            "halfScene": self.halfscene,
            "homescreen": self.homescreen
        }
        self.current_scene = self.states[self.gameStateManager.getState()]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            current_state = self.gameStateManager.getState()
            if current_state == "halfScene" and not hasattr(self, 'game'):

                with open("data/data1.txt", "r") as file:
                    self.hardness = int(file.read())
                self.plain_text = self.get_random_cryptography_message()
                
                
                
                self.enc_instance = MessageEncryptionApp(self.intro.password)
                self.enc_message =self.enc_instance.encrypt_message(self.plain_text)

                self.game = App(self.screen, self.gameStateManager, self.intro.username, self.enc_message,self.hardness,self.enc_instance)
                self.states["game"] = self.game
            self.states[current_state].run()
            pygame.display.update()
            self.clock.tick(FPS)
    import random

    def get_random_cryptography_message(self):
        cryptography_messages = [
            "Encrypt your ambitions with determination; decryption reveals success.",
            "Life's algorithm: iterate, adapt, overcome.",
            "Code your destiny with bytes of resilience and passion.",
            "Debugging life: turning setbacks into breakthroughs.",
            "Success: a compilation of compiled efforts.",
            "Master the code of silence; let success be the noise.",
            "Compile dreams, execute goals, and debug obstacles.",
            "Navigate the binary seas of challenges with a byte-sized ship of courage.",
            "Crack the code of happiness, one positive bit at a time.",
            "In the coding of life, perseverance is the syntax of success.",
            "Adapt to change; it's the only constant in the algorithm of life.",
            "Life's encryption key: positive mindset, resilience, and relentless effort.",
            "Dance with bugs, embrace glitches, and code your way to success.",
            "Decrypt negativity; encrypt positivity into your life's source code.",
            "Life's API: Acceptance, Patience, and Initiative.",
            "Optimize your life's code for efficiency and fulfillment.",
            "In the matrix of challenges, become the architect of your success.",
            "Life's protocol: innovate, iterate, and elevate.",
            "Debugging the code of life: find joy in the unexpected exceptions.",
            "Compile a life of purpose, run it with passion, and debug with wisdom."
        ]
        
        return random.choice(cryptography_messages)




class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def getState(self):
        return self.currentState

    def setState(self, currentState):
        self.currentState = currentState


if __name__ == "__main__":
    Game().run()

# import pygame
# import os
# from cryptography.fernet import Fernet

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 400, 200
# WHITE = (255, 255, 255)
# FONT_SIZE = 18

# # Create a window
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Decrypt Message")

# # Font
# font = pygame.font.Font(None, FONT_SIZE)

# # Message
# message = ""
# decrypted_message = ""

# # Fernet key for decryption
# # Replace with your actual key
# key = b'your_secret_key_here'

# # Decrypt function
# def decrypt_message(key, encrypted_message):
#     fernet = Fernet(key)
#     decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
#     return decrypted_message

# # Main loop
# running = True
# while running:
#     window.fill(WHITE)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 decrypted_message = decrypt_message(key, message)
#         if event.type == pygame.TEXTINPUT:
#             message += event.text
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 message = message[:-1]

#     # Create labels
#     label = font.render("Hello Martin\nPaste in your private key", True, (0, 0, 0))
#     submit_label = font.render("This is your decrypted message:", True, (0, 0, 0))
#     message_label = font.render(message, True, (0, 0, 0))
#     decrypted_message_label = font.render(decrypted_message, True, (0, 0, 0))

#     # Blit labels to the screen
#     window.blit(label, (WIDTH // 2 - label.get_width() // 2, 10))
#     window.blit(submit_label, (WIDTH // 2 - submit_label.get_width() // 2, 70))
#     window.blit(message_label, (WIDTH // 2 - message_label.get_width() // 2, 100))
#     window.blit(decrypted_message_label, (WIDTH // 2 - decrypted_message_label.get_width() // 2, 130))

#     pygame.display.update()

# pygame.quit()

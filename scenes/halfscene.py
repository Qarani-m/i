import time

class InterScene:
	def __init__(self, screen, gameStateManager):
		time.sleep(0.5)
		self.gameStateManager = gameStateManager
	def run(self):

		self.gameStateManager.setState("game")
			


import tkinter as tk
from tkinter import messagebox  # Use messagebox instead of simpledialog
from cryptography.hazmat.primitives import serialization
import hashlib

class CustomDialog:
    def __init__(self, private_key):
        self.private_key = private_key
        self.message = "Here is your hashed private key:"
        # self.hashed_key = self.hash_private_key()

    def show_dialog(self):
        result = messagebox.showinfo("Hashed Private Key", f"{self.message}\n\n Key goes here")
        return result

# Example usage:
if __name__ == "__main__":
    # Replace the following line with your actual private key instance
    example_private_key = None
    dialog = CustomDialog(example_private_key)
    dialog.show_dialog()

import tkinter as tk
from datetime import datetime
import random

class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple ChatBot")
        self.root.geometry("400x500")
        
        # Chat display area (Text widget)
        self.chat_display = tk.Text(root, bd=1, bg="white", width=50, height=15)
        self.chat_display.place(x=6, y=6, height=400, width=388)
        self.chat_display.config(state=tk.DISABLED)  # Make it read-only
        
        # User input field
        self.user_input = tk.Entry(root, width=40)
        self.user_input.place(x=6, y=420, height=30, width=320)
        self.user_input.bind("<Return>", self.send_message)  # Press Enter to send
        
        # Send button
        self.send_button = tk.Button(root, text="Send", width=10, command=self.send_message)
        self.send_button.place(x=330, y=420, height=30, width=60)
        
        # Greet the user
        self.bot_response("Bot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        
        # Display user message
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"You: {user_text}\n")
        self.chat_display.config(state=tk.DISABLED)
        self.user_input.delete(0, tk.END)  # Clear input field
        
        # Generate bot response
        bot_reply = self.generate_response(user_text.lower())
        self.bot_response(f"Bot: {bot_reply}")
        
        # Exit if user says 'bye'
        if user_text.lower() == "bye":
            self.root.after(1000, self.root.destroy)  # Close window after 1 second
    
    def bot_response(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)  # Auto-scroll to latest message
    
    def generate_response(self, user_input):
        if "hello" in user_input or "hi" in user_input:
            return random.choice(["Hello!", "Hi there!", "Hey!"])
        
        elif "how are you" in user_input:
            return "I'm just a bot, but I'm functioning well!"
        
        elif "your name" in user_input:
            return "I'm SimpleBot, your friendly chatbot."
        
        elif "time" in user_input:
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
        
        elif "date" in user_input:
            return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
        
        elif "joke" in user_input:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ]
            return random.choice(jokes)
        
        elif "thank" in user_input:
            return "You're welcome!"
        
        elif "bye" in user_input:
            return "Goodbye! Have a great day."
        
        else:
            return "I didn't understand that. Try asking about time, date, or a joke!"

# Create and run the GUI
root = tk.Tk()
chatbot = ChatBotGUI(root)
root.mainloop()
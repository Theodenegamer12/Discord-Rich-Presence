import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QIcon
import webbrowser
from pypresence import Presence
import json

is_running = False
RPC = None  

def load_data():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data():
    data = {
        "client_id": entry_client_id.text(),
        "state": entry_state.text(),
        "details": entry_details.text(),
        "large_image": entry_large_image.text(),
        "small_image": entry_small_image.text(),
        "large_text": entry_large_text.text(),
        "small_text": entry_small_text.text()
    }
    with open("config.json", "w") as f:
        json.dump(data, f)

def toggle_rich_presence():
    global is_running, RPC
    if is_running:
        button_start_stop.setText("Start")
        label_result.setText("Rich Presence update stopped")
        label_result.setStyleSheet("color: red; font-weight: bold;")
        is_running = False
        if RPC:
            RPC.close()  
            RPC = None
    else:
        button_start_stop.setText("Stop")
        label_result.setText("Updating Rich Presence...")
        label_result.setStyleSheet("color: green; font-weight: bold;")
        is_running = True
        start_rich_presence()

def start_rich_presence():
    global RPC
    if is_running:
        update_rich_presence()
        QTimer.singleShot(15000, start_rich_presence)  

def update_rich_presence():
    global RPC
    print("Updating Rich Presence...")
    state = entry_state.text()
    details = entry_details.text()
    large_image = entry_large_image.text()
    small_image = entry_small_image.text()
    large_text = entry_large_text.text()
    small_text = entry_small_text.text()

    client_id = entry_client_id.text()
    if not client_id:
        label_result.setText("Client ID is required!")
        label_result.setStyleSheet("color: red; font-weight: bold;")
        return

    if not RPC:
        RPC = Presence(client_id)
        RPC.connect()

    try:
        RPC.update(
            state=state,               
            details=details,           
            large_image=large_image,   
            large_text=large_text,     
            small_image=small_image,   
            small_text=small_text     
        )
        label_result.setText("Rich Presence updated!")
        label_result.setStyleSheet("color: green; font-weight: bold;")
    except Exception as e:
        label_result.setText(f"Error updating: {e}")
        label_result.setStyleSheet("color: red; font-weight: bold;")

def show_tutorial():
    print("Displaying tutorial...")
    tutorial_dialog = QMessageBox(window)
    tutorial_dialog.setWindowTitle("Tutorial - Discord Rich Presence")
    tutorial_dialog.setText(
        "1. Go to the Discord Developer Portal.\n\n"
        "2. Create a new application or use an existing one.\n\n"
        "3. In the application, go to the 'Rich Presence' section.\n\n"
        "4. Upload your images in 'Images' and give them names.\n\n"
        "5. Copy the application ID and replace it in this script.\n\n"
        "6. Customize your Rich Presence here and update it!"
    )
    tutorial_dialog.setIcon(QMessageBox.Information)
    tutorial_dialog.exec_()

def open_discord_developer_portal():
    print("Opening Discord Developer Portal...")
    webbrowser.open("https://discord.com/developers/applications", new=2)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Discord Rich Presence Setup")
window.setFixedSize(500, 500)
window.setStyleSheet("background-color: #f0f0f0; font-family: Arial, sans-serif;")

# Set the icon for the window in the taskbar
window.setWindowIcon(QIcon("icons/Discord-Rich-Presence_icon.png"))

layout = QVBoxLayout()

data = load_data()

layout.addWidget(QLabel("Enter your Discord application's Client ID"))
entry_client_id = QLineEdit(data.get("client_id", ""))
layout.addWidget(entry_client_id)

layout.addWidget(QLabel("State (text under the name)"))
entry_state = QLineEdit(data.get("state", ""))
layout.addWidget(entry_state)

layout.addWidget(QLabel("Details (main text)"))
entry_details = QLineEdit(data.get("details", ""))
layout.addWidget(entry_details)

layout.addWidget(QLabel("Large Image (main image name)"))
entry_large_image = QLineEdit(data.get("large_image", ""))
layout.addWidget(entry_large_image)

layout.addWidget(QLabel("Small Image (secondary image name)"))
entry_small_image = QLineEdit(data.get("small_image", ""))
layout.addWidget(entry_small_image)

layout.addWidget(QLabel("Large Text (text for main image)"))
entry_large_text = QLineEdit(data.get("large_text", ""))
layout.addWidget(entry_large_text)

layout.addWidget(QLabel("Small Text (text for secondary image)"))
entry_small_text = QLineEdit(data.get("small_text", ""))
layout.addWidget(entry_small_text)

button_start_stop = QPushButton("Start")
button_start_stop.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px;")
button_start_stop.clicked.connect(toggle_rich_presence)
layout.addWidget(button_start_stop)

button_update = QPushButton("Update Rich Presence")
button_update.setStyleSheet("background-color: #FF6347; color: white; border-radius: 5px; padding: 10px;")
button_update.clicked.connect(update_rich_presence)
layout.addWidget(button_update)

label_result = QLabel("")
layout.addWidget(label_result)

button_layout = QHBoxLayout()

button_tutorial = QPushButton("Tutorial")
button_tutorial.setStyleSheet("background-color: #FF6347; color: white; border-radius: 5px; padding: 10px;")
button_tutorial.clicked.connect(show_tutorial)
button_layout.addWidget(button_tutorial)

button_open_portal = QPushButton("Open Discord Developer Portal")
button_open_portal.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px; padding: 10px;")
button_open_portal.clicked.connect(open_discord_developer_portal)
button_layout.addWidget(button_open_portal)

youtube_icon_path = "icons/youtube_icon.png"
github_icon_path = "icons/github_icon.png"
linktree_icon_path = "icons/linktree_icon.png"

icon_youtube = QIcon(youtube_icon_path)
icon_github = QIcon(github_icon_path)
icon_linktree = QIcon(linktree_icon_path)

button_youtube = QPushButton()
button_youtube.setIcon(icon_youtube)
button_youtube.setIconSize(QSize(32, 32))
button_youtube.setFlat(True)  
button_youtube.clicked.connect(lambda: webbrowser.open("https://www.youtube.com/@theodenegamer1263"))

button_github = QPushButton()
button_github.setIcon(icon_github)
button_github.setIconSize(QSize(32, 32))
button_github.setFlat(True)
button_github.clicked.connect(lambda: webbrowser.open("https://github.com/Theodenegamer12"))

button_linktree = QPushButton()
button_linktree.setIcon(icon_linktree)
button_linktree.setIconSize(QSize(32, 32))
button_linktree.setFlat(True)
button_linktree.clicked.connect(lambda: webbrowser.open("https://linktr.ee/theodenegamer12"))

button_layout.addWidget(button_youtube)
button_layout.addWidget(button_github)
button_layout.addWidget(button_linktree)

layout.addLayout(button_layout)

def close_event(event):
    save_data()
    event.accept()

window.closeEvent = close_event

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

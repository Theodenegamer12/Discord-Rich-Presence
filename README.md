# Discord Rich Presence Setup Application

This application allows you to set up and manage Discord Rich Presence for your application or game. It provides a graphical user interface (GUI) built using **PyQt5** that allows you to input various data for customizing the Rich Presence.

![image](https://github.com/user-attachments/assets/780ea96f-5e0b-4b55-9695-6ab5684de63c)

## Features

- **Start/Stop Rich Presence**: Allows you to start and stop the updating of your Discord Rich Presence.
- **Real-Time Rich Presence Updates**: Updates your Discord status in real-time based on the information you provide.
- **Customizable Fields**: Customize various fields such as:
  - Client ID (required)
  - State (the text that appears under the username)
  - Details (the main text displayed in the Rich Presence)
  - Large and Small Image (displayed images in your Rich Presence)
  - Large and Small Text (associated text with the images)
- **Auto-Save Configuration**: The app will save your configuration to a `config.json` file for easy reuse.
- **Tutorial**: Access a detailed tutorial that guides you through the process of setting up your Discord Developer Portal application for Rich Presence.
- **Quick Access to Discord Developer Portal**: Directly open the Discord Developer Portal to manage your application.
- **Custom Buttons**: Includes buttons for direct links to external resources like YouTube, GitHub, and Linktree.

## Dependencies

- **PyQt5**: Python bindings for Qt5, used for building the GUI.
- **pypresence**: A Python library for interacting with Discord's Rich Presence API.

You can install these dependencies using `pip`:

```bash
pip install PyQt5 pypresence
```
## Code Overview
Loading and Saving Configuration:

The application loads and saves the configuration to a config.json file. This file contains all the parameters for the Discord Rich Presence setup.
GUI Components:

Various input fields (QLineEdit) are used to gather user input such as Client ID, state, details, images, and associated text.
The GUI is composed using a QVBoxLayout for vertical stacking of widgets and a QHBoxLayout for horizontal button placement.
Rich Presence Update:

The Rich Presence status is updated by calling the update_rich_presence function, which uses the pypresence library to communicate with Discord’s API. The status updates every 15 seconds once started.
If the "Start" button is pressed, the program connects to Discord using the provided Client ID and updates the status. If it’s already running, it stops the updates and disconnects.
Tutorial and External Links:

A tutorial is available that provides detailed steps on how to set up Discord Rich Presence from the Discord Developer Portal.
Direct links to the Discord Developer Portal, YouTube, GitHub, and Linktree are available for easy access via clickable buttons.
Error Handling:

Basic error handling is implemented to ensure that the Client ID is entered correctly and that the Rich Presence update does not fail silently.
Icons:

Custom icons are used for the buttons that open external links. These icons should be stored in the icons directory in the same folder as the script.
How to Use
Open the Application: Run the script using Python. A window will appear with the following fields:

Client ID: Your Discord application’s client ID.
State: The state text to display (e.g., “Playing a game”).
Details: The main details text for the Rich Presence.
Large Image: The name of the image for the large display.
Small Image: The name of the image for the small display.
Large Text: Text associated with the large image.
Small Text: Text associated with the small image.
Start/Stop Rich Presence: Click the "Start" button to begin updating your Rich Presence. The application will automatically update your status on Discord. Press "Stop" to end the updates.

Saving Your Configuration: When you close the application, your settings will be automatically saved to the config.json file for future use.

Accessing the Tutorial: Click the "Tutorial" button to view the step-by-step guide on setting up your Discord application for Rich Presence.

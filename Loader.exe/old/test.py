import winreg
import os

def set_terminal_background_image(image_path):
    # Registry key for Windows Terminal settings
    registry_key = r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Terminal Server'

    # Construct the full path for the settings file
    settings_path = os.path.expandvars(os.path.join('%LOCALAPPDATA%', 'Packages', 'Microsoft.WindowsTerminal_8wekyb3d8bbwe', 'LocalState', 'settings.json'))

    # Create or open the registry key
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_key, 0, winreg.KEY_SET_VALUE)
    except FileNotFoundError:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, registry_key)

    # Set the background image in the settings file
    try:
        with open(settings_path, 'r') as file:
            settings_content = file.read()

        # Modify the settings content to include the background image path
        background_setting = f'"backgroundImage": "{image_path}"'
        if background_setting not in settings_content:
            settings_content = settings_content.replace('"profiles": [', f'{background_setting},\n    "profiles": [')

        with open(settings_path, 'w') as file:
            file.write(settings_content)

    except Exception as e:
        print(f"Error modifying settings file: {e}")

    finally:
        winreg.CloseKey(key)

if __name__ == "__main__":
    # Provide the path to your background image
    background_image_path = r'C:\path\to\your\background_image.jpg'

    set_terminal_background_image(background_image_path)

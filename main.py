import webbrowser
import subprocess
import datetime
import json

def tell_time():
    now = datetime.datetime.now()
    print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def open_webpage():
    url = input("Enter the URL of the webpage you want to open: ")
    webbrowser.open(url)
    print("Opening webpage:", url)

def system_status():
    status = subprocess.run(["uptime"], capture_output=True, text=True)
    print("System status:", status.stdout.strip())

def save_personal_info(info):
    with open('personal_info.json', 'w') as f:
        json.dump(info, f, indent=4)
        print("Personal information saved.")

def load_personal_info():
    try:
        with open('personal_info.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    personal_info = load_personal_info()
    if personal_info:
        print(f"Welcome back, {personal_info.get('name')}!")
    else:
        print("Welcome to BonziLinux, your friendly assistant!")
        name = input("What's your name? ")
        pronouns = input("What are your pronouns? ")
        personal_info = {'name': name, 'pronouns': pronouns}
        save_personal_info(personal_info)
    
    while True:
        print("\nWhat can I do for you?")
        print("1. Tell the time")
        print("2. Open a webpage")
        print("3. Show system status")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            tell_time()
        elif choice == '2':
            open_webpage()
        elif choice == '3':
            system_status()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

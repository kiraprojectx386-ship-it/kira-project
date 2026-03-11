import os, sys, time, socket, platform

# --- MASTER CONFIG: 30 KEYS ---
VALID_KEYS = [
    "KIRA-9910", "KIRA-2234", "KIRA-7761", "KIRA-4452", "KIRA-1092",
    "KIRA-8823", "KIRA-3341", "KIRA-5567", "KIRA-1120", "KIRA-4498",
    "KIRA-7712", "KIRA-9903", "KIRA-2287", "KIRA-6654", "KIRA-3311",
    "KIRA-5540", "KIRA-8876", "KIRA-2201", "KIRA-4432", "KIRA-1199",
    "KIRA-7788", "KIRA-6633", "KIRA-5522", "KIRA-4411", "KIRA-3300",
    "KIRA-2211", "KIRA-1144", "KIRA-9988", "KIRA-8855", "KIRA-7744"
]

PC_NAME = platform.node() if platform.node() != "localhost" else socket.gethostname()

# Hidden paths for Windows AppData
LOG_PATH = os.path.join(os.getenv('APPDATA', os.getcwd()), "win_system_xz.dat")
USED_KEYS_PATH = os.path.join(os.getenv('APPDATA', os.getcwd()), "win_archive_xz.dat")

def get_count():
    if not os.path.exists(LOG_PATH): return 0
    try:
        with open(LOG_PATH, "r") as f: return int(f.read())
    except: return 0

def update_count(reset=False):
    count = 0 if reset else get_count() + 1
    with open(LOG_PATH, "w") as f: f.write(str(count))

def get_used_keys():
    if not os.path.exists(USED_KEYS_PATH): return []
    try:
        with open(USED_KEYS_PATH, "r") as f: return f.read().splitlines()
    except: return []

def mark_key_as_used(key):
    with open(USED_KEYS_PATH, "a") as f: f.write(key + "\n")

def lock_screen():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n ===========================================")
        print(" [!] CREDITS EXPIRED. SYSTEM LOCKED.")
        print(f" [!] DEVICE ID: {PC_NAME}")
        print(" ===========================================")
        user_key = input(" ENTER ACTIVATION KEY: ").strip()
        
        used_keys = get_used_keys()

        if user_key in used_keys:
            print("\n [X] ERROR: KEY ALREADY USED!")
            time.sleep(3)
        elif user_key in VALID_KEYS:
            mark_key_as_used(user_key)
            update_count(reset=True)
            print("\n [+] VALID KEY! SYSTEM UNLOCKED.")
            time.sleep(2)
            break
        else:
            print("\n [!] INVALID KEY. ACCESS DENIED.")
            time.sleep(2)

def main():
    while True:
        count = get_count()
        if count >= 3:
            lock_screen()
            continue

        os.system("cls" if os.name == "nt" else "clear")
        print(" ===========================================")
        print("          KIRA-FRPXZ  SYSTEM")
        print(f" DEVICE: {PC_NAME} | TRIALS: {count}/3")
        print(" ===========================================")
        print(" [1] START FRP BYPASS")
        print(" [2] CHECK DEVICE (ADB)")
        print(" [0] EXIT")
        
        choice = input("\n SELECT OPTION > ")
        
        if choice == "1":
            print("\n [*] INITIALIZING...")
            time.sleep(2)
            update_count()
            print(" [+] SUCCESS: OPERATION COMPLETE.")
            input("\n Press Enter to continue...")
        elif choice == "2":
            os.system("adb devices")
            input("\n Press Enter...")
        elif choice == "0":
            break

if __name__ == "__main__":
    main()

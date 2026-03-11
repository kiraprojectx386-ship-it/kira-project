import os, sys, time, socket, platform

VALID_KEYS = ["KIRA-9910", "KIRA-2234", "KIRA-7761", "KIRA-4452", "KIRA-1092"]
PC_NAME = platform.node()

def lock_screen():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n ===========================================")
        print(" [!] CREDITS EXPIRED. SYSTEM LOCKED.")
        print(f" [!] DEVICE ID: {PC_NAME}")
        print(" ===========================================")
        user_key = input(" ENTER ACTIVATION KEY: ").strip()
        if user_key in VALID_KEYS:
            print("\n [+] VALID KEY! SYSTEM UNLOCKED.")
            time.sleep(2)
            break
        else:
            print("\n [!] INVALID KEY. ACCESS DENIED.")
            time.sleep(2)

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(" ===========================================")
        print("          KIRA-FRPXZ  SYSTEM")
        print(f" DEVICE: {PC_NAME}")
        print(" ===========================================")
        print(" [1] START FRP BYPASS")
        print(" [2] CHECK DEVICE (ADB)")
        print(" [0] EXIT")
        choice = input("\n SELECT OPTION > ")
        if choice == "1":
            print("\n [*] INITIALIZING...")
            time.sleep(2)
            print(" [+] SUCCESS: OPERATION COMPLETE.")
            input("\n Press Enter...")
        elif choice == "2":
            os.system("adb devices")
            input("\n Press Enter...")
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
      

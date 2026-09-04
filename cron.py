import time
import login

print("⏰ TEST MODE — running login.auto_login() every 3 minutes...")

while True:
    print(f"🚀 Triggering login ...")
    try:
        login.auto_login()
    except Exception as e:
        print(f"❌ auto_login failed: {e}")
    time.sleep(180)  # 3 minutes

import psutil
import datetime

def convert_bytes(size_in_bytes):
    factor = 1024
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < factor:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= factor

def run_health_check():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 50)
    print(f"🛡️  LINUX HEALTH GUARD REPORT | {now}")
    print("=" * 50)
    # 1. ניטור מעבד (CPU)
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"💻 CPU Usage:    [{cpu_usage}%]")
    # 2. ניטור זיכרון (RAM)
    mem = psutil.virtual_memory()
    print(f"🧠 RAM Usage:    [{mem.percent}%] ({convert_bytes(mem.used)} / {convert_bytes(mem.total)})")
    # 3. ניטור דיסק קשיח (Disk)
    disk = psutil.disk_usage('/')
    print(f"💾 Disk Usage:   [{disk.percent}%] ({convert_bytes(disk.used)} / {convert_bytes(disk.total)})")
    print("-" * 50)
    # 4. בדיקת התראות
    if cpu_usage > 80 or mem.percent > 80 or disk.percent > 90:
        print("⚠️  STATUS: WARNING - High resource usage detected!")
    else:
        print("✅ STATUS: System health is Normal.")
    print("=" * 50)

if __name__ == "__main__":
    run_health_check()

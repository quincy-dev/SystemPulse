import platform
import psutil
import speedtest
import time
import random
import os
import pyfiglet  # Untuk membuat ASCII art
from colorama import init, Fore, Style  # Untuk warna terminal

# Inisialisasi colorama
init(autoreset=True)


def get_rgb_color():
    """Menghasilkan warna RGB secara acak."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'\033[38;2;{r};{g};{b}m'


def loading_animation_tool(tool_name, duration):
    print(f"\nMemuat {tool_name}...")
    for i in range(1, 101):
        time.sleep(duration / 100)  # Simulasi durasi loading
        bar = "#" * (i // 2)  # 50 karakter maksimal
        color = get_rgb_color()  # Warna RGB acak
        print(f"\r{color}[{bar:<50}] {i}%", end="")
    print(Style.RESET_ALL + "\n")  # Reset warna


def display_header():
    os.system("clear" if os.name == "posix" else "cls")
    ascii_banner = pyfiglet.figlet_format("Quincy Dev Tool")
    print(Fore.CYAN + ascii_banner)
    print("=" * 50)
    print(Fore.YELLOW + "Tool Multifungsi oleh Quincy Dev".center(50))
    print(Fore.GREEN + "Selamat datang di tool multifungsi sederhana ini!")
    print("Saya Quincy Dev, dan saya harap skrip ini dapat membantu")
    print("Anda mengenal perangkat Anda lebih baik. Selamat mencoba!")
    print("=" * 50 + Style.RESET_ALL)


def cek_device():
    loading_animation_tool("Pemeriksaan Device", 3)
    print("\n=== Informasi Device ===")
    os_info = f"{platform.system()} {platform.release()}"
    device_name = platform.node()
    architecture = platform.architecture()[0]
    processor = platform.processor()

    print(f"{'Sistem Operasi:':<20} {os_info}")
    print(f"{'Nama Device:':<20} {device_name}")
    print(f"{'Arsitektur:':<20} {architecture}")
    print(f"{'Prosesor:':<20} {processor}")
    
    return {
        "os_info": os_info,
        "device_name": device_name,
        "architecture": architecture,
        "processor": processor
    }


def cek_kecepatan_internet():
    print("\n=== Cek Kecepatan Internet ===")
    print("Mengukur kecepatan internet. Mohon tunggu...")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        loading_animation_tool("Pengecekan Kecepatan Internet", 5)
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"{'Kecepatan Download:':<20} {download_speed:.2f} Mbps")
        print(f"{'Kecepatan Upload:':<20} {upload_speed:.2f} Mbps")
        return {"download": download_speed, "upload": upload_speed}
    except Exception as e:
        print(f"Terjadi kesalahan saat menguji kecepatan internet: {e}")
        return {"download": 0, "upload": 0}


def cek_ram_dan_memory():
    loading_animation_tool("Pemeriksaan RAM dan Memory", 3)
    print("\n=== Informasi RAM & Memory ===")
    ram = psutil.virtual_memory()
    total_ram = ram.total / 1_000_000_000  # Convert to GB
    used_ram = ram.used / 1_000_000_000  # Convert to GB
    free_ram = ram.available / 1_000_000_000  # Convert to GB

    disk = psutil.disk_usage('/')
    total_disk = disk.total / 1_000_000_000  # Convert to GB
    used_disk = disk.used / 1_000_000_000  # Convert to GB
    free_disk = disk.free / 1_000_000_000  # Convert to GB

    print(f"{'Total RAM:':<20} {total_ram:.2f} GB")
    print(f"{'RAM Terpakai:':<20} {used_ram:.2f} GB")
    print(f"{'RAM Tersedia:':<20} {free_ram:.2f} GB")
    print(f"{'Total Memory (Disk):':<20} {total_disk:.2f} GB")
    print(f"{'Memory Terpakai:':<20} {used_disk:.2f} GB")
    print(f"{'Memory Tersedia:':<20} {free_disk:.2f} GB")

    return {
        "total_ram": total_ram,
        "used_ram": used_ram,
        "free_ram": free_ram,
        "total_disk": total_disk,
        "used_disk": used_disk,
        "free_disk": free_disk
    }


def scan_virus():
    loading_animation_tool("Pemindaian Virus", 5)
    print("\n=== Pemindaian Virus ===")
    print("Memindai sistem untuk mendeteksi virus... (Simulasi)")
    time.sleep(2)  # Simulasi pemindaian virus
    print("Pemindaian selesai!")
    print("Tidak ditemukan virus atau malware.")
    return True


def display_summary(device_info, internet_info, memory_info):
    print("\n=== Kesimpulan ===")
    print(f"Perangkat Anda menggunakan {device_info['os_info']} dengan prosesor {device_info['processor']}.")
    print(f"Kecepatan internet Anda tercatat {internet_info['download']:.2f} Mbps untuk download dan {internet_info['upload']:.2f} Mbps untuk upload.")
    print(f"RAM perangkat Anda adalah {memory_info['total_ram']:.2f} GB, dengan {memory_info['free_ram']:.2f} GB tersedia.")
    print(f"Memory penyimpanan total adalah {memory_info['total_disk']:.2f} GB, dengan {memory_info['free_disk']:.2f} GB tersedia.")


def display_footer():
    print("\nTerima kasih telah menggunakan tool ini.")
    print("Semoga informasi ini bermanfaat untuk Anda!")
    print(Fore.MAGENTA + "- Quincy Dev" + Style.RESET_ALL)


if __name__ == "__main__":
    display_header()
    loading_animation_tool("Memuat Tool", 3)  # Durasi loading total: 3 detik
    device_info = cek_device()
    internet_info = cek_kecepatan_internet()
    memory_info = cek_ram_dan_memory()
    scan_virus()  # Panggil fungsi pemindaian virus
    display_summary(device_info, internet_info, memory_info)
    display_footer()

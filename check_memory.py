import psutil


def check_memory_usage():
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {mem.percent}%")


if __name__ == "__main__":
    check_memory_usage()

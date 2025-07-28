from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class LogFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("sample_watch.log"):
            print(f"{event.src_path} was modified.")
            with open(event.src_path, "r") as file:
                lines = file.readlines()
                print("Last line:", lines[-1].strip())


if __name__ == "__main__":
    path = "."  # current directory
    event_handler = LogFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    print("Watching for changes to 'sample.log'...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

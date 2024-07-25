from watchdog.events import FileSystemEventHandler
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from subdomain_checker import SubdomainChecker

class JSONFileHandler(FileSystemEventHandler):
    def __init__(self, checker: 'SubdomainChecker'):
        self.checker = checker

    def on_modified(self, event):
        if event.src_path == self.checker.json_file:
            print("*** Detected change in JSON file. Reloading subdomains...")
            self.checker.load_subdomains()
            statuses = self.checker.check_status()
            self.checker.display_status_table(statuses)

from __future__ import annotations
import requests
from prettytable import PrettyTable
import json
import os
import time
from typing import List, Tuple
from watchdog.observers import Observer
from json_file_handler import JSONFileHandler

class SubdomainChecker:
    def __init__(self, json_file: str):
        self.json_file = os.path.abspath(json_file)
        self.subdomains = []
        self.load_subdomains()
        self.setup_observer()

    def setup_observer(self):
        event_handler = JSONFileHandler(self)
        observer = Observer()
        path = os.path.dirname(self.json_file)
        print(f"Watching for changes in {path}")
        observer.schedule(event_handler, path=path, recursive=False)
        observer.start()
        
    def load_subdomains(self) -> None:
        print("Loading subdomains from JSON file...")
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                if self.validate_json_structure(data):
                    self.subdomains = data['subdomains']
                    print(f"Loaded subdomains: {self.subdomains}")
                else:
                    print("Invalid JSON structure. Please ensure the JSON file has a 'subdomains' key with a list of URLs.")
                    self.subdomains = []
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading JSON file: {e}")
            self.subdomains = []

    def validate_json_structure(self, data: dict) -> bool:
        return isinstance(data, dict) and 'subdomains' in data and isinstance(data['subdomains'], list)

    def check_status(self) -> List[Tuple[str, str]]:
        statuses = []
        for subdomain in self.subdomains:
            try:
                response = requests.get(subdomain)
                if response.status_code == 200:
                    statuses.append((subdomain, "Up"))
                else:
                    statuses.append((subdomain, "Down"))
            except requests.RequestException:
                statuses.append((subdomain, "Down"))
        return statuses

    def display_status_table(self, statuses: List[Tuple[str, str]]) -> None:
        table = PrettyTable()
        table.field_names = ["Subdomain", "Status"]
        for subdomain, status in statuses:
            table.add_row([subdomain, status])
        print(table)

    def run(self) -> None:
        while True:
            statuses = self.check_status()
            self.display_status_table(statuses)
            time.sleep(60)

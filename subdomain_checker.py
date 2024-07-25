import json
import time
from typing import List, Tuple
from prettytable import PrettyTable

import requests


class SubdomainChecker:
    def __init__(self, json_file: str):
        self.subdomains = self.load_subdomains(json_file)

    def load_subdomains(self, json_file: str) -> List[str]:
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data['subdomains']

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
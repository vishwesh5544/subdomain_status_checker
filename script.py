import requests
import time
import json
from typing import List, Tuple

from subdomain_checker import SubdomainChecker


if __name__ == "__main__":
    checker = SubdomainChecker("subdomains.json")
    checker.run()

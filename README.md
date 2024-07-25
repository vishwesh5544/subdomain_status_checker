
# Subdomain Status Checker

This Python script checks the status of multiple subdomains listed in a JSON file and updates their status every minute. The statuses are displayed in a tabular format on the screen.

## Prerequisites

- Python 3.x
- `requests` library
- `prettytable` library

You can install the required libraries using pip:

```bash
pip install requests prettytable
```

## How to Use

1. **JSON File**: Create a JSON file named `subdomains.json` with the subdomains you want to monitor. The subdomains should be complete URLs including the scheme (`http` or `https`).

    Example of `subdomains.json`:

    ```json
    {
      "subdomains": [
        "http://subdomain1.example.com",
        "http://subdomain2.example.com",
        "http://subdomain3.example.com"
      ]
    }
    ```

2. **Running the Script**: Run the script from the command line:

    ```bash
    python check_subdomains_status.py
    ```

3. **Output**: The script will display the status of each subdomain in a tabular format. The status will be updated every minute.

## Classes and Methods

### Class `SubdomainChecker`

- **`__init__(self, json_file: str)`**: Initializes the checker with subdomains loaded from a JSON file.
- **`load_subdomains(self, json_file: str) -> List[str]`**: Loads subdomains from the specified JSON file.
- **`check_status(self) -> List[Tuple[str, str]]`**: Checks the status of each subdomain and returns a list of tuples containing subdomain and its status ("Up" or "Down").
- **`display_status_table(self, statuses: List[Tuple[str, str]]) -> None`**: Displays the statuses in a tabular format using the `prettytable` library.
- **`run(self) -> None`**: Continuously checks the status of the subdomains every minute and displays the updated statuses on the screen.

## Example

1. **JSON File**:

    ```json
    {
      "subdomains": [
        "http://subdomain1.example.com",
        "http://subdomain2.example.com",
        "http://subdomain3.example.com"
      ]
    }
    ```

2. **Output**:

    ```plaintext
    +-----------------------------+-------+
    |          Subdomain          | Status|
    +-----------------------------+-------+
    | http://subdomain1.example.com | Up   |
    | http://subdomain2.example.com | Down |
    | http://subdomain3.example.com | Up   |
    +-----------------------------+-------+
    ```

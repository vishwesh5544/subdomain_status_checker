
# Subdomain Status Checker

This Python script checks the status of multiple subdomains listed in a JSON file and updates their status every minute. The statuses are displayed in a tabular format on the screen. The script also monitors the JSON file for changes and reloads it if modified, displaying the updated statuses.

## Prerequisites

- Python 3.x
- `requests` library
- `prettytable` library
- `watchdog` library

You can install the required libraries using pip:

```bash
pip install requests prettytable watchdog
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
    python script.py
    ```

3. **Output**: The script will display the status of each subdomain in a tabular format. The status will be updated every minute. If the `subdomains.json` file is modified, the script will reload the subdomains automatically and display the updated statuses.

## Classes and Methods

### Class `SubdomainChecker` (in `subdomain_checker.py`)

- **`__init__(self, json_file: str)`**: Initializes the checker with subdomains loaded from a JSON file and sets up a file observer.
- **`setup_observer(self)`**: Sets up a file observer to watch for changes in the JSON file.
- **`load_subdomains(self) -> None`**: Loads subdomains from the specified JSON file.
- **`validate_json_structure(self, data: dict) -> bool`**: Validates the structure of the JSON data.
- **`check_status(self) -> List[Tuple[str, str]]`**: Checks the status of each subdomain and returns a list of tuples containing subdomain and its status ("Up" or "Down").
- **`display_status_table(self, statuses: List[Tuple[str, str]]) -> None`**: Displays the statuses in a tabular format using the `prettytable` library.
- **`run(self) -> None`**: Continuously checks the status of the subdomains every minute and displays the updated statuses on the screen.

### Class `JSONFileHandler` (in `json_file_handler.py`)

- **`__init__(self, checker)`**: Initializes the handler with a reference to the `SubdomainChecker` instance.
- **`on_modified(self, event)`**: Reloads the subdomains if the JSON file is modified and displays the updated statuses.

### Main script (in `script.py`)

- Initializes the `SubdomainChecker` with the JSON file and runs the checker.

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

This script and documentation provide a robust solution for monitoring the status of multiple subdomains listed in a JSON file, with the added functionality of reloading the file if it is modified, all while following an object-oriented approach and separating classes into different files.

## Note

This setup is done on Linux Pop!_OS using Neovim as the text editor.

Link to my Neovim config: [Neovish](https://github.com/vishwesh5544/neovish)

## Contact

For any issues or questions, contact Vishwesh Shukla at <vishweshshukla20@gmail.com>.

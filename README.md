# Spender App Log Processor
This project contains scripts for processing the [Spender App](https://spender.me) log file and transforming the transaction data contained in it into a usable CSV format.

## Features
- **Log to CSV Conversion**: Extracts specific fields from log entries and saves them into a CSV file for easier data handling.
- **Unique entries**: Removes all duplicate transactions.
- ~~**Category Update**: Updates the `categoryLocal` field in the CSV with the most recent category names from the log file.~~

## Requirements
- Python 3.6 or higher

## Setup
1. Ensure Python 3 is installed on your system.
2. Clone this repository or download the scripts directly.
3. Place your log file in the same directory as the scripts or specify its path when running the scripts.


## Configuration
- The `main.py` script can be configured to adjust the batch size for processing. Modify the `batch_size` variable at the top of the script to change how many entries are processed at once.
- ~~The `update_categories.py` script should be run after `main.py` to ensure category names are updated based on the latest available information in the log file.~~

## Contributing

Feel free to fork the project and submit pull requests with any enhancements or bug fixes.

## License

[MIT License](LICENSE.md)

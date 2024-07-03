# Logger Module

## Overview

The Logger module is a simple utility designed for logging information to both the console and a file. It is initialized with specific parameters that define the logging behavior and file storage.

## Features

- **Console Logging**: Logs messages to the console.
- **File Logging**: Logs messages to a specified file.
- **Configurable Parameters**: Allows customization of log file paths and names.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install any required dependencies:
   ```sh
   pip install git+<link_to_this_repo>@main
   ```

## Usage

1. Import the Logger module into your script:
   ```python
   from logger import Logger
   ```

2. Create an instance of the `Logger` class with the required parameters:
   ```python
   Logger = Logger(NAME, ID, LOGS_PATH, LOGS_CATALOG)
   ```
    - `NAME`: The name of the logger instance.
    - `ID`: The ID of the logger instance.
    - `LOGS_PATH`: The path to the directory where log files will be stored.
    - `LOGS_CATALOG`: The name of the log file.
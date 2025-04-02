# Task Tracker CLI

`task_tracker_py` is a simple command-line interface (CLI) application for managing tasks. It allows users to add, list, and manage tasks stored in a `tasks.json` file.

## Features

- Add tasks with a description.
- List all tasks.
- Mark tasks as completed (future feature).
- Delete tasks (future feature).

## Project Structure
task_tracker_py/
├── task_tracker_py/
│   ├── __init__.py - Initializes the package.
│   ├── task_tracker - Main CLI script for task management.
│   └── task.py - Contains the Task class and related logic.
└── tasks.json - Stores tasks in JSON format.

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-tracker-python.git
   cd task-tracker-python
   ```

2. Make the CLI script executable:
   ```bash
   chmod u+x task_tracker_py/task_tracker
   ```

3. (Optional) Add the script to your PATH for easier access:
   ```bash
   ln -s $(pwd)/task_tracker_py/task_tracker /usr/local/bin/task_tracker
   ```

## Usage

### Add a Task

To add a new task, use the `add` command:
```bash
./task_tracker_py/task_tracker add "buy groceries"
```
This will add the task `"buy groceries"` to the `tasks.json` file.

### List Tasks

To list all tasks:
```bash
./task_tracker_py/task_tracker list
```

### Update a Task

To update a task:
```bash
./task_tracker_py/task_tracker update <task_id> <status>
```

### Delete a Task

To delete a task:
```bash
./task_tracker_py/task_tracker delete <task_id>
```

## Development

To extend the project:
1. Add new features by modifying the `task.py` and `task_tracker` files.
2. Test your changes using Python's built-in `unittest` framework or any other testing tool of your choice.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Key Updates:
1. **Expanded Project Structure**:
   - Added descriptions for each file in the structure.

2. **Detailed Usage**:
   - Included examples for adding tasks and future commands like `list`, `complete`, and `delete`.

3. **Development Section**:
   - Added instructions for extending the project and testing.

4. **Contributing and License**:
   - Added sections to encourage contributions and clarify licensing.
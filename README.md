# Silt

Automated Legacy Codebase Explainer

## Overview

Silt analyzes legacy or unfamiliar Python codebases and generates a simple, human-readable markdown report. It leverages the OpenAI API to produce natural-language summaries of code files based on extracted imports and function names.

## Features

- Recursively parse a local Python project directory
- Extract imports and function names from each `.py` file
- Call OpenAI API to generate concise, natural-language summaries per file
- Generate a simple markdown report listing all files with AI-generated descriptions
- Basic CLI interface using Typer

## Tech Stack

- Python 3.x standard libraries (`ast`, `pathlib`)
- OpenAI API (gpt-3.5-turbo)
- Typer for CLI
- Rich for colored terminal output

### Project Structure
```bash
Silt/
├── src/
│ ├── parser.py
│ ├── llm_explainer.py
│ ├── report_generator.py
│ └── main.py
├── prompts/
│ └── module_purpose.txt
├── examples/
│ └── sample_output.md
├── requirements.txt
└── README.md
```


## Installation

```bash
git clone https://github.com/yourusername/code-archaeology.git
cd code-archaeology
pip install -r requirements.txt
```

Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Usage

Analyze a repository:
```bash
python -m src.main --path /path/to/repo # Can only be repositories on your local machine
```

Example with a GitHub repo:
```bash
python -m src.main --repo https://github.com/pallets/flask
```

Reports are generated in the reports/ directory by default.

## Example Output
Sample Markdown report includes:
- File list with imports and functions
- AI-generated summaries describing what each file likely does

## License
This project is licensed under the [MIT License](./LICENSE).

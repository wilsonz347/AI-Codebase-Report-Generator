# Silt

Automated Legacy Codebase Explainer

## Overview

Silt analyzes legacy or unfamiliar codebases and generates a structured, human-readable report that explains system architecture, dependencies, and intent.

## Core Features

### Codebase Ingestion and Analysis
- Parse a local or remote (GitHub) repository
- Extract directory structure, imports, functions, and classes
- Build dependency graphs between modules

### LLM-Driven Insights
- **Module Purpose Inference**: Generate natural-language summaries for files and components  
- **Architectural Pattern Detection**: Identify patterns such as MVC, Factory, or Singleton  
- **Dead Code Detection**: Flag unused functions and classes  
- **Implicit Documentation**: Explain under-documented sections  
- **Design Reasoning**: Provide hypotheses on why certain code exists or is structured a certain way

### Interactive Report Generation
- Executive summary of the codebase  
- Hierarchical breakdown of modules  
- Mermaid-based dependency visualization  
- Section for anomalies and potential refactor candidates  
- Suggested starting points for new developers

## Technical Overview

### Tech Stack
- Python 3.x  
- Tree-sitter for multi-language parsing  
- NetworkX for dependency graph construction  
- OpenAI API (GPT-4 or GPT-3.5-turbo) for LLM inference  
- Rich and Typer for the command-line interface  
- Markdown output with Mermaid diagrams

### Project Structure
```bash
Silt/
├── src/
│ ├── parser.py
│ ├── analyzer.py
│ ├── llm_explainer.py
│ ├── report_generator.py
│ └── main.py
├── prompts/
│ ├── module_purpose.txt
│ ├── pattern_detection.txt
│ └── code_mystery.txt
├── examples/
│ └── sample_output.md
├── tests/
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
python -m src.main --path /path/to/repo
```

Example with a GitHub repo:
```bash
python -m src.main --repo https://github.com/pallets/flask
```

Reports are generated in the reports/ directory by default.

## Example Output
Sample Markdown report includes:
- Executive summary
- File-level purpose explanations
- Dependency diagram in Mermaid syntax
- List of potential issues or "mysteries"

See examples/sample_output.md for a sample output.

## License
MIT License

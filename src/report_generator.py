"""
MARKDOWN REPORT GENERATION
"""
from pathlib import Path

def generate_report(summaries, output_dir='reports/', filename='report.md'):
  """
  Restructure report in markdown format
  
  Returns: Path to generated report
  """
  # Generate a new folder
  Path(output_dir).mkdir(parents=True, exist_ok=True)
  rpath = Path(output_dir) / filename
  
  # Write to file: structure it as markdown
  with open(rpath, "w") as f:
    f.write("# Codebase Summary Report\n\n")
    for item in summaries:
      f.write(f"## {item['File']}\n")
      f.write(f"{item['Summary']}\n\n")
      
  return str(rpath)
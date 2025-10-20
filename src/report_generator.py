"""
MARKDOWN REPORT GENERATION

Purpose: Generate comprehensive, well-formatted markdown reports from analysis results.

What this file should contain:
- Report structure templating
- Markdown formatting utilities
- Mermaid diagram generation for dependency graphs
- Section builders for different report parts:
  * Executive summary
  * File tree visualization
  * Module-by-module breakdown
  * Dependency visualization
  * Pattern findings
  * Mystery/anomaly section
  * Recommendations for new developers
- Table generation for metrics and comparisons
- Code snippet embedding with syntax highlighting markers
- Collapsible sections for detailed information
- Table of contents generation with anchor links
- HTML export functionality (optional)
- Statistics summary (file count, LOC, complexity distribution)

Key classes/functions:
- ReportGenerator class
- generate_report(analysis_results) -> str
- build_executive_summary(stats, key_findings) -> str
- build_dependency_diagram(graph) -> str (Mermaid syntax)
- build_module_section(module_analysis) -> str
- build_mystery_section(mysteries) -> str
- build_recommendations(entry_points, patterns) -> str
- export_to_markdown(report_content, filepath)
- export_to_html(report_content, filepath) -> optional
- generate_toc(report_sections) -> str
"""

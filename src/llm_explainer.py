"""
LLM API INTEGRATION & PROMPT ENGINEERING

Purpose: Interface with OpenAI API to generate natural language explanations.

What this file should contain:
- OpenAI API client initialization and configuration
- Prompt templates for different analysis types
- Response caching mechanism (avoid re-analyzing same code)
- Token counting and cost estimation
- Rate limiting and retry logic with exponential backoff
- Batch processing of similar requests
- Context window management (chunking large files)
- Different explanation strategies:
  * Module/file purpose explanation
  * Function intent inference
  * Pattern explanation (why this pattern was chosen)
  * Design decision reasoning
  * Mystery code explanation
- Response parsing and validation
- Error handling for API failures
- Cost tracking and logging

Key classes/functions:
- LLMExplainer class with OpenAI client
- explain_module_purpose(file_content, context) -> str
- explain_pattern(pattern_type, code_snippet) -> str
- explain_mystery(code_snippet, context) -> str
- infer_design_reasoning(code_snippet) -> str
- _build_prompt(template, code, context) -> str
- _call_api_with_retry(prompt, model) -> str
- cache_response(key, response)
- estimate_cost(token_count) -> float

Prompt templates to include:
- MODULE_PURPOSE_PROMPT
- PATTERN_DETECTION_PROMPT
- MYSTERY_EXPLANATION_PROMPT
- DESIGN_REASONING_PROMPT
"""

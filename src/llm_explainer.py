import os
from openai import OpenAI

class LLMExplainer:
    """LLM explainer for generating file/module summaries using OpenAI API."""

    def __init__(self, api_key=None, model="gpt-3.5-turbo", prompt_path="../prompts/module_purpose.txt"):
      # Initialize OpenAI client & model
      self.api_key = api_key or os.getenv("OPENAI_API_KEY")
      self.model = model
      self.client = OpenAI(api_key=self.api_key)
      with open(prompt_path, "r") as f:
          self.prompt_template = f.read()

    def explain_module_purpose(self, file_info):
      """
      Generate a summary for a Python file given its imports and functions.
      
      Returns: LLM-generated summary of the file's purpose.
      """
      
      # Insert the format of the prompt
      prompt = self.prompt_template.format(
          filename=file_info['path'],
          imports=", ".join(file_info['imports']),
          functions=", ".join(file_info['functions'])
      )

      # Sends the prompt to GPT model 3.5-turbo
      response = self.client.chat.completions.create(
          model=self.model,
          messages=[
              {"role": "system", "content": "You are an expert codebase manager. Given only file names, imports, and function names, you infer and summarize the likely purpose of each file as clearly as possible."},
              {"role": "user", "content": prompt}
          ]
      )
      return response.choices[0].message.content.strip()

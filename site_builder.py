import os
from markdown import markdown

BUILD_DIRECTORY = "build"

def convert_to_html(content: str) -> str:
   return markdown(content)

def make_build(html_content: dict[str, str]):
   os.makedirs(BUILD_DIRECTORY, exist_ok=True)
   for (name, content) in html_content.items():
      with open(f"{BUILD_DIRECTORY}/{name}.html", "w") as f:
         f.write(convert_to_html(content))
   
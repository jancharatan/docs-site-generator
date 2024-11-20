import os
from markdown import markdown

BUILD_DIRECTORY = "build"

def create_tag(tag_name: str, attribute: str, is_open: bool) -> str:
   attribute_info = f" {attribute}" if (is_open and attribute) else ""
   optional_closing = "" if is_open else "/"
   return f"<{optional_closing}{tag_name}{attribute_info}>"

def create_link(text: str, to: str) -> str:
   return create_tag("a", f"href={to}", True) + text + create_tag("a", None, False)

def create_header(text: str) -> str:
   return create_tag("h1", "class=header", True) + text + create_tag("h1", None, False)

def convert_to_html(content: str) -> str:
   return markdown(content)

def make_build(html_content: dict[str, str]):
   os.makedirs(BUILD_DIRECTORY, exist_ok=True)
   with open(f"{BUILD_DIRECTORY}/index.html", "w") as f:
      f.write(create_header("Jan's website"))
      for (name, _) in html_content.items():
          f.write(create_link(name, f"{name}.html"))

   for (name, content) in html_content.items():
      with open(f"{BUILD_DIRECTORY}/{name}.html", "w") as f:
         f.write(convert_to_html(content))

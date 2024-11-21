import os
from markdown import markdown
from html_generator import div, h1, link, css_class

BUILD_DIRECTORY = "build"

HEADER_CLASS = "header"
LINK_CLASS = "link"
NAVBAR_CLASS = "navbar"
STYLESHEET = '<link rel="stylesheet" type="text/css" href="styles.css" />'

def convert_to_html(content: str) -> str:
   return markdown(content)

def create_styles_css():
    with open(f"{BUILD_DIRECTORY}/styles.css", "w") as f:
       f.write(css_class(HEADER_CLASS, ["font-size: xl", "font-weight: bold"]))
       f.write(css_class(LINK_CLASS, ["font-size: xl", "font-weight: bold"]))
       f.write(css_class(NAVBAR_CLASS, ["display: flex", "gap: 16px"]))

def make_build(html_content: dict[str, str]):
    os.makedirs(BUILD_DIRECTORY, exist_ok=True)

    create_styles_css()
    with open(f"{BUILD_DIRECTORY}/index.html", "w") as f:
        f.write(STYLESHEET)
        f.write(h1("Jan's website", HEADER_CLASS))
        
        links = [link(name, f"{name}.html", LINK_CLASS) for (name, _) in html_content.items()]
        f.write(div("".join(links), NAVBAR_CLASS))

    for (name, content) in html_content.items():
        with open(f"{BUILD_DIRECTORY}/{name}.html", "w") as f:
            f.write(STYLESHEET)
            f.write(convert_to_html(content))

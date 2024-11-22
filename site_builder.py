import os
from markdown import markdown
from html_generator import div, h1, link, css_class

BUILD_DIRECTORY = "build"

RUBIK_CLASS = "rubik"
HEADER_CLASS = "header"
LINK_CLASS = "link"
NAVBAR_CLASS = "navbar"
PAGE_CLASS = "page"
STYLESHEET = '<link rel="stylesheet" type="text/css" href="styles.css" />'

def convert_to_html(content: str) -> str:
   return markdown(content)

def get_head() -> str:
    return """<head> 
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
    </head>"""

def create_styles_css():
    with open(f"{BUILD_DIRECTORY}/styles.css", "w") as f:
       f.write("html { overflow: hidden }")
       f.write("* { margin: 0px }")
       f.write(css_class(RUBIK_CLASS, ["font-family: rubik", "font-optical-sizing: auto", "font-weight: 900", "font-style: normal"]))
       f.write(css_class(HEADER_CLASS, ["font-size: 40pt"]))
       f.write(css_class(LINK_CLASS, ["display: flex", "gap: 8px", "font-weight: bold", "font-size: 20pt"]))
       f.write(css_class(NAVBAR_CLASS, ["display: flex", "flex-direction: column", "gap: 16px", "margin-top: 1vh"]))
       f.write(css_class(PAGE_CLASS, ["background-color: #BC8F8F", "width: 100%", "height: 100%", "padding: min(8vh, 8vw)"]))

def page_wrapper(content: str) -> str:
    return get_head() + STYLESHEET + div(content, PAGE_CLASS)

def create_index_html(html_content: dict[str, str]):
    page_content = h1("JAN CHARATAN", f"'{RUBIK_CLASS} {HEADER_CLASS}'")

    links = ""
    for (name, _) in html_content.items():
        links += div("+" + link(f"{name}".lower(), f"{name}.html", None), f"'{RUBIK_CLASS} {LINK_CLASS}'")

    page_content += div("".join(links), NAVBAR_CLASS)

    with open(f"{BUILD_DIRECTORY}/index.html", "w") as f:
        f.write(page_wrapper(page_content))

def create_subpages(html_content: dict[str, str]):
    for (name, content) in html_content.items():
        subpage = convert_to_html(content)
    
        with open(f"{BUILD_DIRECTORY}/{name}.html", "w") as f:    
            f.write(page_wrapper(subpage))

def make_build(html_content: dict[str, str]):
    os.makedirs(BUILD_DIRECTORY, exist_ok=True)

    create_styles_css()
    create_index_html(html_content)
    create_subpages(html_content)

    

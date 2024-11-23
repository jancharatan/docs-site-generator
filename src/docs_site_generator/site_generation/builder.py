import os
from .html_generation import convert_to_html, div, h1, link, get_head, STYLESHEET
from .css_generation import RUBIK_CLASS, HEADER_CLASS, LINK_CLASS, NAVBAR_CLASS, PAGE_CLASS, get_css

BUILD_DIRECTORY = "build"

def page_wrapper(content: str) -> str:
    return get_head() + STYLESHEET + div(content, PAGE_CLASS)

def create_styles_css():
    with open(f"{BUILD_DIRECTORY}/styles.css", "w") as f:
       f.write(get_css())

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

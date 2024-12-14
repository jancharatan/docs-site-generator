from markdown import markdown

STYLESHEET = '<link rel="stylesheet" type="text/css" href="styles.css" />'

def link(text: str, to: str, css_class: str = "") -> str:
   return tag(text, css_class, "a", f"href={to}")

def h1(text: str, css_class: str = "") -> str:
   return tag(text, css_class, "h1")

def div(content: str, css_class: str = "") -> str:
    return tag(content, css_class, "div")

def tag(content: str, css_class: str, tag_name: str, extra_attributes: str = "") -> str:
    return create_tag(tag_name, f"class={css_class} {extra_attributes}", True) + content + create_tag(tag_name, None, False)

def create_tag(tag_name: str, attribute: str, is_open: bool) -> str:
   attribute_info = f" {attribute}" if (is_open and attribute) else ""
   optional_closing = "" if is_open else "/"
   return f"<{optional_closing}{tag_name}{attribute_info}>"

def convert_to_html(content: str) -> str:
   content = content.replace("\n\n\n", "<div class=spacer />")
   return markdown(content)

def get_head() -> str:
    return """<head> 
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
    </head>"""

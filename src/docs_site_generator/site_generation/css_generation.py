HEADER_CLASS = "header"
NAVBAR_LINK_CLASS = "link"
NAVBAR_CLASS = "navbar"
PAGE_CLASS = "page"
SPACER_CLASS = "spacer"

def css_class(class_name: str, attributes: list[str]) -> str:
   if not attributes:
      return ""

   open = f".{class_name} {{ \n"
   attributes = ";\n".join(attributes)
   close = ";\n}\n"
   return open + attributes + close

def get_css():
    return "\n".join([
        "* { margin: 0px }",
        "html { overflow: hidden }",
        css_class(HEADER_CLASS, ["font-size: 40pt"]),
        css_class(NAVBAR_LINK_CLASS, ["display: flex", "gap: 8px", "font-weight: bold", "font-size: 20pt"]),
        css_class(NAVBAR_CLASS, ["display: flex", "flex-direction: column", "gap: 16px", "margin-top: 1vh"]),
        css_class(PAGE_CLASS, ["background-color: #BC8F8F", "width: max(100%, fit-content)", "height: 100%", "padding: min(8vh, 8vw)", "font-family: rubik", "font-optical-sizing: auto", "font-style: normal", "position: relative"]),
        css_class(SPACER_CLASS, ["margin-top: 2vh"])
    ])

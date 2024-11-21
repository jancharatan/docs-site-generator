def create_tag(tag_name: str, attribute: str, is_open: bool) -> str:
   attribute_info = f" {attribute}" if (is_open and attribute) else ""
   optional_closing = "" if is_open else "/"
   return f"<{optional_closing}{tag_name}{attribute_info}>"

def link(text: str, to: str, css_class: str) -> str:
   return create_tag("a", f"href={to} class={css_class}", True) + text + create_tag("a", None, False)

def h1(text: str, css_class: str) -> str:
   return tag_with_css_class(text, css_class, "h1")

def div(content: str, css_class: str) -> str:
    return tag_with_css_class(content, css_class, "div")

def tag_with_css_class(content: str, css_class: str, tag_name: str) -> str:
    return create_tag(tag_name, f"class={css_class}", True) + content + create_tag(tag_name, None, False)

def css_class(class_name: str, attributes: list[str]) -> str:
   if not attributes:
      return ""

   open = f".{class_name} {{ \n"
   attributes = ";\n".join(attributes)
   close = ";\n}\n"
   return open + attributes + close

def extract_plaintext_from_google_doc(data):
    text_content = []

    for element in data['body']['content']:
        if 'paragraph' in element:
            paragraph = element['paragraph']
            
            if 'bullet' in paragraph:
                bullet_symbol = "- "
                text_content.append(bullet_symbol)

            for text_element in paragraph.get('elements', []):
                if 'textRun' in text_element:
                    text_content.append(text_element['textRun'].get('content', ''))

            text_content.append('\n')

    return ''.join(text_content)
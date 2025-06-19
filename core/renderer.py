import re

import markdown


def markdown_to_html(md_content: str, extensions=None):
    """Convierte Markdown a HTML usando python-markdown"""
    # No incluir 'toc' por defecto ya que se maneja manualmente
    default_extensions = ['extra', 'tables', 'fenced_code', 'codehilite', 'attr_list', 'def_list', 'footnotes', 'md_in_html', 'nl2br', 'sane_lists', 'smarty', 'abbr', 'admonition', 'legacy_attrs', 'legacy_em', 'meta', 'wikilinks']
    md = markdown.Markdown(extensions=extensions or default_extensions)
    return md.convert(md_content)

def insert_automatic_toc(html_content: str, toc_levels: int = 3, number_headings: bool = False) -> str:
    """Insertar tabla de contenidos automática después del primer heading, con personalización de niveles y numeración y navegación."""
    print(f"[DEBUG] insert_automatic_toc: toc_levels={toc_levels}, number_headings={number_headings}")
    heading_pattern = r'<h([1-6])([^>]*)>(.*?)</h\1>'
    match = re.search(heading_pattern, html_content)
    if not match:
        print("[DEBUG] insert_automatic_toc: No se encontraron headings, retornando HTML original")
        return html_content
    print(f"[DEBUG] insert_automatic_toc: Encontrado heading: {match.group(0)}")
    toc_html, heading_numbers, anchor_ids = generate_toc_html(html_content, toc_levels, number_headings, return_anchors=True)
    print(f"[DEBUG] insert_automatic_toc: TOC generada: {len(toc_html)} caracteres")
    # Añadir id a los headings
    def add_id(match):
        level = int(match.group(1))
        attrs = match.group(2)
        title = match.group(3)
        clean_title = re.sub(r'<[^>]+>', '', title)
        anchor_id = re.sub(r'[^a-zA-Z0-9\s-]', '', clean_title.lower()).replace(' ', '-')
        # Si ya tiene id, no lo duplica
        if 'id=' in attrs:
            return match.group(0)
        return f'<h{level}{attrs} id="{anchor_id}">{title}</h{level}>'
    html_content = re.sub(heading_pattern, add_id, html_content)
    # Si se solicita numerar, reemplazar los headings en el HTML
    if number_headings and heading_numbers:
        def add_number(match):
            level = int(match.group(1))
            attrs = match.group(2)
            title = match.group(3)
            num = heading_numbers.pop(0)
            return f'<h{level}{attrs}>{num} {title}</h{level}>'
        html_content = re.sub(heading_pattern, add_number, html_content)
    heading_match = re.search(heading_pattern, html_content)
    heading_end = heading_match.end() if heading_match else 0
    result = html_content[:heading_end] + '\n' + toc_html + '\n' + html_content[heading_end:]
    print(f"[DEBUG] insert_automatic_toc: HTML resultante: {len(result)} caracteres")
    return result

def generate_toc_html(html_content: str, toc_levels: int = 3, number_headings: bool = False, return_anchors: bool = False) -> tuple:
    heading_pattern = r'<h([1-6])[^>]*>(.*?)</h\1>'
    headings = re.findall(heading_pattern, html_content)
    if len(headings) < 2:
        return ("", [], []) if return_anchors else ("", [])
    toc_items = []
    heading_numbers = []
    anchor_ids = []
    # Numeración por nivel
    counters = [0] * 6
    for level_str, title in headings:
        level = int(level_str)
        if level > toc_levels:
            continue
        clean_title = re.sub(r'<[^>]+>', '', title)
        anchor_id = re.sub(r'[^a-zA-Z0-9\s-]', '', clean_title.lower()).replace(' ', '-')
        anchor_ids.append(anchor_id)
        if number_headings:
            counters[level-1] += 1
            for i in range(level, 6):
                counters[i] = 0
            num = '.'.join(str(counters[i]) for i in range(level) if counters[i] > 0)
            heading_numbers.append(num)
            display_title = f'{num} {clean_title}'
        else:
            display_title = clean_title
        indent = (level - 1) * 20
        toc_items.append(f'<li style="margin-left: {indent}px;"><a href="#{anchor_id}" style="text-decoration: none; color: #2c3e50;">{display_title}</a></li>')
    toc_html = f'''<div class="table-of-contents" style="background-color: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px; padding: 1.5em; margin: 2em 0; page-break-inside: avoid;"><h2 style="margin-top: 0; color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 0.5em;">📋 Tabla de Contenidos</h2><ul style="list-style-type: none; padding-left: 0; margin: 0;">{''.join(toc_items)}</ul></div>'''
    if return_anchors:
        return toc_html, heading_numbers, anchor_ids
    return toc_html, heading_numbers

def safe_update_metadata(doc_metadata, metadata):
    if isinstance(doc_metadata, dict):
        if metadata:
            doc_metadata.update(metadata)
        return doc_metadata
    elif isinstance(metadata, dict):
        return metadata
    else:
        return {}

# ... en el flujo de conversión principal ...
# doc_metadata, clean_content = extract_metadata(markdown_content)
# doc_metadata = safe_update_metadata(doc_metadata, metadata) 
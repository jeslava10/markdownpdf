import re

yaml_delimiter = re.compile(r'^---$', re.MULTILINE)

def extract_metadata(content: str):
    """Extrae metadatos YAML y devuelve (metadata_dict, markdown_content)"""
    import yaml
    parts = yaml_delimiter.split(content, maxsplit=2)
    if len(parts) >= 3:
        _, yaml_block, markdown_content = parts
        try:
            metadata = yaml.safe_load(yaml_block)
        except Exception:
            metadata = {}
        return metadata or {}, markdown_content.lstrip('\n')
    return {}, content 
from pathlib import Path
from typing import Optional

from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration


def export_pdf(html_content: str, output_path: Path, base_url: Path, style_file: Optional[Path] = None):
    font_config = FontConfiguration()
    stylesheets = [CSS(filename=str(style_file))] if style_file and style_file.exists() else None
    HTML(string=html_content, base_url=base_url).write_pdf(
        output_path,
        stylesheets=stylesheets,
        font_config=font_config
    ) 
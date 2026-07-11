import pytest
from html.parser import HTMLParser

class StructureParser(HTMLParser):
    """HTML parser to extract structural elements from HTML file."""
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title_text = ""
        self.ids_found = set()

    def handle_starttag(self, tag, attrs):
        """Handle the start of a tag, checking for title and capturing ids."""
        if tag == "title":
            self.in_title = True
        for attr in attrs:
            if attr[0] == "id":
                self.ids_found.add(attr[1])

    def handle_endtag(self, tag):
        """Handle the end of a tag to stop capturing title data."""
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        """Capture data inside the title tag."""
        if self.in_title:
            self.title_text += data

def test_index_html_structure():
    """Test index.html structure using HTMLParser to ensure it has required elements."""
    parser = StructureParser()
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            parser.feed(f.read())
    except FileNotFoundError:
        pytest.fail("index.html not found")

    assert parser.title_text == "JenR8ed Terminal Portfolio"
    assert "whoami" in parser.ids_found
    assert "stack" in parser.ids_found
    assert "projects" in parser.ids_found
    assert "contact" in parser.ids_found

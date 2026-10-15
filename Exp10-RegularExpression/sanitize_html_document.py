import re

html_doc = """<div>
    <h1>Welcome to &lt;Lab&gt;!</h1>
    <p>This is a paragraph with <b>bold</b> text and   extra    spaces!!</p>
</div>"""

no_html = re.sub(r'<[^>]+>', ' ', html_doc)
no_special = re.sub(r'[^a-zA-Z0-9\s]', '', no_html)
clean_text = re.sub(r'\s+', ' ', no_special).strip()

print("Sanitized text:")
print(clean_text)

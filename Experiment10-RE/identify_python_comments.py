import re

code_sample = """# Global counter variable
x = 10
url = "http://example.com/#anchor"  # trailing comment
print("# This is inside a string, not a comment")
# End of file
"""

comments = re.findall(r'^[ \t]*#.*$', code_sample, re.MULTILINE)

print("Identified full-line comments:")
for c in comments:
    print(c.strip())

print("\nLimitations of Regex Alone:")
print("- Regex does not maintain lexical parsing state.")
print("- Hashes inside string literals like \"text # note\" can be mistakenly matched.")
print("- Triple-quoted multiline strings or docstrings can be confused with comments.")

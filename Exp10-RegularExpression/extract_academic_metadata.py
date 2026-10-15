import re

references = """1. Smith, J. (2023). Neural Networks. DOI: 10.1016/j.neunet.2023.01.002.
Contact: jsmith@university.edu. Available at https://sciencedirect.com/science/article/1.
2. Kumar, A. (2021). Quantum Computing. DOI: 10.1103/PhysRevA.103.022401.
Contact: akumar@lab.org. URL: http://quantum-lab.org/papers/2021."""

dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', references)
years = re.findall(r'\b(19\d{2}|20\d{2})\b', references)
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', references)
urls = re.findall(r'https?://[^\s]+', references)

print("DOIs:", dois)
print("Publication Years:", years)
print("Emails:", emails)
print("URLs:", urls)

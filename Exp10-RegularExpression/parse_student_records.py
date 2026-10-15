import re

paragraph = """Student records: Amit Kumar with roll 101 secured 88 marks.
Next is Priya Sharma, roll 102, who scored 94 marks.
Rahul Verma (roll 103) obtained 76 marks."""

pattern = r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)?).*?roll\s*(\d+).*?(\d+)\s*marks'
matches = re.findall(pattern, paragraph)

print("Extracted Records (Name, Roll No, Marks):")
for name, roll, marks in matches:
    print(f"Name: {name} | Roll: {roll} | Marks: {marks}")

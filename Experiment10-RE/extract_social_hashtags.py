import re

post = "Learning #Python and #DataScience with #MachineLearning! Join us at #AI_2026."
hashtags = re.findall(r'#\w+', post)

print("Extracted Hashtags:", hashtags)

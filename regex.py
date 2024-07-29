import re

text = "Elon musk's phone number is 9977998889, call him if you have any questions on dogecoin.Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777"

pattern = r"\(\d{3}\)-\d{3}-\d{4}|\d{10}"  # Usage of r

matches = re.findall(pattern, text)

print(matches)

# Double parenthesis approach instead of r

text = "Elon Musk's phone number is 9977998889, call him if you have any questions on Dogecoin. Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777"

pattern = "\\(\\d{3}\\)-\\d{3}-\\d{4}|\\d{10}"

matches = re.findall(pattern, text)

print(matches)

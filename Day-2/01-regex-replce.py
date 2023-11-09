import re
text = "the red fox"
pattern = r"red"
replecement = "brown"

new_text = re.sub(pattern, replecement, text)
search = re.search(pattern, text)
print("The replaced text is;",new_text)
print("text found", search)
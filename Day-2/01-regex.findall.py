import re
text = "the brown colour fox"
pattern= r"fox"
search = re.search(pattern,text)
if search:
    print("pattern found",search)
else:
    print("pettern not found")


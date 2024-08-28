"""
Simple parser for the russian novel .json files

By: Kevin Pettibone 
"""

# -----Measly little import section-----
import json

# -----Constant Section-----
INFILE_NAME = "war and piece.json"
OUTFILE_NAME = "warrenpeace.txt"

# -----The actual code stuff-----

f = open(INFILE_NAME, encoding="utf-8")

tempstr = ""
data = json.load(f)
chapters = data["chapters"]
for chapter in chapters:
    paragraphs = chapter["paragraphs"]
    for paragraph in paragraphs:
        tempstr += paragraph["source_paragraphs"][0]["content"]
print(tempstr)

with open(OUTFILE_NAME, "w", encoding="utf-8") as f:
    f.write(tempstr)

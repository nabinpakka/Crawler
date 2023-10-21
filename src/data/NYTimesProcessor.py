import pandas as pd

file_path = "nytimes.jsonl"
output_path = "nytimes.jsonl"

df = pd.read_json(file_path, lines=True)

df["section"].replace("",)
df.dropna(inplace=True)
df.drop_duplicates(keep='first', inplace=True)

df.to_json(output_path, index=False, lines=True, orient='records')

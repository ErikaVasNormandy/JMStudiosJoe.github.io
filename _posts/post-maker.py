import csv
import os

def generate_markdown(csv_filepath, output_dir):
    with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            filename = f"{row['Date']}-{row['PaintingTitle'].replace(' ', '-')}.md"
            filepath = os.path.join(output_dir, filename)
            
            md_content = f"""---
title: {row['PaintingTitle']}
author: Joey
excerpt: "{row['Description']}"
price: $"{row['Price']}"
skills:
  - oil painting
categories:
  - works
background-image: {row['Painting'].replace(' ', '')}/{row['PaintingTitle'].replace(' ', '')}-preview.jpg

---

## {row['PaintingTitle']}

<img class="imageDisplay" src="/images/{row['Painting'].replace(' ', '')}/{row['PaintingTitle'].replace(' ', '')}.png" onclick="myFunction(this);">

{row['Description']}

## Details
- Date: {row['Date']}
- Dimensions: {row['Width']} x {row['Height']}
- Price: ${row['Price']}

[Etsy Link  ]( {row['StoreLink']} )



"""
            
            with open(filepath, 'w', encoding='utf-8') as mdfile:
                mdfile.write(md_content)
            print(f"Generated: {filepath}")

# Example usage:
def main():
  generate_markdown('Joey-Art.csv', 'output_markdowns')

if __name__ == "__main__":
  main()
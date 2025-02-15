import pandas as pdd

data = {
  "MatMIE": ["Samarbek", "Elif", "Turar", "Ali"],
  "MatDAIS": ["Azem", "Rustam", "Seinasyr", "Daniel"],
  "COMIE" : ["Nursultan", "Muhammed", "Baktyiar", "Daniil"],
  "COMEC" : ["Asyl", "Imran", "Aibek", "Aihan"]
}

df = pdd.DataFrame(data, index = [1, 2, 3, 4])

print(df)
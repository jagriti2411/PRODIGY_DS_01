import pandas as pd
import matplotlib.pyplot as plt
import os

# File dhoondhne ke liye
path = ""
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        if filename.endswith('.csv'):
            path = os.path.join(dirname, filename)

if path:
    df = pd.read_csv(path, skiprows=4)
    # 2023 ka data filter karna
    data = df[['Country Name', '2023']].dropna().sort_values(by='2023', ascending=False).head(10)
    
    # Bar Chart banana
    plt.figure(figsize=(10,6))
    plt.bar(data['Country Name'], data['2023'], color='skyblue')
    plt.title('Top 10 Countries by Population (2023)')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Data nahi mila! Ek baar check karein ki upload finish hua ya nahi.")

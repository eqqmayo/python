import pandas as pd

data = pd.read_csv('data.csv')

# 컬럼명 공백 제거
data.columns = data.columns.str.strip()

filtered_data = data[data['age'] >= 18]
mean_height = filtered_data['height'].mean()

print(f'평균 키: {mean_height}')
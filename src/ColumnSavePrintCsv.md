## ColumnSavePrintCsv
`ColumnIndex`
```python
import pandas as pd

df = pd.read_csv('Test.csv')   # CSV 읽기
print(df.head())               # 상위 5줄 보기

# 첫 번째 컬럼만 선택 (iloc 사용)
first_col = df.iloc[:, [0]]    # df.iloc[:, 0] 하면 Series, [0] 하면 DataFrame
print(first_col.head())

# 새로운 CSV로 저장
first_col.to_csv('NewTest.csv', index=False)
```

`ColumnName`
```python
import pandas as pd

df = pd.read_csv('Test.csv')   # CSV 읽기
print(df.head())               # 상위 5줄 보기

first_col = df[["동영상 ID"]]
print(first_col.head())

# 새로운 CSV로 저장
first_col.to_csv('NewTest.csv', index=False)
```


첫번째행제외
```python
import pandas as pd

# CSV 읽기
df = pd.read_csv('Test.csv')

# 첫 번째 컬럼만 선택
first_col = df[["동영상 ID"]]

# 첫 번째 행 제외 (index=0)
first_col_no_first = first_col.iloc[1:, :]

# 새로운 CSV로 저장, 컬럼 이름 없이
first_col_no_first.to_csv('NewTest.csv', index=False, header=False)
```

## SaveReadCsv
```python
import pandas as pd

df = pd.read_csv('Test.csv')  # CSV 읽기
print(df.head())              # 상위 5줄 보기
df.to_csv('NewTest.csv')  # CSV 저장
```
```python
import pandas as pd

df = pd.read_csv('Test.csv')  # CSV 읽기
print(df.head())              # 상위 5줄 보기
df.to_csv('NewTest.csv', index=False)  # CSV 저장
```

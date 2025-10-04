# PrintCsv

## TotalPrintCsv
```python
import pandas as pd

df = pd.read_csv("Test.csv")
print(df)
```
```python
import csv

with open('Test.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

단위적출력
```python
import pandas as pd

df = pd.read_csv("Test.csv")

for index, row in df.iterrows():
    print(row)
```


## 5PrintCsv
```python
import pandas as pd

df = pd.read_csv("Test.csv")
print(df.head())

# Run Code
# - 최상위경로기준
# - ✅Child .csv
# - ❌GrandChild .csv
```
```python
import pandas as pd

df = pd.read_csv(r"c:\github-nangmanhunter\YoutubeShorts\etc\YouTube\Csv\etc\Test.csv")
print(df.head())

# .head()
# - 5개Default
# - head=5
# - head=5개
# - head()=head(5)
```





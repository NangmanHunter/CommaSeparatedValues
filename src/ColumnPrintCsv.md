## ColumnReadCsv
`csv`
```python
# IndexError출력
import csv

with open("Test.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])  # 첫 번째 열만
```
```python
# 빈줄넘기기
import csv

with open("Test.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row:   # row가 빈 리스트([])면 스킵
            continue
        print(row[0])
```
```python
# IndexError처리
import csv

with open("Test.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            print(row[0])
        except IndexError:
            pass
```

## YouTubeURLCsv
URL붙이기
```python
import pandas as pd

# CSV 읽기
df = pd.read_csv('Test.csv')

# 첫 번째 컬럼만 선택
first_col = df[["동영상 ID"]]

# 각 값 앞에 YouTube URL 붙이기
first_col["동영상 ID"] = "https://www.youtube.com/watch?v=" + first_col["동영상 ID"]

# 새로운 CSV로 저장, 컬럼 이름 없이
first_col.to_csv('NewTest.csv', index=False, header=False)
```
```python
import pandas as pd

# CSV 읽기
df = pd.read_csv('Test.csv')

# 첫 번째 컬럼만 선택
first_col = df[["동영상 ID"]]

# 각 값 앞에 YouTube URL 붙이기
first_col["동영상 ID"] = first_col["동영상 ID"].apply(lambda x: f"https://www.youtube.com/watch?v={x}")

# 새로운 CSV로 저장, 컬럼 이름 없이
first_col.to_csv('NewTest.csv', index=False, header=False)
```


리스트붙이기
```python
import pandas as pd

# CSV 읽기
df = pd.read_csv('Test.csv')

# 첫 번째 컬럼만 선택
first_col = df[["동영상 ID"]]

# 각 값 앞에 YouTube URL 붙이기
first_col["동영상 ID"] = first_col["동영상 ID"].apply(lambda x: f"- https://www.youtube.com/watch?v={x}")

# 새로운 CSV로 저장, 컬럼 이름 없이
first_col.to_csv('NewTest.csv', index=False, header=False)
```


md파일
```python
import pandas as pd

# CSV 읽기
df = pd.read_csv('Test.csv')

# 첫 번째 컬럼만 선택
first_col = df[["동영상 ID"]]

# 각 값 앞에 YouTube URL 붙이기
first_col["동영상 ID"] = first_col["동영상 ID"].apply(lambda x: f"- https://www.youtube.com/watch?v={x}")

# 새로운 CSV로 저장, 컬럼 이름 없이
first_col.to_csv('NewTest.md', index=False, header=False)
```


```python
import pandas as pd

FileName = "Test"

df = pd.read_csv(f"{FileName}.csv") # FileName + ".csv"

first_col = df[["동영상 ID"]]

first_col["동영상 ID"] = first_col["동영상 ID"].apply(lambda x: f"- https://www.youtube.com/watch?v={x}")

first_col.to_csv(f"New{FileName}.md", index=False, header=False)
```


❌각줄추가됨
```python
import pandas as pd

FileName = "Test"

df = pd.read_csv(f"{FileName}.csv")  # CSV 읽기

first_col = df[["동영상 ID"]].copy()  # copy()로 SettingWithCopyWarning 방지

# URL 붙이기
first_col["동영상 ID"] = first_col["동영상 ID"].apply(
    lambda x: f"- https://www.youtube.com/watch?v={x}"
)

# Markdown 파일로 저장 (임시로 CSV 형태로 저장)
csv_content = first_col.to_csv(index=False, header=False)

# 최종 Markdown 파일에 첫 줄 헤더 추가
with open(f"New{FileName}.md", "w", encoding="utf-8") as f:
    f.write(f"## {FileName}\n")  # 첫 줄에 헤더
    f.write(csv_content)          # 나머지 내용 추가
```
- to_csv로 문자열로 만들 때 이미 줄바꿈(\n)이 있는데, 
- f.write가 또 줄바꿈 처리를 하면서 빈 줄이 추가되는 것 때문에 생기는 문제

✅특정파일
```python
import pandas as pd

FileName = "Test"

df = pd.read_csv(f"{FileName}.csv")  # CSV 읽기

first_col = df[["동영상 ID"]].copy()  # copy()로 SettingWithCopyWarning 방지

# URL 붙이기
first_col["동영상 ID"] = first_col["동영상 ID"].apply(
    lambda x: f"- https://www.youtube.com/watch?v={x}"
)

# Markdown 파일로 저장 (임시로 CSV 형태로 저장)
csv_content = first_col.to_csv(index=False, header=False)

# 최종 Markdown 파일에 첫 줄 헤더 추가
with open(f"New{FileName}.md", "w", encoding="utf-8") as f:
    f.write(f"## {FileName}\n")  # 첫 줄에 헤더
    for vid in first_col["동영상 ID"]:
        f.write(f"{vid}\n")       # 한 줄씩 정확히 쓰기
```


❌특정폴더
```python
# 실패
# - 중간에에러나면 걸린다
# - Traceback ...
# 재생목록.csv
# - 여기서걸림.
# - 에러-중단
import pandas as pd
from pathlib import Path

# 처리할 폴더 지정
input_folder = Path(r"C:\Users\djwlf\Downloads\재생목록")
output_folder = input_folder / "MarkdownFiles"
output_folder.mkdir(exist_ok=True)  # 폴더 없으면 생성

# 폴더 안 모든 CSV 파일 반복
for csv_file in input_folder.glob("*.csv"):
    FileName = csv_file.stem  # 확장자 제외한 파일 이름
    df = pd.read_csv(csv_file)

    # 첫 번째 컬럼만 선택
    first_col = df[["동영상 ID"]].copy()

    # URL 붙이기
    first_col["동영상 ID"] = first_col["동영상 ID"].apply(
        lambda x: f"- https://www.youtube.com/watch?v={x}"
    )

    # Markdown 파일 저장
    output_path = output_folder / f"New{FileName}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"## {FileName}\n")  # 첫 줄 헤더
        for vid in first_col["동영상 ID"]:
            f.write(f"{vid}\n")

    print(f"{FileName}.csv -> Markdown 변환 완료")

```

✅특정폴더
```python
import pandas as pd
from pathlib import Path

# 처리할 폴더 지정
input_folder = Path(r"C:\Users\djwlf\Downloads\재생목록")
output_folder = input_folder / "MarkdownFiles"
output_folder.mkdir(exist_ok=True)  # 폴더 없으면 생성

# 폴더 안 모든 CSV 파일 반복
for csv_file in input_folder.glob("*.csv"):
    FileName = csv_file.stem  # 확장자 제외한 파일 이름
    df = pd.read_csv(csv_file, encoding="utf-8-sig")  # 한글 깨짐 방지

    # "동영상 ID" 컬럼 없으면 건너뛰기
    if "동영상 ID" not in df.columns:
        print(f"{csv_file.name}에는 '동영상 ID' 컬럼이 없습니다. 건너뜁니다.")
        continue

    # 첫 번째 컬럼만 선택
    first_col = df[["동영상 ID"]].copy()

    # URL 붙이기
    first_col["동영상 ID"] = first_col["동영상 ID"].apply(
        lambda x: f"- https://www.youtube.com/watch?v={x}"
    )

    # Markdown 파일 저장
    output_path = output_folder / f"New{FileName}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"## {FileName}\n")  # 첫 줄 헤더
        for vid in first_col["동영상 ID"]:
            f.write(f"{vid}\n")

    print(f"{FileName}.csv -> Markdown 변환 완료")
```



명칭변경
```python
import pandas as pd
from pathlib import Path

# 처리할 폴더 지정
input_folder = Path(r"C:\Users\djwlf\Downloads\재생목록")
output_folder = input_folder / "MarkdownFiles"
output_folder.mkdir(exist_ok=True)  # 폴더 없으면 생성

# 폴더 안 모든 CSV 파일 반복
for csv_file in input_folder.glob("*.csv"):
    FileName = csv_file.stem  # 확장자 제외한 파일 이름
    df = pd.read_csv(csv_file, encoding="utf-8-sig")  # 한글 깨짐 방지

    # "동영상 ID" 컬럼 없으면 건너뛰기
    if "동영상 ID" not in df.columns:
        print(f"{csv_file.name}에는 '동영상 ID' 컬럼이 없습니다. 건너뜁니다.")
        continue

    # 첫 번째 컬럼만 선택
    first_col = df[["동영상 ID"]].copy()

    # URL 붙이기
    first_col["동영상 ID"] = first_col["동영상 ID"].apply(
        lambda x: f"- https://www.youtube.com/watch?v={x}"
    )

    # Markdown 파일 저장
    output_path = output_folder / f"{FileName}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"## {FileName}\n")  # 첫 줄 헤더
        for vid in first_col["동영상 ID"]:
            f.write(f"{vid}\n")

    print(f"{FileName}.csv -> Markdown 변환 완료")
```


❌충돌
- ❌파일병합도실행
- Python내에서 프로세스에서 자원잡고있어
- .ps1이 어떻게해든 튕겨져나옴.
- 아싸리 다르게 별도로 잡아서진행ㄱㄱ.
```python
import pandas as pd
from pathlib import Path

# 처리할 폴더 지정
input_folder = Path(r"C:\Users\djwlf\Downloads\재생목록")
output_folder = input_folder / "MarkdownFiles"
output_folder.mkdir(exist_ok=True)  # 폴더 없으면 생성

# 폴더 안 모든 CSV 파일 반복
for csv_file in input_folder.glob("*.csv"):
    FileName = csv_file.stem  # 확장자 제외한 파일 이름
    df = pd.read_csv(csv_file, encoding="utf-8-sig")  # 한글 깨짐 방지

    # "동영상 ID" 컬럼 없으면 건너뛰기
    if "동영상 ID" not in df.columns:
        print(f"{csv_file.name}에는 '동영상 ID' 컬럼이 없습니다. 건너뜁니다.")
        continue

    # 첫 번째 컬럼만 선택
    first_col = df[["동영상 ID"]].copy()

    # URL 붙이기
    first_col["동영상 ID"] = first_col["동영상 ID"].apply(
        lambda x: f"- https://www.youtube.com/watch?v={x}"
    )

    # Markdown 파일 저장
    output_path = output_folder / f"{FileName}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"## {FileName}\n")  # 첫 줄 헤더
        for vid in first_col["동영상 ID"]:
            f.write(f"{vid}\n")

    print(f"{FileName}.csv -> Markdown 변환 완료")



import os

# CSV 처리 끝난 뒤
os.system(r"powershell -ExecutionPolicy Bypass -File C:\github-nangmanhunter\YoutubeShorts\etc\YouTube\Csv\etc\MergeFile.ps1")
```

❌실패
```python
import pandas as pd
from pathlib import Path

# 처리할 폴더 지정
input_folder = Path(r"C:\Users\djwlf\Downloads\재생목록")
output_folder = input_folder / "MarkdownFiles"
output_folder.mkdir(exist_ok=True)  # 폴더 없으면 생성

# 폴더 안 모든 CSV 파일 반복
for csv_file in input_folder.glob("*.csv"):
    FileName = csv_file.stem  # 확장자 제외한 파일 이름
    df = pd.read_csv(csv_file, encoding="utf-8-sig")  # 한글 깨짐 방지

    # "동영상 ID" 컬럼 없으면 건너뛰기
    if "동영상 ID" not in df.columns:
        print(f"{csv_file.name}에는 '동영상 ID' 컬럼이 없습니다. 건너뜁니다.")
        continue

    # 첫 번째 컬럼만 선택
    first_col = df[["동영상 ID"]].copy()

    # URL 붙이기
    first_col["동영상 ID"] = first_col["동영상 ID"].apply(
        lambda x: f"- https://www.youtube.com/watch?v={x}"
    )

    # Markdown 파일 저장
    output_path = output_folder / f"{FileName}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"## {FileName}\n")  # 첫 줄 헤더
        for vid in first_col["동영상 ID"]:
            f.write(f"{vid}\n")

    print(f"{FileName}.csv -> Markdown 변환 완료")



import subprocess

# 기존 CSV -> Markdown 처리 코드 끝난 후

# PowerShell 스크립트 실행
ps_script = r"C:\github-nangmanhunter\YoutubeShorts\etc\YouTube\Csv\etc\MergeFile.ps1"
subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_script])
```




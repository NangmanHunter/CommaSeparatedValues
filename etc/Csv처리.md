



## 특정 열/행만 추출
```python
urls = df["Video URL"].tolist()   # URL 컬럼만 리스트로 추출
first_video = df.iloc[0]          # 첫 번째 행만
```
* Takeout CSV는 **타임스탬프, 제목, ID** 등이 함께 있으므로,
  * **URL만 뽑아서 링크용 리스트** 만들기
  * **정렬용으로 타임스탬프** 활용
    이런 식으로 자주 나눠서 사용함.

## 
```python
recent = df[df["Added Date"] > "2025-01-01"]
```
* 특정 날짜 이후 추가된 영상만, 특정 재생목록만 등





## 3️⃣ R
* 데이터 분석·통계용으로 많이 사용

```R
data <- read.csv("파일.csv")
head(data)
write.csv(data, "새파일.csv", row.names=FALSE)
```

* 장점: 통계 분석에 특화
* 단점: Python보다 범용성 낮음

---

## 4️⃣ 터미널 / 커맨드라인

* **Linux/macOS:** `cat`, `awk`, `sed`, `cut` 등

```bash
head -n 10 파일.csv      # 상위 10줄 보기
cut -d',' -f1,3 파일.csv # 1,3번째 열만 보기
```

* 장점: 스크립트 자동화, 빠름
* 단점: 복잡한 데이터 처리 힘듦

---


## 기타도구
* **TablePlus, DBeaver** 같은 DB 툴 (CSV를 DB처럼 조회)

---

💡 결론:

* **분석/자동화 → Python/pandas**
* **통계 분석 → R**
* **터미널 자동화 → awk/sed/cut**




### 1️⃣ 터미널 / 커맨드라인에서
* Linux / macOS / Git Bash 등에서 사용
```bash
head -n 10 파일.csv
```
* 의미: `파일.csv`의 **첫 10줄**만 출력
* 기본값: `-n` 옵션 안 쓰면 **첫 10줄**이 기본

```bash
head 파일.csv
```

* 반대로 마지막 줄 보고 싶으면 `tail`

```bash
tail -n 10 파일.csv   # 마지막 10줄
```

---

### 2️⃣ Python pandas에서
* `head()` 메서드로 DataFrame 상위 몇 줄 확인 가능
```python
import pandas as pd

df = pd.read_csv('파일.csv')
print(df.head())      # 기본 5줄
print(df.head(10))    # 상위 10줄
```

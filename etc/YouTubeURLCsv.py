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




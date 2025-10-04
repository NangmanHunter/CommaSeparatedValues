# .md파일
$TargetPath = "C:\Users\djwlf\Downloads\재생목록\MarkdownFiles"
$MergeFileName = "MergeFile.md"
Get-ChildItem -Path $TargetPath -File -Filter *.md | Where-Object { $_.Name -ne $MergeFileName } | ForEach-Object {
    "## "+$_.Name
    Get-Content $_.FullName
    ""  
    ""  
} | Set-Content -Path "${TargetPath}\📌${MergeFileName}" -Encoding UTF8
"""Lambda に上げる zip（dist/function.zip）を作る。

使い方（リポジトリのいちばん上で）:
    python scripts/package_lambda.py

warikan/ フォルダの .py ファイルだけを入れる（テストや道具は入れない）。
Lambda の関数の「ハンドラー」は warikan.handler.handler。
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "warikan"
OUT = ROOT / "dist" / "function.zip"


def main() -> None:
    OUT.parent.mkdir(exist_ok=True)
    files = sorted(PACKAGE.glob("*.py"))
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, f.relative_to(ROOT).as_posix())
    names = ", ".join(f.relative_to(ROOT).as_posix() for f in files)
    print(f"{OUT.relative_to(ROOT)} を作りました（{names}）")


if __name__ == "__main__":
    main()

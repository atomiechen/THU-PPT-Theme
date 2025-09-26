"""
Rename or show slide layouts in a PowerPoint file.

Requirements:
```sh
pip install python-pptx
```

Usage:
```
layouts.py [-h] {rename,show} input [output]

positional arguments:
  {rename,show}  Action to perform: 'rename' or 'show'
  input          Input PowerPoint file
  output         Output PowerPoint file (required for 'rename' action)

optional arguments:
  -h, --help     show this help message and exit
```

For example:
```sh
python3 layouts.py rename input.pptx output.pptx
```
"""

import argparse
from pathlib import Path
from pptx import Presentation


# 中文名 → 英文名 映射表
mapping = {
    "标题幻灯片": "Title Slide",
    "标题和内容": "Title and Content",
    "目录": "Content",
    "节标题": "Section Header",
    "两栏内容": "Two Content",
    "比较": "Comparison",
    "仅标题": "Title Only",
    "空白": "Blank",
    "内容与标题": "Content with Caption",
    "图片与标题": "Picture with Caption",
    "标题和竖排文字": "Title and Vertical Text",
    "竖排标题与文本": "Vertical Title and Text",
}


def rename_layouts(input_pptx: str, output_pptx: str):
    # print(f"Renaming layouts in: '{input_pptx}'")
    p = Path(input_pptx)
    with p.open("rb") as fin:
        prs = Presentation(fin)
        for layout in prs.slide_layouts:
            name = layout.name  # 现有布局名
            if name in mapping:
                new_name = mapping[name]
                try:
                    layout.name = new_name
                    print(f"Renamed '{name}' to '{new_name}'")
                except Exception as e:
                    print(f"Failed to set name for layout '{name}': {e}")
            else:
                print(f"Skipped '{name}'")
        prs.save(output_pptx)


def show_layouts(input_pptx: str):
    # print(f"Showing layouts in: '{input_pptx}'")
    p = Path(input_pptx)
    with p.open("rb") as fin:
        prs = Presentation(fin)
        for layout in prs.slide_layouts:
            print(layout.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename or show slide layouts in a PowerPoint file.")
    parser.add_argument("action", choices=["rename", "show"], help="Action to perform: 'rename' or 'show'")
    parser.add_argument("input", help="Input PowerPoint file")
    parser.add_argument("output", nargs="?", help="Output PowerPoint file (required for 'rename' action)")
    args = parser.parse_args()
    
    if args.action == "rename":
        if not args.output:
            parser.error("the 'rename' action requires an output file")
        rename_layouts(args.input, args.output)
    elif args.action == "show":
        show_layouts(args.input)

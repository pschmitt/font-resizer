#!/usr/bin/env python
# coding: utf-8

import argparse
import os

import fontforge


def scale_line_height(font_path, scale_factor):
    try:
        # Open the font
        font = fontforge.open(font_path)

        # Scale the OS/2 metrics
        font.os2_typoascent = int(font.os2_typoascent * scale_factor)
        font.os2_typodescent = int(font.os2_typodescent * scale_factor)
        font.os2_typolinegap = int(font.os2_typolinegap * scale_factor)

        # Scale the hhea metrics
        font.hhea_ascent = int(font.hhea_ascent * scale_factor)
        font.hhea_descent = int(font.hhea_descent * scale_factor)
        font.hhea_linegap = int(font.hhea_linegap * scale_factor)

        # Construct new file path
        dir_name, file_name = os.path.split(font_path)
        name, ext = os.path.splitext(file_name)
        modified_font_path = os.path.join(dir_name, f"{name}-resized{ext}")

        # Save the modified font
        font.generate(modified_font_path)

    except Exception as e:
        print(f"An error occurred with {font_path}: {e}")

    finally:
        font.close()
        return modified_font_path


def main():
    parser = argparse.ArgumentParser(
        description="Scale the line height of multiple fonts."
    )
    parser.add_argument(
        "font_paths", nargs="+", help="Paths to the font files"
    )
    parser.add_argument(
        "--scale",
        type=float,
        required=True,
        help="Scale factor for line height (e.g., 1.3 to increase by 30%)",
    )

    args = parser.parse_args()

    for font_path in args.font_paths:
        modified_font_path = scale_line_height(font_path, args.scale)
        print(f"Scaled font saved as: {modified_font_path}")


if __name__ == "__main__":
    main()

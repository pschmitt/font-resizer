# 📏 font-resizer

font-resizer is a Python script that allows for easy scaling of
the line height in font files.

This tool is particularly useful for [Comic Code](https://tosche.net/fonts/comic-code)
users that are plagued with wrong line heights after patching their beloved font
using [NerdFonts-patcher](https://github.com/ryanoasis/nerd-fonts).

See issue: https://github.com/ryanoasis/nerd-fonts/issues/1165

## 🚀 Getting Started

Either:

- Python 3.10+
- [FontForge](https://fontforge.org/en-US/) and its Python bindings

**or**: `docker`/`podman`

## 💥 Usage

For scaling the line height to `80%` of the original size:

```shell
docker run -it --rm \
  -v "$PWD/myfonts:/fonts" \
  pschmitt/font-resizer \
  --scale 0.8 \
  /fonts/ComicCodeNerdFont-Regular.otf \
  /fonts/ComicCodeLigaturesNerdFont-Regular.otf
```

This should produce the following files in your `myfonts/` directory:

- ComicCodeNerdFont-Regular-resized.otf
- ComicCodeLigaturesNerdFont-Regular-resized.otf

## 🖋️ License

This project is licensed under the GNU General Public License v3.0 -
see the [LICENSE](./LICENSE) file for details.

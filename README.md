# MagicInjection  
**Inject magic bytes into files to bypass basic file upload security mechanisms.**

![License](https://img.shields.io/badge/license-MIT-green.svg)  
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

---

## Description

**MagicInjection** is a simple Python tool that injects *magic bytes* into files to trick file type validation mechanisms, often used in insecure file upload filters. This technique is commonly used to bypass poorly implemented file upload restrictions by mimicking headers of legitimate file types.

> ⚠️ This tool is intended for **educational purposes** and **authorized security testing** only.

---

## Supported File Types

The following file signatures (magic bytes) are supported:

| Format | Description           |
|--------|-----------------------|
| `7z`   | 7-Zip archive         |
| `doc`  | Microsoft Word (legacy `.doc`) |
| `gif`  | Graphics Interchange Format |
| `jpeg` | JPEG image            |
| `mp3`  | MPEG Layer III Audio  |
| `pdf`  | Portable Document Format |
| `png`  | Portable Network Graphics |
| `rar`  | RAR archive           |
| `xml`  | XML file              |
| `zip`  | ZIP archive           |

---

## Example Usage

Injecting PNG magic bytes into a PHP file:

```bash
└─$ ./MagicInjection.py badfile.php png
Writing magic bytes for 'png' to --> 'badfile.php'...
Done!
```

Now check the file type:

```bash
└─$ file badfile.php
badfile.php: PNG image data, 0 x 0, 0-bit grayscale, non-interlaced
```

The file now passes as a PNG image despite having `.php` extension, which might help bypass certain upload filters.

---

## 📦 Installation

Clone the repo and run the script using Python 3:

```bash
git clone https://github.com/yourusername/MagicInjection.git
cd MagicInjection
chmod +x MagicInjection.py
./MagicInjection.py <filename> <filetype>
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

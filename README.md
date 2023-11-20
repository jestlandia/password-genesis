 <h1 align='center'>🔒 Password Genesis 🔒</h1>

<p align="center">
  <img src="password-genesis.png" alt="password-genesis.png" width="500" style="display: block; margin: 0 auto;">
</p>

![GitHub last commit](https://img.shields.io/github/last-commit/jestlandia/password-genesis)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/jestlandia/password-genesis)
![GitHub stars](https://img.shields.io/github/stars/jestlandia/password-genesis?style=social)

## 🛡️ About

Password Genesis is a versatile Python-based password generator, offering a variety of character sets for highly customizable password creation. This project includes two main scripts:
- `ascii_password.py`: For generating passwords with ASCII characters.
- `unicode_password.py`: For generating passwords with Unicode characters.

## 💻 Installation

1. Clone the repository:
   ```
   git clone https://github.com/jestlandia/password-genesis.git
   ```
2. Navigate to the cloned directory:
   ```
   cd password-genesis/password_creation
   ```

## 🛠️ Usage

To generate a password, navigate to the `password_creation` directory and run one of the scripts with your desired parameters.

- ### ASCII Password Generator

```bash
python ascii_password.py [length] [options]
```
<details>
  <summary><b>Options:</b></summary>
 
| Option | Description |
| ------ | ----------- |
| `-u, --uppercase` | Include uppercase letters. |
| `-l, --lowercase` | Include lowercase letters. |
| `-d, --digits` | Include digits. |
| `-s, --special` | Include special characters. |
| `-e, --emojis` | Include emojis. |
| `-mu, --max_uppercase [int]` | Maximum number of uppercase characters. |
| `-ml, --max_lowercase [int]` | Maximum number of lowercase characters. |
| `-md, --max_digits [int]` | Maximum number of digits. |
| `-ms, --max_special [int]` | Maximum number of special characters. |
| `-me, --max_emojis [int]` | Maximum number of emojis. |

</details> 

- ### Unicode Password Generator

```bash
python unicode_password.py [length] [options]
```
<details>
  <summary><b>Options:</b></summary>
 
| Option | Description |
| ------ | ----------- |
| `-u, --uppercase` | Include uppercase letters. |
| `-l, --lowercase` | Include lowercase letters. |
| `-d, --digits` | Include digits. |
| `-s, --special` | Include special characters. |
| `-m, --math` | Include special characters. |
| `-e, --emojis` | Include emojis. |
| `-mu, --max_uppercase [int]` | Maximum number of uppercase characters. |
| `-ml, --max_lowercase [int]` | Maximum number of lowercase characters. |
| `-md, --max_digits [int]` | Maximum number of digits. |
| `-ms, --max_special [int]` | Maximum number of special characters. |
| `-mm, --max_math [int]` | Maximum number of special characters. |
| `-me, --max_emojis [int]` | Maximum number of emojis. |

</details> 

## 🌟 Examples

- Generate a 12-character ASCII password with a mix of upper/lowercase letters, digits, special characters, and emojis:
  ```bash
  python ascii_password.py 12 -uldse
  ```
- Generate a 16-character ASCII password with uppercase letters and digits, using a maximum of 5 digits:
  ```bash
  python ascii_password.py 16 -ud -md 5
  ```
- Generate an 8-character password with only emojis:
  ```bash
  python ascii_password.py 8 -e
  ```
- Generate a 20-character UNICODE password with lowercase letters, digits, special characters, and math characters, using a maximum of 3 special characters:
  ```bash
  python unicode_password.py 20 -ldsm -ms 3
  ```

## 🔒 Security

This tool generates strong and complex passwords, contributing to better security in your digital life. 

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/jestlandia/password-genesis/issues) for open issues or submit a new one.

## ⭐ Show your support

Give a ⭐️ if this project helped you!

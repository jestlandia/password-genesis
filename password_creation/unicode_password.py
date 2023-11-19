import random
import unicodedata
import argparse

class PasswordGenerator:
    def __init__(self, length=12, uppercase=True, lowercase=True, digits=True, special=True, math=True, emojis=True, 
                 max_uppercase=None, max_lowercase=None, max_digits=None, max_special=None, max_math=None, max_emojis=None):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.digits = digits
        self.special = special
        self.math = math
        self.emojis = emojis
        self.max_uppercase = max_uppercase
        self.max_lowercase = max_lowercase
        self.max_digits = max_digits
        self.max_special = max_special
        self.max_math = max_math
        self.max_emojis = max_emojis

    def generate_password(self):
        characters = ""
        
        def add_characters(char_set, max_count):
            return ''.join(random.choice(char_set) for _ in range(max_count)) if max_count is not None else char_set
    
        if self.uppercase:
            uppercase_letters = ''.join(chr(i) for i in range(0x41, 0x5B) if unicodedata.category(chr(i)) == 'Lu')
            uppercase_chars = add_characters(uppercase_letters, self.max_uppercase)
            characters += uppercase_chars
        if self.lowercase:
            lowercase_letters = ''.join(chr(i) for i in range(0x61, 0x7B) if unicodedata.category(chr(i)) == 'Ll')
            lowercase_chars = add_characters(lowercase_letters, self.max_lowercase)
            characters += lowercase_chars
        if self.digits:
            digits = ''.join(chr(i) for i in range(0x30, 0x3A) if unicodedata.category(chr(i)) == 'Nd')
            digit_chars = add_characters(digits, self.max_digits)
            characters += digit_chars
        if self.special:
            uppercase_special_letters = ''.join(chr(i) for i in range(0x5B, 0x10000) if unicodedata.category(chr(i)) == 'Lu')
            lowercase_special_letters = ''.join(chr(i) for i in range(0x7B, 0x10000) if unicodedata.category(chr(i)) == 'Ll')
            special_characters = uppercase_special_letters + lowercase_special_letters
            special_chars = add_characters(special_characters, self.max_special)
            characters += special_chars
        if self.math: 
            fullwidth_digits = ''.join(chr(i) for i in range(0xFF10, 0xFF1A))
            all_digits = ''.join(chr(i) for i in range(0x3A, 0x10000) if unicodedata.category(chr(i)) == 'Nd')
            special_digits = ''.join(char for char in all_digits if char not in fullwidth_digits)
            math_symbols = ''.join(chr(i) for i in range(0x2200, 0x2300) if unicodedata.category(chr(i)) == 'Sm')            
            special_math_characters = special_digits + math_symbols
            special_math_chars = add_characters(special_math_characters, self.max_math)
            characters += special_math_chars
        if self.emojis: 
            emoji_str = "😂❤️🤣👍😭🙏😘🥰😍😊🎉😁💕🥺😅🔥☺️🤦♥️🤷🙄😆🤗😉🎂🤔👏🙂😳🥳😎👌💜😔💪✨💖👀😋😏😢👉💗😩💯🌹💞🎈💙😃😡💐😜🙈🤞😄🤤🙌🤪❣️😀💋💀👇💔😌💓🤩🙃😬😱😴🤭😐🌞😒😇🌸😈🎶✌️🎊🥵😞💚☀️🖤💰😚👑🎁💥🙋☹️😑🥴👈💩✅👋🤮😤🤢🌟❗😥🌈💛😝😫😲🖕‼️🔴🌻🤯💃👊🤬🏃😕👁️⚡☕🍀💦⭐🦋🤨🌺😹🤘🌷💝💤🤝🐰😓💘🍻😟😣🧐😠🤠😻🌙😛🤙🙊"
            emoji_chars = add_characters(emoji_str, self.max_emojis)
            characters += emoji_chars
        # Check if at least one character set is selected
        if not characters:
            raise ValueError("At least one character set must be selected")
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(self.length))
        print("Generated Password:", password)
        return password


def main(): 
    parser = argparse.ArgumentParser(description='Insert data from JSON files into an existing SQLite table')

    parser.add_argument('length', type=int, default=12, help='Length of password')
    parser.add_argument('-u', '--uppercase', action='store_true', help="Include uppercase letters")
    parser.add_argument('-l', '--lowercase', action='store_true', help="Include lowercase letters")
    parser.add_argument('-d', '--digits', action='store_true', help="Include digits")
    parser.add_argument('-s', '--special', action='store_true', help="Include special characters")
    parser.add_argument('-m', '--math', action='store_true', help="Include math special characters")
    parser.add_argument('-e', '--emojis', action='store_true', help="Include emojis")
    parser.add_argument('-mu', '--max_uppercase', type=int, default=None, help="Maximum number of uppercase characters")
    parser.add_argument('-ml', '--max_lowercase', type=int, default=None, help="Maximum number of lowercase characters")
    parser.add_argument('-md', '--max_digits', type=int, default=None, help="Maximum number of digits")
    parser.add_argument('-ms', '--max_special', type=int, default=None, help="Maximum number of special characters")
    parser.add_argument('-mm', '--max_math', type=int, default=None, help="Maximum number of math symbols")
    parser.add_argument('-me', '--max_emojis', type=int, default=None, help="Maximum number of emojis")


    args = parser.parse_args()
    
    password_generator = PasswordGenerator(args.length, args.uppercase, args.lowercase, args.digits, args.special, args.math, args.emojis, 
                                           args.max_uppercase, args.max_lowercase, args.max_digits, args.max_math, args.max_special, args.max_emojis)
    password_generator.generate_password()
    
if __name__ == "__main__":
    main()

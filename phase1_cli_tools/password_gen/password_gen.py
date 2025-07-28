import random
import string

print("パスワード生成アプリ")

try:
    length = int(input("パスワードの長さを入力してください（例：12）: "))
    
    # 各文字種の使用有無を確認
    use_lower = input("英小文字を含めますか？(y/n): ").lower() == 'y'
    use_upper = input("英大文字を含めますか？(y/n): ").lower() == 'y'
    use_digits = input("数字を含めますか？(y/n): ").lower() == 'y'
    use_symbols = input("記号を含めますか？(y/n): ").lower() == 'y'

    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("エラー：最低1つの文字種を選んでください。")
    elif length < 4:
        print("4文字以上を推奨します。")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        print("生成されたパスワード:", password)

except ValueError:
    print("数字を入力してください。")

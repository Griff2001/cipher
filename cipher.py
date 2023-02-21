SYMBOLS = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'

print('the caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Let the user decide if they are encrypting or decrypting:
while True:  # keep asking until the user enters e or d:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
        print('kindly enter the letter e or d.')

        # let the user enter the key to use:
while True:  # keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print('please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('>').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# let the user enters the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('>')
# the cipher will only function in uppercase letters:
message = message.upper()

# stores the encrypted or the decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)  # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

            # Handle the wrap-around if num is larger than the length of
            # SYMBOLS or less than 0:
            if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

            # Add encyrypted/decrypted number's symbol to be translated:
            translated = translated + symbol
# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard .'.format(mode))
except:
    pass  # Do nothing if pyperclip wasn't installed.

alphabet = "abcdefghijklmnopqrstuvwxyz"
newMessage = ''

message = input('Please, enter your s-message: ')

key = input('Enter s-key: ')
key = '-' + key
key = int(key)

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) %26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print('Your s-message is: ', newMessage)
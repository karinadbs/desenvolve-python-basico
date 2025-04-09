import emoji

emojis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print('Emojis disponíveis: ')
for texto, emoji in emojis.items():
    print(f"{emoji} - {texto}")

frase = input('Digite uma frase e ela será emojizada: ')

frase_emojizada = frase
for texto, emoji in emojis.items():
    frase_emojizada = frase_emojizada.replace(texto, emoji)

print('Frase emojizada: ')
print(frase_emojizada)
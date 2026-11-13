
#fun game using dictionary
def build_emoji_dict():
    emoji_dict = {}
    word = input("Word: ").lower()

    while word != "":
        emoji = input(f"Emoji for {word}: ")
        emoji_dict[word] = emoji
        word = input("Word: ").lower()

    print("Words in your dictionary:", len(emoji_dict))
    return emoji_dict

def print_emoji_dict(emoji_dict):
    for key in emoji_dict:
        print(f"{key}:",emoji_dict[key])
def translate(sentence, emoji_dict):
    result = ""
    for word in sentence.split():
        if word.lower() in emoji_dict:
          result+= emoji_dict[word.lower()]
        else:
            result+=word  
        result += " " 

    return result       
def main():
    print("Let's build your emoji dictionary! Press enter when you are done.")

    emoji_dict = build_emoji_dict()
    print_emoji_dict(emoji_dict)

    sentence = input("Enter a sentence: ")

    while sentence != "":
        translated = translate(sentence, emoji_dict)
        print(translated)
        sentence = input("Enter a sentence: ")
if __name__ == "__main__":
    main()
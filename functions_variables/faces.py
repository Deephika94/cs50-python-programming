
def convert(text):
    text = text.replace(":)","😊")
    text = text.replace(":(","☹️")
    print(text)

def main():
    greet = input()
    convert(greet)

main()

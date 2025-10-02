emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = "o.o"
    say("Oh, hi!")
    emoticon = "-.-"
    say("Goodbye.")
    
def say(phrase):
    print(phrase + " " + emoticon)

main()
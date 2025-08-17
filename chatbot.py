from datetime import datetime
def replymessage(msg: str)->str:
    if msg in("Hi","Hlo","yo","Hey"):
        return "Hi there!"
    elif msg in("How are you","Are you ok"):
        return "I am fine"
    elif msg in("Bye","See you"):
        return "Good Bye"
    elif msg in("thank you","thanks","thanks a lot"):
        return "You are welcome"
    elif msg in("help","What can you do"):
        return "I can tell you jokes, show the time,chat with you over simple thing"
    elif msg in("what day is it","what is the date","what is the day"):
        today=datetime.now().strftime("%A, %d%b%y")
        return f"Today is {today}."
    elif msg in("what is the time"):
        now=datetime.now().strftime("%I:%M%p").lstrip("0")
        return f"It is {now}."
def main():
    print("-----CHATBOT----\nType exit anytime to quit")
    while True:
        user=input("you:\n")
        if(user=="exit"):
            print("Good Bye")
            break
        reply=replymessage(user)
        print("BOT:",reply)
main()
    

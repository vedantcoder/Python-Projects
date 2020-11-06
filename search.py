import wikipedia
while True:
    my_input = input("")
    print(wikipedia.summary(my_input, sentences=2))

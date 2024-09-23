# return list of answers

def read():
    questions = []
    with open("./questions.txt", "r") as f:
        for x in f:
            questions.append(x)
    return questions

if __name__ == "__main__":
    print(read())
class Pair:
    def __init__(self, word, times):
        self.word = word
        self.times = times

    def __repr__(self):
        return "Pair - Word: % s - Times: % s" % (self.word, self.times)


prompt = ["MARK ZUCKERBERG is a sweet looking 19 year old whose lack of "
          "any physically intimidating attributes masks a very "
          "complicated and dangerous anger. He has trouble making eye "
          "contact and sometimes it’s hard to tell if he’s talking to you"
          " or to himself "
          "ERICA, also 19, is Mark’s date. She has a girl-next-door face "
          "that makes her easy to fall for. At this point in the "
          "conversation she already knows that she’d rather not be there "
          "and her politeness is about to be tested. "
          "The scene is stark and simple. "
          "MARK "
          "How do you distinguish yourself in a "
          "population of people who all got 1600 on "
          "their SAT’s? "
          "ERICA "
          "I didn’t know they take SAT’s in China."
          "MARK "
          "They don’t. I wasn’t talking about China"
          " anymore, I was talking about me. ERICA You got 1600? MARK "]

res = []
for wrd in prompt:
    words = wrd.split()
for wd in words:
    if wd not in res:
        res.append(wd)
print("All the words found in the prompt are: ", res)
for w in res:
    pair = Pair(w, words.count(w))
    print(pair)


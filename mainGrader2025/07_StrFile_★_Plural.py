word = input()

if word[-1] in ["s", "x"] or word[-2::] == "ch":
	word = word + "es"
elif word[-1] == "y" and word[-2] not in ["a", "e", "i", "o", "u"]:
	word = word[:-1] + "ies"
else: word = word + "s"

print(word)
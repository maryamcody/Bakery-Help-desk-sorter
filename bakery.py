
URGENT_WORDS = {
    "refund": 3, "broken": 3, "late": 2,
    "missing": 2, "wrong": 2, "cancel": 2,
    "never": 2, "again": 1, "now": 1,
}

THRESHOLD = 4
PUNCTUATION = ".,!?:;\"'()"

TEST_MESSAGES = [
    ("My cake arrived broken and I want a refund now!", "URGENT"),
    ("The delivery is late again, and my order is missing", "URGENT"),
    ("Thank you, the cupcakes were delicious", "NORMAL"),
    ("Do you sell gluten free bread?", "NORMAL"),
    ("Can I cancel my order? I ordered the wrong size", "URGENT"),
    ("I never had a late delivery before, great service!", "NORMAL"),
]


def tokenize(message):
    words = []

    for word in message.split():
        cleaned = word.lower().strip(PUNCTUATION)

        if cleaned:
            words.append(cleaned)

    return words


print("PART 1: Clean words")
print(tokenize("Where is my REFUND?!"))


def urgency_score(message):
    score = 0

    for word in tokenize(message):
        score += URGENT_WORDS.get(word, 0)

    return score


print("\nPART 2: Score")
print(urgency_score(
    "My cake arrived broken and I want a refund now!"
))



def label(message):
    if urgency_score(message) >= THRESHOLD:
        return "URGENT"

    return "NORMAL"


print("\nPART 3: Label")
print(label("Thank you, the cupcakes were delicious"))


print("\nPART 4: Test all messages")

mistakes = 0

for number, (message, expected) in enumerate(TEST_MESSAGES, start=1):
    score = urgency_score(message)
    result = label(message)

    if result != expected:
        mistakes += 1

    print("\nMessage", number)
    print("Text:", message)
    print("Urgency Score:", score)
    print("Expected:", expected)
    print("Result:", result)

    if result == expected:
        print("Status: CORRECT")
    else:
        print("Status: INCORRECT")

    print("-" * 40)


print("\nFINAL SUMMARY")
print("Total Messages:", len(TEST_MESSAGES))
print("Correct Answers:", len(TEST_MESSAGES) - mistakes)
print("Mistakes:", mistakes)

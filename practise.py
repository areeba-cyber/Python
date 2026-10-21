# functions
def greet (name, greet="Hello"):
    print(f"{greet} My name is {name}")
greet("Ali")
greet("Areeba", greet="Hi")

# Parameters are the names in the definition. Arguments are the values you pass in.
# A function without return gives back None.
# *args collects extra positional arguments into a tuple, and **kwargs collects extra keyword arguments into a dict


1. Stats function: Write `describe(numbers)` that returns the minimum, maximum, and average of a list. Call it and unpack the three results into separate variables.

2. Default and keyword parameters: Write `make_email(name, domain="example.com")` that returns a lowercase email like `sara.khan@example.com` from `"Sara Khan"`. Call it once with the default domain and once with a keyword argument.

3. Remove duplicates, keep order: Given `[3, 1, 3, 2, 1, 5]`, write a function that returns a new list with duplicates removed while keeping the original order. Using a set will help, but a set alone won’t preserve order.

4. Set operations: Two students’ course lists are `{"math", "physics", "art"}` and `{"art", "history", "math"}`. Print the courses they share, the courses only the first takes, and all courses combined.

5. Word counter: Write `count_words(text)` that returns a dictionary mapping each word to how many times it appears, ignoring case. Then print the word that appears most often.


1.
def describe(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = describe([4, 8, 15, 16, 23, 42])
print(low, high, avg)   # 4 42 18.0

2.
def make_email(name, domain="example.com"):
    return name.lower().replace(" ", ".") + "@" + domain

print(make_email("Sara Khan"))                    # sara.khan@example.com
print(make_email("Sara Khan", domain="uni.edu"))  # sara.khan@uni.edu

3.
def dedupe(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(dedupe([3, 1, 3, 2, 1, 5]))   # [3, 1, 2, 5]

4.
a = {"math", "physics", "art"}
b = {"art", "history", "math"}

print(a & b)   # shared: {'math', 'art'}
print(a - b)   # only first: {'physics'}
print(a | b)   # all combined: {'math', 'physics', 'art', 'history'}

5.
def count_words(text):
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts

text = "The cat saw the dog. The dog saw the cat!"
counts = count_words(text)
print(counts)   # {'the': 4, 'cat': 2, 'saw': 2, 'dog': 2}

most_common = max(counts, key=counts.get)
print(most_common)   # the
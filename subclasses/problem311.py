text = input("Enter multiple sentences: ")

sentences = [s.strip() for s in text.split(".") if s.strip()]

if sentences:
    longest = max(sentences, key=len)
    print("Longest sentence:", longest)
    print("Length:", len(longest))
else:
    print("No sentences found")
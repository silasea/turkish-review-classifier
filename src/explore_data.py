from datasets import load_dataset

ds = load_dataset("turkish-nlp-suite/MusteriYorumlari")

print("Splits:", ds)
print()

train = ds["train"]
print("Train size:", len(train))
print()
for i in range(5):
    print(train[i])
print()

from collections import Counter
labels = Counter(train["label"])
print("Label distribution:", sorted(labels.items()))
import json
from collections import Counter

def read_json(file_path, word_min_len=6, top_words_amt=10):
    with open(file_path, encoding = "utf-8") as f:
        json_data = json.load(f)

        words = []
        for item in json_data["rss"]["channel"]["items"]:
            description = item["description"]
            words.extend(description.split())

        word_counts = Counter(words)

        top_words = []
        for word, count in word_counts.most_common():
            if len(word) > word_min_len:
                top_words.append(word)
                if len(top_words) >= top_words_amt:
                    break

       
    return top_words


if __name__ == '__main__':
    print(read_json('newsafr.json'))
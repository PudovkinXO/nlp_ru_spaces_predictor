import random
import pandas as pd

df_news = pd.read_csv('news.csv')
df_sentences = pd.read_csv('sentences.csv')

actions = ["куплю", "продам", "сдам", "ищу", "отдам", "срочноотдам"]
objects = [
    "айфон", "телефон" "ноутбук", "телевизор", "диван", "стиральнуюмашину", "квартиру", 
    "комнату", "велосипед", "микроволновку", "машину", "холодильник", "пылесос", "работу", "работника", "кроссовки", "кеды"
]
brands = [
    "", "Samsung", "LG", "Philips", "HP", "Apple", "Xiaomi", "Huawei", 
    "Playstation5", "XboxOne", "Lenovo", "Mac", "Canon", "Fender", "Merida", "Nike", "Reebook"
]
numbers = ["", "13", "14", "15", "27дюймов", "70литров", "про"]
suffixes = ["", "доставка", "недорого", "бу", "срочно", "удаленно"]

def generate_sentence():
    action = random.choice(actions) 
    obj = random.choice(objects) 
    brand = random.choice(brands) 
    number = random.choice(numbers)  
    suffix = random.choice(suffixes) 

    words = [action, obj, brand, number, suffix]
    sentence = ' '.join([w for w in words if w])
    return sentence

def make_dataset(n_samples):
    input_texts = []
    labels_list = []

    for _ in range(n_samples):
        sent = generate_sentence()

        input_text = ''.join(sent.split())
        input_texts.append(input_text)

        labels = []
        j = 0
        for word in sent.split():
            for i, ch in enumerate(word):
                if j == 0:
                    labels.append(0)
                else:
                    labels.append(1 if i == 0 else 0)
                j += 1
        labels_list.append(labels)

    for num in range(4750):
        raw_text = str(df_news['text'][num].strip())
        sentences = [s.strip() for s in raw_text.split('. ') if s.strip()]
        for sent in sentences:
            input_text = ''.join(sent.split())
            input_texts.append(input_text)

            labels = []
            j = 0
            for word in sent.split():
                for i, ch in enumerate(word):
                    if j == 0:
                        labels.append(0)
                    else:
                        labels.append(1 if i == 0 else 0)
                    j += 1
            labels_list.append(labels)
    
    for sent in df_sentences['sentence']:
        input_text = ''.join(sent.split())
        input_texts.append(input_text)

        labels = []
        j = 0
        for word in sent.split():
            for i, ch in enumerate(word):
                if j == 0:
                    labels.append(0)
                else:
                    labels.append(1 if i == 0 else 0)
                j += 1
        labels_list.append(labels)

    df = pd.DataFrame({"input_text": input_texts, "labels": labels_list})
    return df

if __name__ == "__main__":
    df = make_dataset(n_samples=10000)
    df.to_csv("train_data.csv", index=False, encoding="utf-8")
    print(f'train_data.csv generated with {len(df)} samples')
    
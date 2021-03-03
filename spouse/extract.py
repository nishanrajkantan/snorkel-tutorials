import pickle

with open("data/dev_data.pkl", "rb") as f:
    dev_data = pickle.load(f)

with open("data/test_data.pkl", "rb") as f:
    test_data = pickle.load(f)

with open("data/train_data.pkl", "rb") as f:
    train_data = pickle.load(f)

dev_data.to_csv("dev_data.csv")
test_data.to_csv("test_data.csv")
train_data.to_csv("train_data.csv")
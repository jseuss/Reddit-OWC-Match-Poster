import pickle
with open("members.pkl", "rb") as f:
    members = pickle.load(f)
print(len(members))
print(members["Philippines"])
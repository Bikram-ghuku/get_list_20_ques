import requests
x = requests.get("https://opentdb.com/api.php?amount=20")
ques = []
ans=[]
for data in x.json()["results"]:
  f=[]
  f.append(data["correct_answer"])
  for s in data["incorrect_answers"]:
    f.append(s)
  ans.append(f)
  ques.append(data["question"])
print(ques)
print(ans)

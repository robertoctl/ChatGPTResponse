from openai import OpenAI

client = OpenAI(api_key="")


question = input("What would you like to ask ChatGPT? ")

response = client.completions.create(model="text-davinci-003",
prompt=question,
max_tokens=1024,
n=1,
stop=None,
temperature=0.8)

answer = response.choices[0].text

print(answer)
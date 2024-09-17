from openai import OpenAI

client = OpenAI(
   api_key= "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",
     
)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a about coding."
        }
    ]
)

print(completion.choices[0].message)
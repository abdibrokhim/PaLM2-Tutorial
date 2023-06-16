import pprint
import google.generativeai as palm

palm.configure(api_key='YOUR_API_KEY')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

print(model)

prompt = """
You are an expert at solving word problems.

Solve the following problem:

I have three houses, each with three cats.
each cat owns 4 mittens, and a hat. Each mitten was
knit from 7m of yarn, each hat from 4m.
How much yarn was needed to make all the items?

Think about it step by step, and show your work.
"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # candidate_count=8,  # The number of candidates to return
    temperature=1.0,  # Set the temperature to 1.0 for more variety of responses.
    max_output_tokens=800,  # The maximum length of the response
)

print(completion.result)




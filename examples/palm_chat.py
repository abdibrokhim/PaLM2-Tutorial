import google.generativeai as palm

palm.configure(api_key='PALM_KEY')


# Create a new conversation
response = palm.chat(messages='Hello')

# Last contains the model's response:
response.last


# Add to the existing conversation by sending a reply
response = response.reply("Just chillin'")
# See the model's latest response in the `last` field:
response.last

response.messages  # See the full conversation history

# Create a brand new chat with candidate_count = 4.
response = palm.chat(messages="What should I eat for dinner tonight? List a few options", candidate_count = 4)
# See the model's default response
response.last

# See alternate possible model responses
response.candidates

response.last = response.candidates[2]  # Set the last message to the third candidate


# Setting temperature=1 usually produces more zany responses!
response = palm.chat(messages="What should I eat for dinner tonight? List a few options", temperature=1)
response.last


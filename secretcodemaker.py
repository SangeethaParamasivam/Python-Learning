'''*Secret Code Maker: Day 6 Python Assignment*
*Description*
You are a secret agent who needs to send coded messages to your partner. You need to write a simple program that can take normal text and turn it into a secret code.
*Task*
1. Create a variable called `agent_name` with your name (or any name you choose)
2. Create a variable called `secret_message` with a short message like "Meet me at the park"
3. Create your coded message by:
   - Converting the message to uppercase
   - Replacing all spaces with "#"
   - Adding the agent name at the end, separated by "007"
4. Print the original message and the coded message
*Example*
If your variables are:
```python
agent_name = "Alex"
secret_message = "Meet me at the park"
```
Your output should be:
```
Original message: Meet me at the park
Coded message: MEET#ME#AT#THE#PARK007ALEX
*Bonus* (Optional)
Convert the number of characters in your original message to a string and add it to the beginning of your coded message.
Example with bonus:
```
Original message: Meet me at the park
Coded message: 19#MEET#ME#AT#THE#PARK007ALEX
'''


# Define variables
agent_name = "Alex"  # Change this to any name
secret_message = "Meet me at the park"  # Change this to any message

# Encode the message
coded_message = secret_message.upper().replace(" ", "#") + "007" + agent_name

# Bonus: Add the length of the original message
coded_message_with_length = str(len(secret_message)) + "#" + coded_message

# Print results
print("Original message:", secret_message)
print("Coded message:", coded_message)
print("Coded message with bonus:", coded_message_with_length)

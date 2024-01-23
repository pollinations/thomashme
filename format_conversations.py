import json

def transform_and_sort_conversation(input_file_path, output_file_path):
    # Load and parse the JSON data from the file
    with open(input_file_path, 'r') as file:
        data = json.load(file)

    # Sort the data by timestamp before processing
    data.sort(key=lambda x: x['timestamp'])

    conversation_dict = {}
    total_messages = 0

    # Grouping messages by conversationId
    for msg in data:
        conversation_id = msg['conversationId']
        if conversation_id not in conversation_dict:
            conversation_dict[conversation_id] = []
            # Append the system message at the start of each conversation
            conversation_dict[conversation_id].append({"role": "system", "content": "This GPT is designed to impersonate Thomas Haferlach a unique individual with a rich, multifaceted background."})
        role = 'assistant' if msg['senderName'] == 'Thomas Haferlach' else 'user'
        conversation_dict[conversation_id].append({"role": role, "content": msg['text']})
        total_messages += 1

    # Formatting each conversation
    for conversation_id, messages in conversation_dict.items():
        formatted_messages = [msg for msg in messages]  # Extract formatted message
        # Saving the transformed data to a new JSONL file
        with open(output_file_path, 'a') as file:
            json.dump({"messages": formatted_messages}, file)
            file.write('\n')

    # Print the number of conversations and the total number of messages
    print(f"Number of conversations: {len(conversation_dict)}")
    print(f"Total number of messages: {total_messages}")

# Example usage
input_file_path = 'chatistics_export.json'
output_file_path = 'gpt_conversations_small.jsonl'
transform_and_sort_conversation(input_file_path, output_file_path)

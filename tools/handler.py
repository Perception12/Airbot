import json
from tools.description import tool_dict

def handle_tool_calls(message):
    responses = []
    
    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        
        if tool_name not in tool_dict.keys():
            return "Unknown tool called"
        
        arguments = json.loads(tool_call.function.arguments)
        
        print(f"Handling tool call: {tool_name} with arguments {arguments}")
        
        response = tool_dict[tool_name](**arguments)
            
        responses.append(
            {
                "role": "tool",
                "content": response,
                "tool_call_id": tool_call.id
            }
        )
        
    return responses
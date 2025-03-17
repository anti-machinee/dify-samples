# CompletionApi

## Description
- Send a request to the text generation application.

## CURL (streaming)
```bash
curl -X POST 'http://localhost:5001/v1/completion-messages' \
--header 'Authorization: Bearer app-wVuFvKgGBJ8cgeCNEByWeRUZ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {"Target_code": "Java", "default_input": "def main(): return 1"},
    "response_mode": "streaming",
    "user": "abc-123"
}'
```

## Response
```bash
data: {"event": "message", "message_id": "35a68440-3766-40f8-9ce2-b79788072012", "created_at": 1740194075, "task_id": "f9fe6f2c-79c0-4cca-acc5-0bcc67e6cb47", "id": "35a68440-3766-40f8-9ce2-b79788072012", "answer": "public", "from_variable_selector": null}

.....

data: {
    "event": "message_end",
    "message_id": "35a68440-3766-40f8-9ce2-b79788072012",
    "created_at": 1740194075,
    "task_id": "f9fe6f2c-79c0-4cca-acc5-0bcc67e6cb47",
    "id": "35a68440-3766-40f8-9ce2-b79788072012",
    "metadata": {
        "usage": {
            "prompt_tokens": 66,
            "prompt_unit_price": "0.003",
            "prompt_price_unit": "0.001",
            "prompt_price": "0.0001980",
            "completion_tokens": 38,
            "completion_unit_price": "0.004",
            "completion_price_unit": "0.001",
            "completion_price": "0.0001520",
            "total_tokens": 104,
            "total_price": "0.0003500",
            "currency": "USD",
            "latency": 1.1430654770010733
        }
    },
    "files": null
}
```

## CURL (blocking)
```bash
curl -X POST 'http://localhost:5001/v1/completion-messages' \
--header 'Authorization: Bearer app-wVuFvKgGBJ8cgeCNEByWeRUZ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {"Target_code": "Java", "default_input": "def main(): return 1"},
    "response_mode": "blocking",
    "user": "abc-123"
}'
```

## Response
```bash
{
    "event": "message",
    "task_id": "aae3248f-2ea4-4853-adcc-9e9ec8901984",
    "id": "a2d1836c-798b-4567-9228-acd45165463d",
    "message_id": "a2d1836c-798b-4567-9228-acd45165463d",
    "mode": "completion",
    "answer": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(main());\n    }\n\n    public static int main() {\n        return 1;\n    }\n}",
    "metadata": {
        "usage": {
            "prompt_tokens": 66,
            "prompt_unit_price": "0.003",
            "prompt_price_unit": "0.001",
            "prompt_price": "0.0001980",
            "completion_tokens": 38,
            "completion_unit_price": "0.004",
            "completion_price_unit": "0.001",
            "completion_price": "0.0001520",
            "total_tokens": 104,
            "total_price": "0.0003500",
            "currency": "USD",
            "latency": 2.0427040780050447
        }
    },
    "created_at": 1740195083
}
```

## Analysis
- Authorize by token in api_tokens table

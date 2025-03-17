# AppQueueManager
- Self developed class
-

## Functions

## listen

## stop_listen

## publish_error

## publish

## _publish

## set_stop_flag
- Generate a Redis key associated with the task
- Fetch stored value for that key. The result is a byte object if the key exists
- Set expected user prefix
- Convert Redis stored value into a string. Check if it matches expected user prefix
- Generate a Redis key for the stop flag
- Store the key in Redis with value is 1 indiating stopped and be expried in 600 seconds

## _is_stopped

## _generate_task_belong_cache_key

## _generate_stopped_cache_key

## _check_for_sqlalchemy_models

# GenerateTaskStoppedError
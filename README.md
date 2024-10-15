# faux_processor

Fake application for learning and assessment purposes

Faux Processor is an AWS lambda that takes a JSON file location, and counts the number of items in a field named `to_process`.

It then writes this result to an API.

The triggering event takes the following form:

```JSON
{
    "file": "FILE_KEY_INCLUDING_PREFIX",
    "retry": true,
    "retry_attempts": 3
}
```

If `retry` is missing, it defaults to false.
If `retry_attempts` is missing, it defaults to 0.

# Assign Tags by Name Kata


## Try The API

You could try to use POST, PUT and PATCH methods for Post.

PATCH allows us to perform partial updates to a Post.

**Example:**

For Post with `id = 1` execute a PATCH method with following body:

```json
{
  "tag_names": [
    "django"
  ]
}
```

The result is:

```json
{
  "id": 1,
  "title": "Hello, World!",
  "body": "It's a lovely day, isn't it?",
  "author": 2,
  "created_at": "2024-07-30T17:43:39.442103Z",
  "updated_at": "2024-07-30T18:37:28.191484Z",
  "tags": [
    {
      "id": 3,
      "name": "django"
    }
  ]
}
```

Check also the tags:

```json
[
  {
    "id": 1,
    "name": "Tag 1"
  },
  {
    "id": 2,
    "name": "Tag 2"
  },
  {
    "id": 3,
    "name": "django"
  }
]
```

The `django` tag has been added automatically.




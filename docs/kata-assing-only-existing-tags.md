# Assign Only Exisisting Tags Kata

## Pre-requisites

* [Assign Tags by Name Kata](kata-assign-tags-by-name.md)

## Modify PostSerializser


```python
# posts/serializers.py
# .......

class PostSerializer(serializers.ModelSerializer):
    # ...........

    def validate_tag_names(self, value):
        existing_tags = Tag.objects.values_list('name', flat=True)
        invalid_tags = [name for name in value if name not in existing_tags]
        if invalid_tags:
            raise serializers.ValidationError(f"These tags do not exist: {', '.join(invalid_tags)}")
        return value

    # ..............

    def _save_tags(self, post, tag_names):
        tags = Tag.objects.filter(name__in=tag_names)
        post.tags.set(tags)

```

## Exploring the API

**Example:**

Update post with `id = 1` using PATCH method:

```json
{
  "tag_names": [
    "django", "beginner", "intermediate"
  ]
}
```

Results in validation error:

```json
{
  "tag_names": [
    "These tags do not exist: beginner, intermediate"
  ]
}
```

The `django` tag exists from earlier katas, but `beginner` and `intermediate` do not exist.

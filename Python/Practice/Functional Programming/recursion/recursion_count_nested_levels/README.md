# Count Nested Levels

In Doc2Doc, we might have documents nested inside other documents, forming a kind of tree. You know how crazy `.docx` files can get...

Anyways, we want to find out how deeply nested a given document is.

## Assignment

Complete the `count_nested_levels` function.

It should recursively search for the `target_document_id` in the `nested_documents` dictionary and return the number of nested levels of that document.

If the target document doesn't exist, the function should return `-1`.

## Example

In this dictionary, the document with id `3` is nested `2` levels deep.

```py
{
    1: {
        3: {}
    }
}
```
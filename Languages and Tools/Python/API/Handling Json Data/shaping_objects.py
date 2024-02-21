import json
from dataclasses import dataclass

@dataclass
class Owner:
    display_name: str
    link: str

@dataclass
class Item:
    title: str
    link: str
    owner: Owner

json_string = """
{
    "title": "Test Title",
    "link": "http://example.com",
    "owner": {
        "display_name": "Test User",
        "link": "http://example.com/user"
    }
}
"""

# Assuming `json_string` is a JSON string in the shape of the Item class
dict_obj = json.loads(json_string)

# Create an Owner instance from the owner dictionary
owner_dict = dict_obj.pop('owner')
owner_instance = Owner(**owner_dict)

# Now we can create an Item instance from the dictionary
item = Item(owner=owner_instance, **dict_obj)

print(item.title)
print(item.link)
print(item.owner.display_name)
print(item.owner.link)

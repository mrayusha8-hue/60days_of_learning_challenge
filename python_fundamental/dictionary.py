#dictionary-> collection of {key:value} pairs NO DUPLICATE

capitals={"Nepal": "Kathmandu","India": "Delhi","China": "Beijing"}

print(capitals.get("Nepal"))   #returns the value associated with the key "Nepal"

print(capitals.get("USA"))     #returns None if key is not found

capitals.update({"USA":"Washington DC"})  #adds a new key-value pair to the dictionary or append() also be used
print(capitals)

capitals.pop("India")          #removes the item with key "India"
print(capitals)

capitals.popitem()       #removes last item
print(capitals)

capitals.clear()         #removes all items
print(capitals)         #prints empty dictionary

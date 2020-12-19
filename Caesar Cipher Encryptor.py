def caesarcipherencryptor(string,key):
  result=[]
  key = key%26
  for letter in string:
    result.append(newletterkey(letter, key))
  return "".join(result)
def newletterkey(letter,key):
  newlettercode = ord(letter) + key
  return chr(newlettercode) if newlettercode <=122 else chr(96 + newlettercode%122)
print(caesarcipherencryptor('xyz',2))



O(n) Time and O(n) Space

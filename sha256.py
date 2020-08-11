import sys
import hashlib

filename = sys.argv
print("File: ", str(sys.argv[1]))
sha256 = hashlib.sha256()
with open(sys.argv[1], "rb") as file:

	for block in iter(lambda: file.read(4096), b""):
		sha256.update(block)
	print(sha256.hexdigest())

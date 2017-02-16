# Open the unsorted file, read into a list, and close it again.
f = open("url.txt")
lines = f.read().splitlines()
f.close()

print(len(lines))

f = open("out.txt", "w")
# Cycle through the list and pad left on each line to make them the same length.
# I could read these into an array of key-value pairs, true, and sort that.
# But this lets me take advantage of the built in sort() function, and lets
# me dump the sorted list to another file and read down it if I want, for fun.
for i in range(len(lines)):
	lines[i] = lines[i].strip(' ')
	while len(lines[i]) < 7: # The largest number is five digits, I know.
		lines[i] = "0" + lines[i]

lines.sort()

# Read down and figure out what this URL is!
url = ""
for line in lines:
	f.write(line + "\n")
	url += line[-1]		# Should I split the string instead? Sure. 
										# But I know what the data is in this case.

print(url)
f.close()


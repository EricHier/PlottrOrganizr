file = open("index.html", "r")
fileOutput = open("index_shortened.html", "w")

content = file.read()
content = content.replace("\\", "\\\\").replace("\n", "").replace("\"", "\\\"")

fileOutput.truncate(0)
fileOutput.write(content)
fileOutput.close()

file.close()

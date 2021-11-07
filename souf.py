import re

a_file = open("C:/Users/aze/Desktop/tp/sf.txt", "r", encoding="utf-8")

out = open("C:/Users/aze/Desktop/tp/res.txt", "w", encoding="utf-8")

for line in a_file.readlines():

   
    souf = re.findall("^KEYWORDS", line)
    clean = re.sub('<[^>]+>', ' ', line)
    if not souf and clean :
        #print(line)

        out.write(clean)

#out.write(clean)   
a_file.close()
out.close()
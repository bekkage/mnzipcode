
with open('zip') as f:
    lines = f.readlines()

skip = ['<a', '</a', 'span', 'ul', 'li']
codehtml = '<span class="list-zipcode">'

codes = {}
isUl = False

# CAN USE STACK HERE (FOR too many UL)

for i in range(0, len(lines)):
    if '<ul' in lines[i]:
        isUl = True

    if isUl:
        if codehtml in lines[i]:
            codes[lines[i-2].strip()] = lines[i].strip().replace(codehtml, '').replace('</span>', '')

print(codes)


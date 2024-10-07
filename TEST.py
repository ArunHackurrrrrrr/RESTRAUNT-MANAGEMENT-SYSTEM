# import ast

# with open('STAFF.txt','r') as readData:
#     bbc = readData.read()

#     kkc = f'({bbc})'
#     llc =kkc.replace('(','{')
#     nnc=llc.replace(')','}')
#     print(nnc)

#     dictk = ast.literal_eval(nnc)
#     # print(dictk.keys())

import ast

# Open and read the contents of STAFF.txt
with open('STAFF.txt', 'r') as readData:
    bbc = readData.read().strip()  # Strip any extra newlines or spaces

# Try to safely evaluate the content into a dictionary
try:
    dictk = ast.literal_eval(bbc)  # Converts string to dictionary
    print("Dictionary Keys:", dictk.keys())  # Print keys of the dictionary
except (SyntaxError, ValueError) as e:
    print(f"Error while converting string to dictionary: {e}")

    
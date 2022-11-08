import re

random_string = "friskmioshekFriskMioshekmioshekmioshekehsoimfriskksirfmioshekcostam...damnsk"

def regular_expression(patterns, phase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phase))
        
test_patterns = ['f[rm]+']

regular_expression(test_patterns,random_string)

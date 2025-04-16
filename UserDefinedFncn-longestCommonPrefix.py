*User - defined function assignment question* 

3. Write a function longest_common_prefix(words) that finds the longest common prefix among a list of words.
def longest_common_prefix(words):

    if not words:

        return ""

    prefix = words[0]

    for word in words[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if not prefix:

                return ""

    return prefix



print(longest_common_prefix(["flower", "flow", "flight"]))  

from fuzzywuzzy import fuzz, StringMatcher
import difflib
fuzz.SequenceMatcher = difflib.SequenceMatcher
print(fuzz.ratio("ababab", "aaaaab"))
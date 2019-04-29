# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(self, haystack, needle):
  lh,ln = len(haystack),len(needle)
  if ln == 0:
      return 0
  if ln >lh:
      return -1
  for i in range(0,lh-ln+1):
      if haystack[i:i+ln]==needle:
          return i
  return -1

import sys

N = int(sys.stdin.readline())

pattern_prefix, pattern_suffix = sys.stdin.readline().rstrip().split('*')

pattern_prefix_length = len(pattern_prefix)
pattern_suffix_length = len(pattern_suffix)

pattern_length = pattern_prefix_length + pattern_suffix_length

for _ in range(N):
    line = sys.stdin.readline().rstrip()

    line_prefix = line[:pattern_prefix_length]
    line_suffix = line[-pattern_suffix_length:]

    if (
        line_prefix == pattern_prefix and
        line_suffix == pattern_suffix and
        pattern_length <= len(line)
    ):
        print('DA')
    else:
        print('NE')
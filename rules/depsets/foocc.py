# "Foo compiler" that just concatenates its inputs to form its output.
import sys

if __name__ == "__main__":
  if len(sys.argv) < 1:
    raise AssertionError
  output = open(sys.argv[1], "wt")
  for path in sys.argv[2:]:
    input = open(path, "rt")
    output.write(input.read())

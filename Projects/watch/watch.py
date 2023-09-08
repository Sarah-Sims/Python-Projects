import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str
        #sesarch for the string from HTML youtune embeeded
    if re.search(r".+\".+\".",s):
        link_split = s.split("\"")
        for line in link_split:
            if matches := re.search(r"^https?://(?:www\.)?youtube\.com/embed/(.+)$", line, re.IGNORECASE):
                if matches.group(1) != None:
                    return build_url(matches.group(1))
    else:
        return None


def build_url(s):
    return f"https://youtu.be/{s}"
    #xpect that any such URL will be in one of the formats below. Assume that the value of src
    #print(link_split)
    #will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.


if __name__ == "__main__":
    main()
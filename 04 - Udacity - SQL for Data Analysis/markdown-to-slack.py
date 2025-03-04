# Well, it gives the slack format, but now what XD, it still can't recognize code blocks

# Credits: https://stackoverflow.com/questions/41271577/is-there-a-way-to-upload-a-markdown-file-as-a-slack-post

import re
import sys

REGEX_REPLACE = (
    (re.compile("^- ", flags=re.M), "• "),
    (re.compile("^  - ", flags=re.M), "  ◦ "),
    (re.compile("^    - ", flags=re.M), "    ⬩ "),
    (re.compile("^      - ", flags=re.M), "    ◽ "),
    (re.compile("^#+ (.+)$", flags=re.M), r"*\1*"),
    (re.compile("\*\*"), "*"),
)


def main(i, o):
    s = i.read()
    for regex, replacement in REGEX_REPLACE:
        s = regex.sub(replacement, s)
    o.write(s)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as i, open(
        sys.argv[1] + ".slack", "w", encoding="utf-8"
    ) as o:
        main(i, o)

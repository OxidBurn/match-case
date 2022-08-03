import re
from dataclasses import dataclass
import string

@dataclass
class RegexEqual(str):
    string: str
    match: re.Match = None

    def __eq__(self, pattern):
        self.match = re.search(pattern, self.string)
        return self.match is not None

    def __getitem__(self, group):
        return self.match[group]

print(bool(RegexEqual('Something') == "^S.*ing$"))

match RegexEqual("Something to match"):
    case "^...match":
        print("Nope...")
    case "^S.*ing$":
        print("Closer...")
    case "^S.*match$":
        print("Yep!")

match RegexEqual("Something to match"):
    case "^Some(.*ing).*$" as capture:
        print(f"Captured: '{capture[1]}'")
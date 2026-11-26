#!/usr/bin/env python3
"""Write one museum placard line for an ordinary office object.

The placard treats a stapler as an ancient artifact: catalogue date,
material, imagined rite, donor. Pure standard library only.
"""

import os
import stat

PLACARD = (
    "Stapler, c. 1987. Pressed steel and quiet menace. Instrument of the "
    "Binding Rite, joining two leaves into one, that neither might stray. "
    "Donated by the Department of Accounts."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(PLACARD)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()

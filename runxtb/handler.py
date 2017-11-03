#!/usr/bin/env python3

import re

# handler take text and fn, convert input to xyz and return new fn

def write_xyz(xyz_fn, lines):
    number_of_atoms = str(len(lines))
    with open(xyz_fn, "w") as handle:
        handle.write(number_of_atoms + "\n\n" + "\n".join(lines))

    return xyz_fn


def handle_gaussian(text, gaussian_inp_fn):
    line_re = "[A-Z]+\s*" + "[\d\-\.]+\s*"*3
    lines = [line.strip() for line in text.split("\n")]
    func = lambda line: re.match(line_re, line)
    coord_lines = list(filter(func, lines))
    xyz_fn = f"{gaussian_inp_fn}.xyz"
    return write_xyz(xyz_fn, coord_lines)


if __name__ == "__main__":
    with open("/scratch/programme/runxtb/test/model.com") as handle:
        text = handle.read()
    handle_gaussian(text)

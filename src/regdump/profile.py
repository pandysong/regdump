import re
from regdump.file_reader import readlines
from collections import namedtuple

Field = namedtuple(
    "Field", ["start", "len", "name", "description", "valuemap"])


def get_field(field, description, valuemap):
    s = field[0]
    if ":" in s:
        bitendstart = s.strip().split(":")
        bitlen = int(bitendstart[0]) - int(bitendstart[1]) + 1
        start = int(bitendstart[1])
    else:
        bitlen = 1
        start = int(s)

    return Field(start=start, len=bitlen, name=field[2],
                 description=description, valuemap=valuemap)


def is_field_header(field):
    return (len(field) == 4) and (field[0][0].isdigit())


def split_field(f):
    return [s.strip() for s in f.split(",")]


def parse_profile_internal(lines, lq, err_io):
    # skip the header

    profile = []
    try:
        header = next(lines)
        while True:
            l = next(lines)
            field = split_field(l)
            if is_field_header(field):
                # it is field header, go ahead to get description

                description = next(lines).strip()
                dfield = split_field(description)
                if is_field_header(dfield):
                    lq.put(description)
                    continue

                try:
                    # get the value map
                    m = {}
                    while True:
                        vmap = next(lines)
                        vfield = split_field(vmap)
                        if is_field_header(vfield):
                            lq.put(vmap)
                            break
                        mapvalues = [s.strip() for s in vmap.split(":")]
                        m[mapvalues[0]] = mapvalues[1]
                    #print("  map", m)

                finally:
                    # create object
                    # using try:finally because StopIteration could happen
                    # when getting value map
                    f = get_field(field, description, m)
                    field = None
                    description = None
                    m = {}
                    profile = profile + [f]
            else:
                print("unexpcted line:", field)

    except StopIteration:
        pass

    return profile


def parse_profile(profile, err_io):
    """Parse reg profile from a .reg file

        profile: the profile file name
        err_io: file like interface to receive the log info. This
            could be used by a client to recevie the log and display on
            the console or on web page if needed.
    """

    try:
        lines, lq = readlines(profile, "gb18030")

        # create BOM dict from schematic and part database
        # one schematic could define multiple product which is defined by product
        return parse_profile_internal(lines, lq, err_io)
    except UnicodeDecodeError:
        # if gb18030 fails, we try utf-8
        lines, lq = readlines(pads_schematic, "utf-8")
        return parse_profile_internal(lines, lq, err_io)

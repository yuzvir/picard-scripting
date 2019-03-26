PLUGIN_NAME = u"Release Format (types of mediums)"
PLUGIN_AUTHOR = u"Nobody Cares"
PLUGIN_DESCRIPTION = u"""Like %media% tag this plugin gives you
opportunity to use %~releaseformat% that returns formated string with
all types of mediums in release (example: 4×CD + DVD-Video)"""
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "2.0"]

from collections import OrderedDict

from picard.metadata import register_album_metadata_processor
from picard import log


def convert_to_str(item):
    medium_format, medium_count = item
    if medium_count == 1:
        return medium_format
    return "%d×%s" % (medium_count, medium_format)

def release_format(album, metadata, release):
    mediums = OrderedDict()
    for medium in release.get("media") or []:
        fmt = medium.get("format") or "UNK"
        if fmt not in mediums:
            mediums[fmt] = 1
        else:
            mediums[fmt] += 1
    metadata["~releaseformat"] = " + ".join(map(convert_to_str, mediums.items()))


register_album_metadata_processor(release_format)

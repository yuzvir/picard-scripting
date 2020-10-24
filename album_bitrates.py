PLUGIN_NAME = u"Album Bitrates"
PLUGIN_AUTHOR = u"Nobody Cares"
PLUGIN_DESCRIPTION = u"""This plugin gives you
opportunity to use %_folderbr% that returns average bitrate for a folder."""
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "2.0"]

from picard.metadata import register_album_metadata_processor, register_track_metadata_processor
from picard.file import register_file_post_load_processor
from picard.file import register_file_post_addition_to_track_processor
from picard import log
import json

BITRATES_ORDER = [
    '64', '128', '160', '192', 'V2', '256', 'V0', '320'
]


def convert_bitrate(br):
    if br == 320.0:
        return '320'
    elif br == 256.0:
        return '256'
    elif br == 192.0:
        return '192'
    elif br == 160.0:
        return '160'
    elif br == 128.0:
        return '128'
    elif br == 64.0:
        return '64'
    elif br >= 220.0:
        return 'V0'
    elif br < 220.0:
        return 'V2'
    return None


def calculate_album_bitrates(track, file):
    bitrates = []
    converted_bitrates = []
    for album_file in track.album.iterfiles():
        bitrate = album_file.metadata.get('~bitrate')
        if not bitrate:
            continue
        bitrates.append(float(bitrate))
    if not bitrates:
        return
    average_bitrate = sum(bitrates) / len(bitrates)
    album_bitrates = set(map(convert_bitrate, bitrates))
    album_bitrates.discard(None)
    if not album_bitrates:
        return
    sorted_bitrates = []
    for br in BITRATES_ORDER:
        if br in album_bitrates:
            sorted_bitrates.append(br)
    album_bitrate = "+".join(sorted_bitrates)
    for album_file in track.album.iterfiles():
        album_file.metadata['~albumBitrate'] = album_bitrate


register_file_post_addition_to_track_processor(calculate_album_bitrates)

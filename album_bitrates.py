PLUGIN_NAME = u"Album Bitrates"
PLUGIN_AUTHOR = u"Nobody Cares"
PLUGIN_DESCRIPTION = u"""This plugin gives you
opportunity to use %_folderbr% that returns average bitrate for a folder."""
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15", "2.0"]

from picard.file import register_file_post_addition_to_track_processor

BITRATES_ORDER = {
    '64': 0,
    '128': 1,
    '160': 2,
    '192': 3,
    'V2': 4,
    '256': 5,
    'V0': 6,
    '320': 7
}


CBR_VALUES = {
    320.0: '320',
    225.0: '256',
    192.0: '192',
    160.0: '160',
    128.0: '128',
    64.0: '64',
}


def convert_bitrate(br):
    cbr = CBR_VALUES.get(br)
    if cbr:
        return cbr
    if br >= 220.0:
        return 'V0'
    elif br < 220.0:
        return 'V2'
    return None


def calculate_album_bitrates(track, file):
    bitrates = []
    for album_file in track.album.iterfiles():
        bitrate = album_file.metadata.get('~bitrate')
        if not bitrate:
            continue
        bitrates.append(float(bitrate))
    if not bitrates:
        return
    album_bitrates = set(map(convert_bitrate, bitrates))
    album_bitrates.discard(None)
    if not album_bitrates:
        return
    sorted_bitrates = sorted(album_bitrates, key=BITRATES_ORDER.get)
    album_bitrate = "+".join(sorted_bitrates)
    for album_file in track.album.iterfiles():
        album_file.metadata['~albumBitrate'] = album_bitrate


register_file_post_addition_to_track_processor(calculate_album_bitrates)

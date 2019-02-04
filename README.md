# picard-scripting

[MusicBrainz Picard](https://picard.musicbrainz.org) is a music tagger (ID3 etc) that uses the MusicBrainz database as a source of information.
You provide Picard with your MP3s, FLACs, M4As etc, it will recognize the music with acoustic fingerprinting, find the correspondent artists, albums and tracks in the MusicBrainz online database and use this information to tag (ID3 etc) your files.

Picard can be scripted and these are my personal configurations. They do the following:

* Change non-filesystem-friendly chars on filenames into filesystem-friendly ones using Unicode. For example: #➡♯, :➡∶, /➡／, *➡✱ etc

* Correctly handle release date versus original release date, number of discs etc


## Folder Structure ##

* (ALBUM_ARTIST | Various Artists)/
	* (Unofficial* Albums | Live | Singles & EPs | Compilations | Promos | Others)/
		* ORIGINAL_YEAR - [LABEL]* ALBUM (RELEASE_YEAR)* [RELEASE_INFO] [CATALOG_ID] [AUDIO_QUALITY] {INCOMPLETE}*/
			* (Disc | CD) DISC_NUMBER - DISC_SUBTITLE/*
				* TRACK_NUMBER - TRACK_ARTIST - TITLE

Example:

Coil/Albums/2003 - ANS (2004) [CD, Album] [THRESHOLD1] [MP3 256@44k]/CD 01/01 - Coil - [untitled].mp3

Notes:

* Release folder (Albums, Live, etc.) wouldn't be created for Various Artists
* if RELEASETYPE is set to 'bootleg' release folder will be changed to Unoffical Albums, Unoffical Singles & EPs, etc.
* LABEL will be added only for Various Artists albums
* RELEASE_YEAR will be added only if it differs from ORIGINAL_YEAR
* {INCOMPLETE} will be added only if album doesn't have all tracks
* DISC_SUBTITLE - will be added only if it exists
* Disc folder will be created for multidiscs albums




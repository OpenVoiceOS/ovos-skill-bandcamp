> # ⚠️ DEPRECATED
>
> This OCP **search skill** is deprecated and unmaintained. OCP search skills
> (`OVOSCommonPlaybackSkill` + `@ocp_search`) are replaced by **MediaProvider**
> plugins loaded in-process by the
> [`ovos-ocp-pipeline-plugin`](https://github.com/OpenVoiceOS/ovos-ocp-pipeline-plugin),
> which dispatches search to them — the replacement is
> [`ovos-media-provider-bandcamp`](https://github.com/OpenVoiceOS/ovos-media-provider-bandcamp).
> The package is published, but it only does anything once the OCP pipeline's
> MediaProvider dispatch is the default search path — installing it does not
> replace this skill under the legacy OCP/`ovos-audio` stack. `ovos-media` is
> a separate component (the player daemon) and is not involved in search.
>
> - **How MediaProviders work / how to migrate:** https://github.com/OpenVoiceOS/ovos-media/blob/dev/docs/media-providers.md
> - **Base-class deprecation:** [ovos-workshop#423](https://github.com/OpenVoiceOS/ovos-workshop/pull/423)
>
> This skill keeps working until the OCP pipeline's MediaProvider dispatch
> becomes the default search path and this repository is archived.

# <img src='./res/logo.png' width='50' height='50' style='vertical-align:bottom'/> BandCamp Skill

## About

Bandcamp skill for your hipster music needs

![](./gui.gif)

## Examples
* "play compressorhead"
* "play astronaut problems"
* "play {artist/album/genre/track}"

* "search bandcamp for black metal"
* "search bandcamp for {artist/album/genre/track}"

* "play center of all infinity album"
* "play {album} album"

* "play freezing moon by mayhem"
* "play {track} by {artist}"


## Credits
JarbasAl

## Category
**Entertainment**

## Tags
- music
- audio
- bandcamp
- common play


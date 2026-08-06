# Source and license notice

This repository automates a modified Lite build of
[zly2006/zhihu-plus-plus](https://github.com/zly2006/zhihu-plus-plus), licensed under
the GNU Affero General Public License, version 3.

For every published APK, the corresponding source is the upstream tag with the
version shown by that release, plus `scripts/patch_upstream.py` from this
repository commit. The workflow applies that patch deterministically before
building. No upstream source files are redistributed or modified in this
repository outside the build runner.

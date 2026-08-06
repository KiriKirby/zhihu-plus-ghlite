# zhihu-plus-ghlite

Automatically builds the Lite flavor of [Zhihu++](https://github.com/zly2006/zhihu-plus-plus)
when upstream publishes a formal release.

The APK package name is `com.github.zly2006.zhplus.lite`, matching upstream Lite.
This APK is signed with this repository's own key and therefore cannot coexist with
or normally replace the upstream Lite APK. If upstream Lite is installed, Android
requires it to be uninstalled before installing this build; installed application
data is not retained by that migration.

## Automation

`.github/workflows/release-lite.yml` checks upstream once a week (Monday 03:23 UTC), and can also be
started manually. It does no Android build unless the matching release in this
repository is absent or lacks `zhihu++-lite.apk`. Builds only run
`:app:assembleLiteRelease`; Full, desktop, tests, Rust targets, and NDK installation
are intentionally omitted.

Each built APK is patched to check this repository's formal GitHub Releases only.
Nightly checks are disabled in the patched app, and the previous Reden fallback is
removed, so it cannot redirect users to upstream assets.

## Signing

The repository needs these Actions secrets before a release can be built:

- `ANDROID_SIGNING_KEY`: base64-encoded JKS contents
- `ANDROID_KEY_ALIAS`
- `ANDROID_KEYSTORE_PASSWORD`
- `ANDROID_KEY_PASSWORD`

All future releases must retain the same key. Android will reject an update signed by
a different certificate.

## Corresponding source

See [NOTICE.md](NOTICE.md). A release tag maps directly to its upstream tag; the
patch script in this repository is the complete local modification applied to that
source before compilation.

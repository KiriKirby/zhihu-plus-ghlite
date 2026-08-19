# Contributing

This repository contains the automation and minimal patch for the Lite Android
distribution of Zhihu++. Changes should remain focused on that purpose.

Before opening a pull request, run:

```text
python -m py_compile scripts/patch_upstream.py
```

Explain workflow changes, preserve the package name
`com.github.zly2006.zhplus.lite`, and update `README.md` and `NOTICE.md` when
the build or corresponding-source process changes. Do not commit signing keys,
APK files, credentials, or generated build output. Pull requests are reviewed
under the AGPL-3.0 license.

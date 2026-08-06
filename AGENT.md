# zhihu-plus-ghlite

Read this file before changing the repository.

- This repository publishes only the Lite Android variant of `zly2006/zhihu-plus-plus`.
- The published package name must remain `com.github.zly2006.zhplus.lite`.
- The update client must query this repository, never the upstream GitHub or Reden endpoints.
- Only upstream formal releases may be built or offered as updates; nightly and prerelease updates stay disabled.
- A release is idempotent: do not rebuild an upstream tag when its Release already contains `zhihu++-lite.apk`.
- Keep the corresponding-source instructions and the AGPL notice accurate whenever the workflow or patch changes.

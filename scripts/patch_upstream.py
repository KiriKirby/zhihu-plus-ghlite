#!/usr/bin/env python3
"""Apply the minimal, deterministic changes for this Lite distribution."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def replace_once(path: Path, pattern: str, replacement: str) -> None:
    content = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"Expected one matching block in {path}")
    path.write_text(updated, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--release-repository", required=True)
    args = parser.parse_args()

    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.release_repository):
        raise ValueError("release repository must have the form owner/repository")

    latest_url = f"https://api.github.com/repos/{args.release_repository}/releases/latest"
    release_file = args.source.resolve() / "shared/src/commonMain/kotlin/com/github/zly2006/zhihu/updater/GithubRelease.kt"

    replace_once(
        release_file,
        r'^const val ZHIHU_PLUS_PLUS_GITHUB_LATEST_RELEASE_URL = .*\n'
        r'^const val ZHIHU_PLUS_PLUS_REDEN_LATEST_RELEASE_URL = .*\n'
        r'^const val ZHIHU_PLUS_PLUS_GITHUB_NIGHTLY_RELEASE_URL = .*$',
        f'const val ZHIHU_PLUS_PLUS_GITHUB_LATEST_RELEASE_URL = "{latest_url}"',
    )
    replace_once(
        release_file,
        r'''suspend fun fetchLatestZhihuRelease\(
    client: HttpClient,
    githubToken: String\?,
\): GithubRelease = runCatching \{
    client\.get\(ZHIHU_PLUS_PLUS_REDEN_LATEST_RELEASE_URL\)\.raiseForStatus\(\)\.body<GithubRelease>\(\)
\}\.getOrNull\(\) \?: client
    \.get\(ZHIHU_PLUS_PLUS_GITHUB_LATEST_RELEASE_URL\) \{
        githubToken\?\.let \{ token ->
            headers \{
                append\(HttpHeaders\.Authorization, "Bearer \$token"\)
            \}
        \}
    \}\.raiseForStatus\(\)
    \.body<GithubRelease>\(\)''',
        '''suspend fun fetchLatestZhihuRelease(
    client: HttpClient,
    githubToken: String?,
): GithubRelease = client
    .get(ZHIHU_PLUS_PLUS_GITHUB_LATEST_RELEASE_URL) {
        githubToken?.let { token ->
            headers {
                append(HttpHeaders.Authorization, "Bearer $token")
            }
        }
    }.raiseForStatus()
    .body<GithubRelease>()''',
    )
    replace_once(
        release_file,
        r'''suspend fun fetchNightlyZhihuRelease\(
    client: HttpClient,
    githubToken: String\?,
\): GithubRelease = client
    \.get\(ZHIHU_PLUS_PLUS_GITHUB_NIGHTLY_RELEASE_URL\) \{
        githubToken\?\.let \{ token ->
            headers \{
                append\(HttpHeaders\.Authorization, "Bearer \$token"\)
            \}
        \}
    \}\.raiseForStatus\(\)
    \.body<GithubRelease>\(\)''',
        '''suspend fun fetchNightlyZhihuRelease(
    client: HttpClient,
    githubToken: String?,
): GithubRelease = throw IllegalStateException("Nightly updates are disabled for Lite releases")''',
    )


if __name__ == "__main__":
    main()

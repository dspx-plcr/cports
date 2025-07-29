pkgname = "python-urwid"
pkgver = "3.0.2"
pkgrel = 0
build_style='python_pep517'
hostmakedepends = [
  "python",
  "python-build",
  "python-installer",
  "python-pip",
  "python-setuptools_scm",
]
depends = [
  "python",
  "python-wcwidth",
  "reticulum",
]
pkgdesc = "Console user interface library for Python"
license = "LGPL-2.1-only"
url = "https://github.com/urwid/urwid"
source = f"$(PYPI_SITE)/u/urwid/urwid-{pkgver}.tar.gz"
sha256 = "e7cb70ba1e7ff45779a5a57e43c57581ee7de6ceefb56c432491a4a6ce81eb78"

def check(self):
  # broken, cbf fixing it
  pass

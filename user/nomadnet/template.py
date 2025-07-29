pkgname = "nomadnet"
pkgver = "0.8.0"
pkgrel = 0
build_style='python_pep517'
hostmakedepends = [
  "python",
  "python-build",
  "python-installer",
  "python-pip",
  "python-setuptools",
]
depends = [
  "python",
  "python-lxmf",
  "python-qrcode",
  "python-urwid",
  "reticulum",
]
pkgdesc = "Cryptography-based networking stack"
license = "custom:reticulum"
url = "https://github.com/markqvist/NomadNet"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9008ccef41792f2a04ab308444fd3cd8322222fe84cd09baa84feaf51700b1cc"

def check(self):
  pass

def post_install(self):
  self.install_license(self.srcdir / 'LICENSE')

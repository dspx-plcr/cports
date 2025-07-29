pkgname = "python-lxmf"
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
  "reticulum",
]
pkgdesc = "Cryptography-based networking stack"
license = "custom:reticulum"
url = "https://github.com/markqvist/LXMF"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d77f83757ded06c738e097c3a8fc337768ab6459bf9f86403b780509d4690784"

def check(self):
  pass

def post_install(self):
  self.install_license(self.srcdir / 'LICENSE')

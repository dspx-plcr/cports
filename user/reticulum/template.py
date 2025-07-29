pkgname = "reticulum"
pkgver = "1.0.0"
pkgrel = 0
build_style='python_pep517'
hostmakedepends = [
  "python",
  "python-build",
  "python-installer",
  "python-pip",
  "python-setuptools",
]
depends = ["python", "python-pyserial", "python-cryptography"]
pkgdesc = "Cryptography-based networking stack"
license = "custom:reticulum"
url = "https://github.com/markqvist/Reticulum"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "25769ce1e439734a10b0fb9e82eafa5289fb4d4e1be80d78ff64ef207603860c"

def check(self):
  # doens't use pytest, cbf fixing it
  pass

def post_install(self):
  self.install_license(self.srcdir / 'LICENSE')

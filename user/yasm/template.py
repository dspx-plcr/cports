pkgname = "yasm"
pkgver = "1.3.0"
pkgrel = 0
build_style = 'cmake'
hostmakedepends = ["clang", "gmake", "cmake", "ninja", "python"]
pkgdesc = "Yasm Assembler"
license = 'BSD-2-Clause AND GPL-2.0-only AND LGPL-2.0-only AND custom:yasm'
url = "https://github.com/yasm/yasm"
source = f"https://github.com/yasm/yasm/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f708be0b7b8c59bc1dbe7134153cd2f31faeebaa8eec48676c10f972a1f13df3"

def post_install(self):
    self.install_license(self.srcdir / 'Artistic.txt')
    self.install_license(self.srcdir / 'BSD.txt')
    self.install_license(self.srcdir / 'GNU_GPL-2.0')
    self.install_license(self.srcdir / 'GNU_LGPL-2.0')

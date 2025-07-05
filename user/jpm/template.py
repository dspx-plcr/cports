pkgname = "jpm"
pkgver = "1.1.0"
pkgrel = 0
hostmakedepends = ["janet"]
depends = ["janet", "janet-devel", "janet-devel-static"]
pkgdesc = "Janet Project Manager"
license = "MIT"
url = "https://github.com/janet-lang/jpm"
source = f"https://github.com/janet-lang/jpm/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "337c40d9b8c087b920202287b375c2962447218e8e127ce3a5a12e6e47ac6f16"

def install(self):
    self.do("janet", self.chroot_srcdir / "bootstrap.janet",
        env={"PREFIX": "/usr", "DESTDIR": self.chroot_destdir})
    self.install_license(self.srcdir / "LICENSE")

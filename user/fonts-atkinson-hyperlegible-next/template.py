pkgname = "fonts-atkinson-hyperlegible-next"
pkgver = "2025.02.21"
_commit = "7925f50f649b3813257faf2f4c0b381011f434f1"
pkgrel = 0
pkgdesc = "Atkinson Hyperlegible Next font"
license = "OFL-1.1"
url = "https://github.com/googlefonts/atkinson-hyperlegible-next"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "4b455dcf5ce2d6261df7caf6f4d035c893b446f14269106a07bc03c204368626"

def install(self):
    self.install_file("fonts/otf/*.otf", \
        "usr/share/fonts/atkinson-hyperlegible-next", glob=True)
    self.install_license("OFL.txt")

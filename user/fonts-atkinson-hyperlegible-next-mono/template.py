pkgname = "fonts-atkinson-hyperlegible-next-mono"
pkgver = "2024.11.20"
_commit = "154d50362016cc3e873eb21d242cd0772384c8f9"
pkgrel = 0
pkgdesc = "Atkinson Hyperlegible Next font"
license = "OFL-1.1"
url = "https://github.com/googlefonts/atkinson-hyperlegible-next-mono"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "d8b50ca876781ef6c2f0e1dd1a7ed6896a7f7769242e76be901b98c6d7edfafb"

def install(self):
    self.install_file("fonts/otf/*.otf", \
        "usr/share/fonts/atkinson-hyperlegible-next-mono", glob=True)
    self.install_license("OFL.txt")

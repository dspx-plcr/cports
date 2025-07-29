pkgname = "dumbpipe"
pkgver = "0.28.0"
pkgrel = 0
build_style='cargo'
hostmakedepends = ["rust", "cargo",]
pkgdesc = "Unix pipes between devices"
license = "MIT OR Apache-2.0"
url = "https://github.com/n0-computer/dumbpipe"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bb7bd90eacebe505f2c669e4e13dac57c43c9c0eb5eca94dfa1378fd7cdcda84"

def check(self):
	# no network connection
	pass

def post_install(self):
	self.install_license(self.srcdir / 'LICENSE-APACHE')
	self.install_license(self.srcdir / 'LICENSE-MIT')

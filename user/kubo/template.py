pkgname = "kubo"
pkgver = "0.36.0"
pkgrel = 0
build_style='go'
hostmakedepends = ["go", "gmake", "bash"]
pkgdesc = "IPFS implementation in Go"
license = "MIT AND Apache-2.0"
url = "https://github.com/ipfs/kubo"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "624c830b5ef33cfacc7de1bc9ce9f9e85d14cd79a37092484470b987f6e63b6b"

def build(self):
	from cbuild.util import golang
	self.do("make", "build", env=golang.get_go_env(self))

def install(self):
	self.install_bin(self.srcdir / 'cmd/ipfs/ipfs')
	self.install_license(self.srcdir / 'LICENSE')
	self.install_license(self.srcdir / 'LICENSE-MIT')
	self.install_license(self.srcdir / 'LICENSE-APACHE')

def check(self):
	# network is unreachable
	pass

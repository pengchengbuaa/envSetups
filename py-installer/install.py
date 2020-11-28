from .tasks.install_package import install_packages
from .tasks.setup_ssh import setup_ssh
from .tasks.setup_zsh import setup_zsh
from .utils.running_platform import get_distribution
from .utils.package_manager import get_package_manager


dist = get_distribution()
pkg_m = get_package_manager(dist)

install_packages(pkg_m)
setup_ssh()
setup_zsh()
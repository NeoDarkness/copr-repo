%global commit      0a37ab19f654e77129b409fed371891c01ffd0b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250711

Name:           catppuccin-grub-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Catppuccin themes for GRUB

License:        MIT
URL:            https://github.com/catppuccin/grub
Source0:        %{url}/archive/%{commit}/grub-%{commit}.tar.gz

BuildArch:      noarch

%global themedir /boot/grub2/themes

Requires:       catppuccin-frappe-grub-theme = %{version}-%{release}
Requires:       catppuccin-latte-grub-theme = %{version}-%{release}
Requires:       catppuccin-macchiato-grub-theme = %{version}-%{release}
Requires:       catppuccin-mocha-grub-theme = %{version}-%{release}

%description
Meta package for Catppuccin GRUB themes.

%package -n catppuccin-frappe-grub-theme
Summary:        Catppuccin Frappé GRUB theme

%description -n catppuccin-frappe-grub-theme
Catppuccin Frappé GRUB theme.

%package -n catppuccin-latte-grub-theme
Summary:        Catppuccin Latte GRUB theme

%description -n catppuccin-latte-grub-theme
Catppuccin Latte GRUB theme.

%package -n catppuccin-macchiato-grub-theme
Summary:        Catppuccin Macchiato GRUB theme

%description -n catppuccin-macchiato-grub-theme
Catppuccin Macchiato GRUB theme.

%package -n catppuccin-mocha-grub-theme
Summary:        Catppuccin Mocha GRUB theme

%description -n catppuccin-mocha-grub-theme
Catppuccin Mocha GRUB theme.

%prep
%autosetup -n grub-%{commit}

%install
install -d %{buildroot}%{themedir}
cp -a src/* %{buildroot}%{themedir}/

%files -n catppuccin-frappe-grub-theme
%license LICENSE
%doc README.md
%{themedir}/catppuccin-frappe-*/

%files -n catppuccin-latte-grub-theme
%license LICENSE
%doc README.md
%{themedir}/catppuccin-latte-*/

%files -n catppuccin-macchiato-grub-theme
%license LICENSE
%doc README.md
%{themedir}/catppuccin-macchiato-*/

%files -n catppuccin-mocha-grub-theme
%license LICENSE
%doc README.md
%{themedir}/catppuccin-mocha-*/

%changelog
%autochangelog
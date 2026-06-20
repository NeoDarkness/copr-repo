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

Requires:       catppuccin-frappe-grub-theme
Requires:       catppuccin-latte-grub-theme
Requires:       catppuccin-macchiato-grub-theme
Requires:       catppuccin-mocha-grub-theme

%description
Meta package for Catppuccin GRUB themes.

%prep
%autosetup -n grub-%{commit}

%install
install -d %{buildroot}%{themedir}
cp -a src/* %{buildroot}%{themedir}/

%package -n catppuccin-frappe-grub-theme
Summary: Catppuccin Frappé GRUB theme
BuildArch: noarch

%description -n catppuccin-frappe-grub-theme
Catppuccin Frappé GRUB theme.

%files -n catppuccin-frappe-grub-theme
%{themedir}/catppuccin-frappe/

%package -n catppuccin-latte-grub-theme
Summary: Catppuccin Latte GRUB theme
BuildArch: noarch

%description -n catppuccin-latte-grub-theme
Catppuccin Latte GRUB theme.

%files -n catppuccin-latte-grub-theme
%{themedir}/catppuccin-latte/

%package -n catppuccin-macchiato-grub-theme
Summary: Catppuccin Macchiato GRUB theme
BuildArch: noarch

%description -n catppuccin-macchiato-grub-theme
Catppuccin Macchiato GRUB theme.

%files -n catppuccin-macchiato-grub-theme
%{themedir}/catppuccin-macchiato/

%package -n catppuccin-mocha-grub-theme
Summary: Catppuccin Mocha GRUB theme
BuildArch: noarch

%description -n catppuccin-mocha-grub-theme
Catppuccin Mocha GRUB theme.

%files -n catppuccin-mocha-grub-theme
%{themedir}/catppuccin-mocha/

%files
%license LICENSE
%doc README.md

%changelog
%autochangelog
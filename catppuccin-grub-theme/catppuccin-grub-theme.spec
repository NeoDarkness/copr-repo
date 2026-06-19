%global commit      0a37ab19f654e77129b409fed371891c01ffd0b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250711

Name:           catppuccin-grub-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Catppuccin themes for GRUB

License:        MIT
URL:            https://github.com/catppuccin/grub
Source0:        https://github.com/catppuccin/grub/archive/%{commit}/grub-%{commit}.tar.gz

BuildArch:      noarch

Requires:       catppuccin-mocha-grub-theme = %{version}-%{release}
Requires:       catppuccin-macchiato-grub-theme = %{version}-%{release}
Requires:       catppuccin-frappe-grub-theme = %{version}-%{release}
Requires:       catppuccin-latte-grub-theme = %{version}-%{release}

%description
Meta package for Catppuccin GRUB themes.

%package -n catppuccin-mocha-grub-theme
Summary:        Catppuccin Mocha theme for GRUB

%description -n catppuccin-mocha-grub-theme
Catppuccin Mocha theme for GRUB.

%package -n catppuccin-macchiato-grub-theme
Summary:        Catppuccin Macchiato theme for GRUB

%description -n catppuccin-macchiato-grub-theme
Catppuccin Macchiato theme for GRUB.

%package -n catppuccin-frappe-grub-theme
Summary:        Catppuccin Frappé theme for GRUB

%description -n catppuccin-frappe-grub-theme
Catppuccin Frappé theme for GRUB.

%package -n catppuccin-latte-grub-theme
Summary:        Catppuccin Latte theme for GRUB

%description -n catppuccin-latte-grub-theme
Catppuccin Latte theme for GRUB.

%prep
%autosetup -n grub-%{commit}

%install
install -dm755 %{buildroot}/boot/grub2/themes

cp -a src/. %{buildroot}/boot/grub2/themes/

%files
%license LICENSE
%doc README.md

%files -n catppuccin-mocha-grub-theme
/boot/grub2/themes/catppuccin-mocha-grub-theme

%files -n catppuccin-macchiato-grub-theme
/boot/grub2/themes/catppuccin-macchiato-grub-theme

%files -n catppuccin-frappe-grub-theme
/boot/grub2/themes/catppuccin-frappe-grub-theme

%files -n catppuccin-latte-grub-theme
/boot/grub2/themes/catppuccin-latte-grub-theme

%changelog
%autochangelog

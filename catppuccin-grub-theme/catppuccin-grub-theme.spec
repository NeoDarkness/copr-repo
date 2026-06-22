%global commit      0a37ab19f654e77129b409fed371891c01ffd0b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250711

Name:           catppuccin-grub-theme
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel themes for GRUB2

License:        MIT
URL:            https://github.com/catppuccin/grub
Source0:        %{url}/archive/%{commit}/grub-%{commit}.tar.gz

BuildArch:      noarch

Requires:       grub2-common

%description
Catppuccin themes for GRUB2 (Frappé, Latte, Macchiato, Mocha).

%package latte
Summary:        Catppuccin Latte GRUB2 theme
Requires:       %{name} = %{version}-%{release}

%description latte
Catppuccin Latte flavor theme for GRUB2.

%package frappe
Summary:        Catppuccin Frappé GRUB2 theme
Requires:       %{name} = %{version}-%{release}

%description frappe
Catppuccin Frappé flavor theme for GRUB2.

%package macchiato
Summary:        Catppuccin Macchiato GRUB2 theme
Requires:       %{name} = %{version}-%{release}

%description macchiato
Catppuccin Macchiato flavor theme for GRUB2.

%package mocha
Summary:        Catppuccin Mocha GRUB2 theme
Requires:       %{name} = %{version}-%{release}

%description mocha
Catppuccin Mocha flavor theme for GRUB2.

%prep
%autosetup -n grub-%{commit}

%install
install -d %{buildroot}/boot/grub2/themes
cp -a src/* %{buildroot}/boot/grub2/themes/

%files
%license LICENSE
%doc README.md

%files latte
/boot/grub2/themes/catppuccin-latte-*

%files frappe
/boot/grub2/themes/catppuccin-frappe-*

%files macchiato
/boot/grub2/themes/catppuccin-macchiato-*

%files mocha
/boot/grub2/themes/catppuccin-mocha-*

%changelog
%autochangelog
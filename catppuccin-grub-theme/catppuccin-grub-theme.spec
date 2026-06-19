%global commit 0a37ab19f654e77129b409fed371891c01ffd0b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20260619

%global debug_package %{nil}

Name:           catppuccin-grub-theme
Version:        %{date}git%{shortcommit}
Release:        %autorelease
Summary:        Catppuccin themes for GRUB

License:        MIT
URL:            https://github.com/catppuccin/grub
Source0:        https://github.com/catppuccin/grub/archive/%{commit}/grub-%{commit}.tar.gz

BuildArch:      noarch

Requires:       %{name}-mocha = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}

%description
Meta package for Catppuccin GRUB themes.

%package mocha
Summary:        Catppuccin Mocha theme for GRUB
%description mocha
Catppuccin Mocha theme for GRUB.

%package macchiato
Summary:        Catppuccin Macchiato theme for GRUB
%description macchiato
Catppuccin Macchiato theme for GRUB.

%package frappe
Summary:        Catppuccin Frappé theme for GRUB
%description frappe
Catppuccin Frappé theme for GRUB.

%package latte
Summary:        Catppuccin Latte theme for GRUB
%description latte
Catppuccin Latte theme for GRUB.

%prep
%autosetup -n grub-%{commit}

%install
# Membuat direktori tujuan langsung di /boot/grub2/themes
install -dm755 %{buildroot}/boot/grub2/themes

# Menyalin folder tema dari repo upstream (folder src berisi subfolder mocha, latte, dll)
cp -a src/. %{buildroot}/boot/grub2/themes/

%files
%license LICENSE
%doc README.md

%files mocha
/boot/grub2/themes/catppuccin-mocha-grub-theme

%files macchiato
/boot/grub2/themes/catppuccin-macchiato-grub-theme

%files frappe
/boot/grub2/themes/catppuccin-frappe-grub-theme

%files latte
/boot/grub2/themes/catppuccin-latte-grub-theme

%changelog
%autochangelog

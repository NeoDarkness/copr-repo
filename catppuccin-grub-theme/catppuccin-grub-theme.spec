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

%description
Catppuccin GRUB themes (Frappé, Latte, Macchiato, Mocha).

%prep
%autosetup -n grub-%{commit}

%install
install -d %{buildroot}/boot/grub2/themes
cp -a src/. %{buildroot}/boot/grub2/themes/

%files
%license LICENSE
%doc README.md
%dir /boot/grub2/themes
/boot/grub2/themes/*

%changelog
%autochangelog
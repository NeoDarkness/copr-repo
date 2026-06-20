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

%description
Catppuccin GRUB themes (Frappé, Latte, Macchiato, Mocha).

%prep
%autosetup

%install
install -d %{buildroot}%{themedir}
cp -a src/. %{buildroot}%{themedir}/

%files
%license LICENSE
%doc README.md
%{themedir}/catppuccin-*-grub-theme/

%changelog
%autochangelog
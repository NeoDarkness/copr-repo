%global commit 0a37ab19f654e77129b409fed371891c01ffd0b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250711

%global _grubthemedir /boot/grub2/themes

Name:           grub2-catppuccin-theme
Version:        0^%{commitdate}git.%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel theme for GRUB2

License:        MIT
URL:            https://github.com/catppuccin/grub
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

Requires:       grub2-common

%description
Soothing pastel theme for GRUB2.

%prep
%autosetup -n grub-%{commit} -p1

%install
install -d %{buildroot}%{_grubthemedir}
cp -a src/* %{buildroot}%{_grubthemedir}/

%files
%license LICENSE
%doc README.md
%{_grubthemedir}/catppuccin-*-grub-theme

%changelog
%autochangelog
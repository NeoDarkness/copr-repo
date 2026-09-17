%global commit f83671d17ea67e335b34f8028a7e6d78bca735d7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20240608

Name:           papirus-folders-catppuccin
Version:        0^%{commitdate}git.%{shortcommit}
Release:        %autorelease
Summary:        Soothing pastel folder colors for Papirus icon themes

License:        MIT
URL:            https://github.com/catppuccin/papirus-folders
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

Requires:       papirus-folders
Requires:       papirus-icon-theme

%description
Soothing pastel folder colors for Papirus icon themes.

This package provides Catppuccin folder color variants for use with
the papirus-folders utility, allowing you to bring the cozy
Catppuccin aesthetic to your file manager.

%prep
%autosetup -n papirus-folders-%{commit} -p1

%install
install -d %{buildroot}%{_datadir}/icons/Papirus
cp -a src/* %{buildroot}%{_datadir}/icons/Papirus/

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Papirus/*x*/places/*cat-*.svg

%changelog
%autochangelog
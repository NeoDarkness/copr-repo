%global forgeurl https://github.com/catppuccin/papirus-folders
%global commit   f83671d17ea67e335b34f8028a7e6d78bca735d7

Name:           papirus-folders-catppuccin
Version:        1.0.0
Release:        %autorelease
Summary:        Catppuccin folder colors for Papirus icon themes

License:        MIT

%forgemeta

URL:            https://github.com/catppuccin/papirus-folders
Source0:        %forgesource

BuildArch:      noarch

Requires:       papirus-folders
Requires:       papirus-icon-theme

%description
Catppuccin folder colors for Papirus icon themes.

This package provides Catppuccin folder color variants for use with the
papirus-folders utility.

%prep
%forgeautosetup

%install
install -d %{buildroot}%{_datadir}/icons/Papirus
cp -a src/* %{buildroot}%{_datadir}/icons/Papirus/

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Papirus/*x*/places/*cat-*.svg

%changelog
%autochangelog
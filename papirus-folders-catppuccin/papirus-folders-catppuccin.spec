%global forgeurl https://github.com/catppuccin/papirus-folders
%global commit f83671d17ea67e335b34f8028a7e6d78bca735d7

%forgemeta

Name:           papirus-folders-catppuccin
Version:        0
Release:        %autorelease
Summary:        Soothing pastel folder colors for Papirus icon themes

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

Requires:       papirus-folders
Requires:       papirus-icon-theme

%description
Soothing pastel folder colors for Papirus icon themes.

This package provides Catppuccin folder color variants for use with
the papirus-folders utility, allowing you to bring the cozy
Catppuccin aesthetic to your file manager.

%prep
%forgeautosetup -p1

%build

%install
install -d %{buildroot}%{_datadir}/icons/Papirus
cp -r src/* %{buildroot}%{_datadir}/icons/Papirus/

%check

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Papirus/*x*/places/*cat-*.svg

%changelog
%autochangelog
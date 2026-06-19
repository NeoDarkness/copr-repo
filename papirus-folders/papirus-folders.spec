Name:           papirus-folders
Version:        1.14.0
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icons

License:        GPL-3.0-only
URL:            https://github.com/PapirusDevelopmentTeam/papirus-folders

Source0:        https://github.com/PapirusDevelopmentTeam/papirus-folders/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

Requires:       papirus-icon-theme

%description
Papirus folders is a utility that allows changing folder colors
for Papirus icon themes.

%prep
%autosetup -n papirus-folders-%{version}

%install
install -Dm755 \
    papirus-folders \
    %{buildroot}%{_bindir}/papirus-folders

%files
%license LICENSE
%doc README.md

%{_bindir}/papirus-folders

%changelog
%autochangelog

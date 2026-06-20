Name:           papirus-folders
Version:        1.14.0
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icon themes

License:        GPL-3.0-only
URL:            https://github.com/PapirusDevelopmentTeam/papirus-folders
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

Requires:       papirus-icon-theme

%description
Papirus Folders is a utility for changing folder colors in Papirus icon themes.

%prep
%autosetup -n papirus-folders-%{version}

%install
install -D -m 0755 papirus-folders %{buildroot}%{_bindir}/papirus-folders

%files
%license LICENSE
%doc README.md
%{_bindir}/papirus-folders

%changelog
%autochangelog
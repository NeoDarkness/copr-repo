Name:           papirus-folders
Version:        1.14.0
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icon themes

License:        MIT
URL:            https://github.com/PapirusDevelopmentTeam/papirus-folders
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

Requires:       papirus-icon-theme

%description
Papirus Folders is a utility for changing folder colors in Papirus icon themes.

%prep
%autosetup

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/papirus-folders
%{_datadir}/bash-completion/completions/papirus-folders
%{_datadir}/zsh/site-functions/_papirus-folders

%changelog
%autochangelog
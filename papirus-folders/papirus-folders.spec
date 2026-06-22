%global forgeurl https://github.com/PapirusDevelopmentTeam/papirus-folders

Name:           papirus-folders
Version:        1.14.0
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icon themes

License:        MIT

%forgemeta

URL:            https://github.com/PapirusDevelopmentTeam/papirus-folders
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  make

Requires:       papirus-icon-theme

%description
Papirus Folders is a utility for changing folder colors in Papirus icon themes.

%prep
%forgeautosetup

%install
%make_install PREFIX=%{_prefix} ZSHCOMPDIR=%{zsh_completions_dir}

%files
%license LICENSE
%doc README.md
%{_bindir}/papirus-folders
%{bash_completions_dir}/papirus-folders
%{zsh_completions_dir}/_papirus-folders

%changelog
%autochangelog
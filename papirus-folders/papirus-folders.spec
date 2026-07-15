%global forgeurl https://github.com/PapirusDevelopmentTeam/papirus-folders

Version:        1.14.0

%forgemeta

Name:           papirus-folders
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icon themes

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  make

Requires:       papirus-icon-theme

%description
Utility for changing folder colors in Papirus icon themes.

%prep
%forgeautosetup

%build

%install
%make_install PREFIX=%{_prefix} ZSHCOMPDIR=%{zsh_completions_dir}

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/papirus-folders
%{bash_completions_dir}/papirus-folders
%{zsh_completions_dir}/_papirus-folders

%changelog
%autochangelog
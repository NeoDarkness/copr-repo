Name:           papirus-folders
Version:        1.14.0
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icon themes

License:        MIT
URL:            https://github.com/PapirusDevelopmentTeam/papirus-folders
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

Requires:       papirus-icon-theme

%description
Utility for changing folder colors in Papirus icon themes.

%prep
%autosetup -p1

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
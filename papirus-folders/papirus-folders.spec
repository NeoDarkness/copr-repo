%global forgeurl https://github.com/PapirusDevelopmentTeam/papirus-folders

Name:           papirus-folders
Version:        1.14.0
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icon themes

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  make

Requires:       papirus-icon-theme

%description
Utility for changing folder colors in Papirus icon themes.

%prep
%forgeautosetup

%build
# Nothing to build

%install
%make_install \
    PREFIX=%{_prefix} \
    DESTDIR=%{buildroot} \
    ZSHCOMPDIR=%{zsh_completions_dir}

%check
# No test suite available

%files
%license LICENSE
%doc README.md
%{_bindir}/papirus-folders
%{bash_completions_dir}/papirus-folders
%{zsh_completions_dir}/_papirus-folders

%changelog
%autochangelog
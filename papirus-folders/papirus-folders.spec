%global forgeurl https://github.com/PapirusDevelopmentTeam/papirus-folders
%global commit 0f838ee5679229e3a3e97e3b333c222c9e9615b4

Name:           papirus-folders
Version:        1.14.0
Release:        %autorelease
Summary:        Folder color switching utility for Papirus icon themes

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

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
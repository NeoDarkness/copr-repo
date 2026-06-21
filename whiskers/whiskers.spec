Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool for the high-spirited

License:        MIT
URL:            https://github.com/catppuccin/whiskers
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26

%description
Whiskers is a CLI tool used to generate Catppuccin ports.

%prep
%autosetup
%cargo_prep -N
sed -i 's/^offline = true$//' .cargo/config.toml

%build
%cargo_build

%install
%cargo_install

%check
%cargo_test

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog

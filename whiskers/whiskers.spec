Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT
URL:            https://github.com/catppuccin/whiskers
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  rust

%undefine __cargo_generate_buildrequires

%description
Whiskers CLI tool

%prep
%autosetup

%cargo_prep_online

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
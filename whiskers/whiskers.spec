%global __cargo_common_opts --target-dir %{_target_platform}/cargo-target

Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT
URL:            https://github.com/catppuccin/whiskers
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%autosetup

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
%global forgeurl https://github.com/catppuccin/whiskers

Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT

%forgemeta

URL:            https://github.com/catppuccin/whiskers
Source0:        %forgesource
Source1:        whiskers-%{version}-vendor.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%forgeautosetup -b 1
%cargo_prep -v vendor

%build
%cargo_vendor_manifest
%cargo_build -a

%check
%cargo_test -a

%install
%cargo_install -a

%files
%license LICENSE
%license cargo-vendor.txt
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog
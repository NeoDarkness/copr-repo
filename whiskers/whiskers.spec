%global forgeurl https://github.com/catppuccin/whiskers

Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        MIT AND (MIT OR Apache-2.0) AND BSD-3-Clause AND GPL-3.0-only

%forgemeta

URL:            https://github.com/catppuccin/whiskers
Source0:        %forgesource
Source1:        %{name}-%{version}-vendor.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%forgeautosetup
%setup -q -T -D -a 1
%cargo_prep -v vendor

%build
%cargo_vendor_manifest
%cargo_build -a
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%check
%cargo_test -a

%install
install -Dm0755 target/rpm/whiskers \
    %{buildroot}%{_bindir}/whiskers

%files
%license LICENSE LICENSE.dependencies cargo-vendor.txt
%doc README.md CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog
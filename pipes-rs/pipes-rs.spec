%global forgeurl https://github.com/lhvy/pipes-rs

Name:           pipes-rs
Version:        1.6.4
Release:        %autorelease
Summary:        Animated terminal screensaver inspired by pipes.sh

License:        BlueOak-1.0.0

%forgemeta

URL:            https://github.com/lhvy/pipes-rs
Source0:        %forgesource
Source1:        %{name}-%{version}-vendor.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%description
pipes-rs is a Rust-based animated terminal screensaver inspired by pipes.sh.

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
install -Dm0755 target/rpm/pipes-rs \
    %{buildroot}%{_bindir}/pipes-rs

%files
%license LICENSE.md LICENSE.dependencies cargo-vendor.txt
%doc README.md
%{_bindir}/pipes-rs

%changelog
%autochangelog
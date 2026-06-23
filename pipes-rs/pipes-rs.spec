%bcond check 1

%global forgeurl https://github.com/lhvy/pipes-rs

Name:           pipes-rs
Version:        1.6.4
Release:        %autorelease
Summary:        Animated terminal screensaver inspired by pipes.sh

License:        %{shrink:
    BlueOak-1.0.0 AND
    MIT AND
    Apache-2.0 AND
    (MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
}

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
%cargo_build_crate

%if %{with check}
%check
%cargo_test
%endif

%install
install -Dm0755 target/rpm/pipes-rs \
    %{buildroot}%{_bindir}/pipes-rs

%files
%license LICENSE.md 
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/pipes-rs

%changelog
%autochangelog
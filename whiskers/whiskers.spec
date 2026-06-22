%global forgeurl https://github.com/catppuccin/whiskers

Name:           whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    ISC AND
    Unicode-3.0 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT) AND
    ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND
    ((MIT OR Apache-2.0) AND Unicode-3.0)
}

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
%cargo_build_crate -a

%check
%cargo_test -a

%install
install -Dm0755 target/rpm/whiskers \
    %{buildroot}%{_bindir}/whiskers

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%doc CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog
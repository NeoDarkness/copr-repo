%bcond check 1

%global forgeurl https://github.com/catppuccin/whiskers

Name:           catppuccin-whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

SourceLicense:  MIT

License:        %{shrink:
    (Apache-2.0 OR MIT) AND BSD-3-Clause
    (MIT OR Apache-2.0) AND Unicode-3.0
    0BSD OR MIT OR Apache-2.0
    Apache-2.0
    Apache-2.0 OR BSL-1.0
    Apache-2.0 OR MIT
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
    BSD-2-Clause OR Apache-2.0 OR MIT
    BSD-3-Clause
    ISC
    MIT
    MIT OR Apache-2.0
    MIT OR Apache-2.0 OR LGPL-2.1-or-later
    MIT OR Zlib OR Apache-2.0
    Unlicense OR MIT
}

%forgemeta

URL:            https://github.com/catppuccin/whiskers
Source0:        %forgesource
Source1:        %{name}-%{version}-vendor.tar.gz

BuildRequires:  cargo-rpm-macros

Provides:       whiskers = %{version}-%{release}

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%forgeautosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build_crate -a

%if %{with check}
%check
%cargo_test -a
%endif

%install
cargo_install_crate -a

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%doc CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog
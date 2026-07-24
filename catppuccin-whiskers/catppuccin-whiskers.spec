%bcond check 1

%global cargo_install_lib 0

%global forgeurl https://github.com/catppuccin/whiskers

Version:        2.9.0

%forgemeta

Name:           catppuccin-whiskers
Release:        %autorelease
Summary:        Soothing port creation tool for the high-spirited

SourceLicense:  MIT

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR LGPL-2.1-or-later
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND
    ((MIT OR Apache-2.0) AND Unicode-3.0) AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    BSD-3-Clause AND
    ISC AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
}

URL:            %{forgeurl}
Source0:        %{forgesource}
# Generated with: cargo vendor
Source1:        vendor.tar.gz

BuildRequires:  cargo-rpm-macros

%description
Soothing port creation tool for the high-spirited.

%prep
%autosetup -n %{archivename} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm 0755 target/rpm/whiskers -t %{buildroot}%{_bindir}

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%doc CHANGELOG.md
%{_bindir}/whiskers

%changelog
%autochangelog
%bcond check 1

%global cargo_install_lib 0

%global forgeurl https://github.com/sharkdp/vivid

Version:        0.11.1

%forgemeta

Name:           vivid
Release:        %autorelease
Summary:        LS_COLORS manager with multiple themes

SourceLicense:  MIT OR Apache-2.0

# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# LGPL-3.0-or-later
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    LGPL-3.0-or-later AND
    MIT AND
    (MIT OR Apache-2.0) AND
    (Unlicense OR MIT) AND
    (Zlib OR Apache-2.0 OR MIT)
}

URL:            %{forgeurl}
Source0:        %{forgesource}
# Generated with: cargo vendor
Source1:        vendor.tar.gz

BuildRequires:  cargo-rpm-macros

%description
LS_COLORS manager with multiple themes.

%prep
%autosetup -n %{archivename} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm 0755 target/rpm/vivid -t %{buildroot}%{_bindir}

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%doc CHANGELOG.md
%{_bindir}/vivid

%changelog
%autochangelog
%bcond check 1

%global forgeurl https://github.com/catppuccin/whiskers
%global commit 233654f3cd8101f572e6842dce426c56c86ff98b

Name:           catppuccin-whiskers
Version:        2.9.0
Release:        %autorelease
Summary:        Soothing port creation tool

License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    BSD-3-Clause AND
    ISC AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (MIT OR Zlib OR Apache-2.0) AND
    Unicode-3.0 AND
    (Unlicense OR MIT) AND
    0BSD
}

URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}
# To generate vendor tarball:
# spectool -g catppuccin-whiskers.spec
# cargo vendor
# tar czf vendor.tar.gz vendor/
Source1:        vendor.tar.gz

BuildRequires:  cargo-rpm-macros >= 24

%description
Whiskers CLI tool used to generate Catppuccin ports.

%prep
%autosetup -n %{archivename} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm0755 \
    target/rpm/whiskers \
    %{buildroot}%{_bindir}/whiskers

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE LICENSE.dependencies cargo-vendor.txt
%doc README.md
%{_bindir}/whiskers

%changelog
%autochangelog
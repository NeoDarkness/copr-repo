%bcond check 0

%global cargo_install_lib 0

%global forgeurl https://github.com/ClementTsang/bottom

Version:        0.14.4

%global tag %{version}

%forgemeta

Name:           bottom
Release:        %autorelease
Summary:        Customizable cross-platform graphical process/system monitor for the terminal

# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR MIT OR Apache-2.0
# ISC
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    MIT AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR MIT OR Apache-2.0) AND
    ISC AND
    (MIT OR Apache-2.0) AND
    MPL-2.0 AND
    (Unlicense OR MIT) AND
    Zlib AND
    (Zlib OR Apache-2.0 OR MIT)
}

URL:            %{forgeurl}
Source0:        %{forgesource}
# Generated with: cargo vendor
Source1:        vendor.tar.gz
Patch0:         bottom-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils

%description
A customizable cross-platform graphical process/system monitor for the
terminal. Supports Linux, macOS, and Windows.

%prep
%autosetup -n %{archivename} -p1 -a1
%cargo_prep -v vendor

%build
export BTM_GENERATE=1

%cargo_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

install -Dpm0644 \
    target/tmp/bottom/completion/btm.bash \
    %{buildroot}%{bash_completions_dir}/btm

install -Dpm0644 \
    target/tmp/bottom/completion/btm.fish \
    %{buildroot}%{fish_completions_dir}/btm.fish

install -Dpm0644 \
    target/tmp/bottom/completion/_btm \
    %{buildroot}%{zsh_completions_dir}/_btm

install -Dpm0644 \
    target/tmp/bottom/manpage/btm.1 \
    %{buildroot}%{_mandir}/man1/btm.1

install -Dpm0644 \
    desktop/bottom.desktop \
    %{buildroot}%{_datadir}/applications/bottom.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/bottom.desktop

install -Dpm0644 \
    assets/icons/bottom-system-monitor.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/bottom-system-monitor.svg

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
%{_bindir}/btm
%{bash_completions_dir}/btm
%{fish_completions_dir}/btm.fish
%{zsh_completions_dir}/_btm
%{_mandir}/man1/btm.1*
%{_datadir}/applications/bottom.desktop
%{_datadir}/icons/hicolor/scalable/apps/bottom-system-monitor.svg

%changelog
%autochangelog
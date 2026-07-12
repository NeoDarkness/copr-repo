%bcond check 0

%global cargo_install_lib 0

%global forgeurl https://github.com/starship/starship
%global commit   9140ca5d6a6d7e3f7362baf428b50b4f94811991

%forgemeta

Name:           starship
Version:        1.26.0
Release:        %autorelease
Summary:        Minimal, blazing-fast, and infinitely customizable prompt for any shell! ☄🌌️

SourceLicense:  ISC
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0 OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-2-Clause OR MIT OR Apache-2.0
# CC0-1.0 OR MIT-0 OR Apache-2.0
# ISC
# MIT
# MIT AND Apache-2.0
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR LGPL-2.1-or-later
# MIT OR Apache-2.0 OR Zlib
# MPL-2.0
# Unlicense
# Unlicense OR MIT
# WTFPL
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    ISC AND
    MIT AND
    Apache-2.0 AND
    ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND
    ((MIT OR Apache-2.0) AND Unicode-3.0) AND
    (Apache-2.0 OR BSL-1.0 OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR MIT OR Apache-2.0) AND
    (CC0-1.0 OR MIT-0 OR Apache-2.0) AND
    (MIT AND Apache-2.0) AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    MPL-2.0 AND
    Unlicense AND
    (Unlicense OR MIT) AND
    WTFPL AND
    Zlib AND
    (Zlib OR Apache-2.0 OR MIT)
}

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        vendor.tar.gz

BuildRequires:  cargo-rpm-macros

%description
The minimal, blazing-fast, and infinitely customizable prompt for any
shell! ☄🌌️.

%prep
%autosetup -n %{archivename} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

target/rpm/starship completions bash > starship.bash
target/rpm/starship completions fish > starship.fish
target/rpm/starship completions zsh > _starship

%install
%cargo_install

install -Dpm0644 \
    starship.bash \
    %{buildroot}%{bash_completions_dir}/starship

install -Dpm0644 \
    starship.fish \
    %{buildroot}%{fish_completions_dir}/starship.fish

install -Dpm0644 \
    _starship \
    %{buildroot}%{zsh_completions_dir}/_starship

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
%{_bindir}/starship
%{bash_completions_dir}/starship
%{fish_completions_dir}/starship.fish
%{zsh_completions_dir}/_starship

%changelog
%autochangelog
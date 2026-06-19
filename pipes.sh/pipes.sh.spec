Name:           pipes.sh
Version:        1.3.0
Release:        %autorelease
Summary:        Animated pipes terminal screensaver

License:        MIT
URL:            https://github.com/pipeseroni/pipes.sh
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
Requires:       bash >= 4.0.0

%description
pipes.sh is an animated terminal screensaver inspired by the classic
pipes screensaver.

%prep
%autosetup

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.rst

%{_bindir}/pipes.sh
%{_mandir}/man6/pipes.sh.6*

%changelog
%autochangelog

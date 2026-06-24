%global forgeurl https://github.com/pipeseroni/pipes.sh

Name:           pipes.sh
Version:        1.3.0
Release:        %autorelease
Summary:        Animated pipes terminal screensaver

License:        MIT

%forgemeta

URL:            https://github.com/pipeseroni/pipes.sh
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  make

%description
pipes.sh is an animated terminal screensaver inspired by
the classic pipes screensaver.

It renders colorful animated pipes directly in the terminal.

%prep
%forgeautosetup

%build
# Nothing to build

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%check
# No test suite available

%files
%license LICENSE
%doc README.rst
%{_bindir}/pipes.sh
%{_mandir}/man6/pipes.sh.6*

%changelog
%autochangelog
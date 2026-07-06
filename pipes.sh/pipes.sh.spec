%global forgeurl https://github.com/pipeseroni/pipes.sh
%global commit 581792d4e0ea51e15889ba14a85db1bc9727b83d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pipes.sh
Version:        0^git%{shortcommit}
Release:        %autorelease
Summary:        Animated pipes terminal screensaver

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

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
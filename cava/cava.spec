%global forgeurl https://github.com/karlstav/cava
%global commit 1de0cf4c98768bb94a36cec10f5ea44efcde49f4

Name:           cava
Version:        1.0.0
Release:        %autorelease
Summary:        Console-based audio visualizer

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config

BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(iniparser)

BuildRequires:  alsa-lib-devel
BuildRequires:  pipewire-devel
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel

BuildRequires:  ncurses-devel

%description
CAVA is a console-based audio visualizer supporting multiple audio
input backends and terminal output modes.

%prep
%forgeautosetup
echo %{version} > version
autoreconf -fiv

%build
%configure FONT_DIR=/lib/kbd/consolefonts
%make_build

%install
%make_install

%check
# No test suite available

%files
%license LICENSE
%doc README.md
%{_bindir}/cava
/lib/kbd/consolefonts/cava.psf

%changelog
%autochangelog
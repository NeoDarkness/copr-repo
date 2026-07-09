%global forgeurl https://github.com/karlstav/cava
%global tag      1.0.0

%forgemeta

Name:           cava
Version:        1.0.0
Release:        %autorelease
Summary:        Console-based Audio Visualizer for ALSA

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(libpulse)

%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep
%forgeautosetup
./autogen.sh

%build
%configure FONT_DIR=/lib/kbd/consolefonts
%make_build

%install
%make_install

%check

%files
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
/lib/kbd/consolefonts/cava.psf

%changelog
%autochangelog
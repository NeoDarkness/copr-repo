%global forgeurl https://github.com/karlstav/cava

Version:        1.0.0

%global tag %{version}

%forgemeta

Name:           cava
Release:        %autorelease
Summary:        Console-based Audio Visualizer for Alsa

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(iniparser)
BuildRequires:  libtool
BuildRequires:  make

%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep
%forgeautosetup -p1
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
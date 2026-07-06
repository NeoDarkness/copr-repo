%global forgeurl https://github.com/karlstav/cava
%global version 1.0.0
%global commit 4b12c2b043723f42567ddbfd5a516566bdf52316

Name:           cava
Version:        %{forgeversion}
Release:        %autorelease
Summary:        Console-based Audio Visualizer for ALSA

License:        MIT
URL:            %{forgeurl}

%forgemeta

Source0:        %{forgesource}

BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  iniparser-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-libs-devel

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
# No test suite available

%files
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
/lib/kbd/consolefonts/cava.psf

%changelog
%autochangelog